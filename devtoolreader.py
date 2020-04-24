#!/usr/bin/python3
import sqlite3
import snappy
import unicodedata
import argparse

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

def parse_file(dbFile, strip):
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM object_Data")
    data = cursor.fetchall()[0][0]
    conn.close()
    print("[+] Decompressing")
    decomp = snappy.decompress(data)
    if strip:
        # strip out control characters; (unfortunatley including \n)
        return remove_control_characters(decomp.decode('ascii', errors='ignore'))
    else:
        return decomp.decode('ascii', errors='ignore')

def write_to_file(data, filename):
    f = open(filename, "w")
    f.write(data)
    f.close()
    print("[+] File written")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parses Indexeddb files from firefox;pp')
    parser.add_argument('indexeddb_file', action="store", help='IndexedDB file to parse')
    parser.add_argument('-s', action="store_true", default=False, help='Srip the file of any control characters')
    parser.add_argument('-o', action="store", dest='output_file', default="output.txt", help='Set the output file name')
    args = parser.parse_args()
    output = parse_file(args.indexeddb_file, args.s)
    write_to_file(output, args.output_file)

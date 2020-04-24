# DevToolReader
Parses Indexeddb files - used to extract devtools console history. Blog post here: https://phl4nk.wordpress.com/2020/04/24/the-curious-case-of-firefoxs-devtools-storage/

### Usage
```sh
usage: devToolReader.py [-h] [-s] [-o OUTPUT_FILE] indexeddb_file
Parses Indexeddb files from firefox;

positional arguments:
  indexeddb_file  IndexedDB file to parse

optional arguments:
  -h, --help      show this help message and exit
  -s              Srip the file of any control characters
  -o OUTPUT_FILE  Set the output file name
```
### Dependencies
Needs python snappy
```sh
$ pip3 install pip3 install python-snappy
```

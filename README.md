# cryptdata


## Files:

*   `cryptdata.py`: Likely contains the core encryption/decryption logic.
*   `example-data.txt`: Unstructured data.
*   `example-patients-1000.csv`: Comma delimited sample of 1000 "patient" records.

## Usage:

```
% ./cryptdata.py --help
usage: cryptdata.py [-h] [-m {encrypt,decrypt}] infile outfile

Encrypt or decrypt a file. When encrypting create a checksum of the encrypted file.

positional arguments:
  infile                file to encrypt or decrypt
  outfile               target file for encrypted or decrypted file

options:
  -h, --help            show this help message and exit
  -m, --mode {encrypt,decrypt}
                        encrypt or decrypt infile
```

# cryptdata


## Files:

*   `cryptdata.py`: Likely contains the core encryption/decryption logic.
*   `dataset.txt`: Original dataset.
*   `decrypted_dataset.txt`: Decrypted version of `dataset.txt`.
*   `decrypted.txt`: Another decrypted file.
*   `encrypted_dataset.txt`: Encrypted version of `dataset.txt`.
*   `encrypted_dataset.txt.sha256`: SHA256 checksum for `encrypted_dataset.txt`.
*   `encrypted.txt`: Another encrypted file.
*   `encrypted.txt.sha256`: SHA256 checksum for `encrypted.txt`.
*   `patients-1000.csv`: A CSV file containing 1000 patient records.
*   `patients-decrypted.csv`: Decrypted version of patient data.
*   `patients.enc`: Encrypted patient data.
*   `patients.enc.sha256`: SHA256 checksum for `patients.enc`.

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

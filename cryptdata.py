#!/usr/bin/env python3
#
# Program: cyrptdata.py
# Author: J. Keith Lawson
# Date: March, 2024
# Description: A small command line utility to encrypt a text file and create a checksum of the resulting encrypted file.
#

import sys
import os
import argparse
import csv
import base64
import hashlib
from csv import DictWriter
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def calculate_checksum(file, algorithm='sha256'):
    # Open the file in binary mode
    with open(file, 'rb') as file:
        # Create a hash object using the specified algorithm
        hash_object = hashlib.new(algorithm)

        # Read the file in chunks to avoid loading large files into memory
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)

    # Return the hexadecimal digest of the calculated hash
    return hash_object.hexdigest()

def get_password():
    password = input("Enter your password: ")
    if args.mode == "encrypt":
        while True:
            confirm_password = input("Confirm your password: ")
            if password == confirm_password:
                return password.encode('utf-8')
            else:
                print("Passwords do not match. Please try again.")
    return password.encode('utf-8')

def get_key():
    salt = b'\x9fi\xef]F\xd9uo\x81\x10d\x07\xf9\x121\xda' 
    password = get_password()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def check_result(result):
    # Results should be between 1 - 9
    if 0 < int(result) < 11:
        return True
    else:
        return False

def encrypt_line(line, key):
    cipher_suite = Fernet(key)
    encrypted_line = cipher_suite.encrypt(line.encode())
    return encrypted_line

def encrypt(infile, outfile):
    print("Encrypting "+infile+"...")
    key = get_key()
    f = Fernet(key)

    with open(infile, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        with open(outfile, 'wb') as f_out:
            for row in csv_reader:
                if not check_result(row[11]):
                    print("ERROR: Lab result must be between 1-9 (skipping): " + ','.join(row) + "\n")
                    continue
                encrypted_line = encrypt_line(','.join(row), key)
                f_out.write(encrypted_line + b'\n')
    checksum = calculate_checksum(outfile)
    with open(outfile + ".sha256", "w") as check_file:
        print(checksum, file=check_file)
    print("Encryption complete. Encrypted file saved as", outfile)
    print(f"Checksum (SHA-256) of '{outfile}': {checksum}")

def decrypt(infile,outfile):
    print("Decrypting "+infile+"...")
    key = get_key()
    f = Fernet(key)
    with open(infile + ".sha256", 'r') as check_file:
        read_checksum = check_file.read()
    read_checksum = read_checksum.rstrip()
    checksum = calculate_checksum(infile)
    if read_checksum != checksum:
        print(f"Error: {infile} checksum does not match.\nStored: {read_checksum}\n{infile}: {checksum}")
        sys.exit(1) 
    with open(infile, 'r') as f_in:
        with open(outfile, 'w', newline='') as f_out:
            for line in f_in:
                line = line.rstrip()
                try:
                    decrypted_line = f.decrypt(line)
                    decrypted_line = decrypted_line.decode()
                    f_out.write(decrypted_line + '\n')
                except Exception as e:
                    print("Error decrypting data: " + str(e))
                    sys.exit(1)
    print("Decryption complete. Decrypted file saved as", outfile)
def read_file_and_print_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

def prompt_to_overwrite(filename):
    while True:
        response = input(f"The file '{filename}' already exists. Do you want to overwrite it? (y/n): ").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please enter y (yes) or n (no).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Encrypt or decrypt a file. When encrypting create a checksum of the encrypted file.')
    parser.add_argument('-m', '--mode', default='encrypt', choices=['encrypt', 'decrypt'], help='encrypt or decrypt infile')
    parser.add_argument('infile', help='file to encrypt or decrypt') 
    parser.add_argument('outfile', help='target file for encrypted or decrypted file') 
    args = parser.parse_args()

    if not os.path.exists(args.infile):
        print("Error: Input file " + args.infile + " does not exist.")
        quit() 

    if os.path.exists(args.outfile):
        if not prompt_to_overwrite(args.outfile):
            quit()
    
    if args.mode == "encrypt":
        encrypt(args.infile,args.outfile) 
    elif args.mode == "decrypt":
        decrypt(args.infile,args.outfile) 
    else:
        print("Invalid mode. Please choose '-m encrypt' for encryption or '-d decrypt' for decryption.")
        quit() 

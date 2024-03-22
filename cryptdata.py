#!/usr/bin/env python3

import sys
import os.path
import argparse

def encrypt():
    print("Going to encrypt\n")

def decrypt():
    print("Going to decrypt\n")

def read_file_and_print_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

def prompt_to_overwrite(filename):
    while True:
        response = input(f"The file '{filename}' already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Encrypt or decrypt a file. When encrypting create a checksum of the encrypted file.')
    parser.add_argument('-m', '--mode', default='encrypt', choices=['encrypt', 'decrypt'], help='encrypt or decrypt input_file')
    parser.add_argument('input_file', help='file to encrypt or decrypt') 
    parser.add_argument('output_file', help='target file for encrypted or decrypted file') 
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        process = encrypt
    elif args.mode == "decrypt":
        process = decrypt
    else:
        print("Invalid mode. Please choose '-m encrypt' for encryption or '-d decrypt' for decryption.")
        quit() 
    
    if not os.path.exists(args.input_file):
        print("Error: Input file " + args.input_file + " does not exist.")
        quit() 

    if os.path.exists(args.output_file):
        if not prompt_to_overwrite(args.output_file):
            quit()

    with open(args.input_file, "r") as f:
        data = f.read()
    
    processed_data = process(data)
    
    with open(args.output_file, "w") as f:
        f.write(processed_data)
    
    print(f"File {args.input_file} {'encrypted' if args.mode == '-e' else 'decrypted'} and saved to {args.output_file}.")

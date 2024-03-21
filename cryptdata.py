#!/usr/bin/env python3

import sys
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

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python [-ed] cryptdata.py input_file output_file password")
        sys.exit(1)
        
    parser = argparse.ArgumentParser(description="Command line parser")
    parser.add_argument("subroutine", choices=["-e", "-d"], help="Choose subroutine to call: 'one' or 'two'")
    args = parser.parse_args()
    if args.subroutine == "-e":
        encrypt()
    elif args.subroutine == "two":
        decrypt()

    file_path = sys.argv[1]
    read_file_and_print_lines(file_path)



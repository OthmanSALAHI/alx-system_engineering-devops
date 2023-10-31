#!/usr/bin/python3
from sys import argv
from os  import scandir, system

def main():
    for file in scandir('.'):
        if file.is_file() and file.name != "README.md" and file.name != "push.py":
            print(f"(*) chmod u+x {file.name}")
            system(f"chmod u+x {file.name}")

if __name__ == "__main__":
    main()

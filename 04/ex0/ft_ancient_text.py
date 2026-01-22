#!/usr/bin/env python3
from collections.abc import Generator
from typing import BinaryIO


def get_next_line(file: BinaryIO) -> Generator[int, str, None]:
    line = 1
    while line:
        line = file.readline()
        if line == "" or line is None:
            return None
        yield line


def ft_ancient_text():
    file_name = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")
    try:
        with open(file_name, 'r') as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            for line in get_next_line(file):
                print(line, end='')
            file.close()
        print("\n\nData recovery complete.", end=" ")
    except (FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found. Run data generator first.\n")
    finally:
        print("Storage unit disconnected")


if __name__ == "__main__":
    ft_ancient_text()

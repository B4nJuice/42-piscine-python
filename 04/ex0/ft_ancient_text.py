#!/usr/bin/env python3

def ft_ancient_text():
    file_name = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")
    try:
        with open(file_name, 'r') as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            content = file.read()
            print(content)
        print("\nData recovery complete.", end=" ")
    except (FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found. Run data generator first.\n")
    finally:
        print("Storage unit disconnected")


if __name__ == "__main__":
    ft_ancient_text()

#!/usr/bin/env python3

def ft_vault_security():
    file_name = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open(file_name, 'r+') as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = file.read()
            print(content)
            print("\nSECURE PRESERVATION:")
            new_content = "[CLASSIFIED] New security protocols archived"
            print(new_content)
            file.write("\n" + new_content)
            print("Vault automatically sealed upon completion")
    except (FileNotFoundError, PermissionError) as e:
        print(e)
    finally:
        print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()

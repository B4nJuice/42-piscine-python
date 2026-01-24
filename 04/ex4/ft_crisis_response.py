#!/usr/bin/env python3

def ft_recover_file(file_name: str) -> None:
    print(f"CRISIS ALERT: Attempting to access to '{file_name}'")
    status = "Normal operations resumed"
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered = ''{content}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        status = "Crisis handled, system stable"
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        status = "Crisis handled, security maintained"
    finally:
        print(f"STATUS: {status}")


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    ft_recover_file("lost_archive.txt")
    print()
    ft_recover_file("classified_vault.txt")
    print()
    ft_recover_file("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()

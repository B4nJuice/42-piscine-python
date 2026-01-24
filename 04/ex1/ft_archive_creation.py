#!/usr/bin/env python3

def ft_archive_creation():
    file_name = "new_discovery.txt"

    print("=== CYBER ARCHIVES - DATA PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file_name}")
    try:
        with open(file_name, 'a') as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            content = (
                "[ENTRY 001] New quantum algorithm discovered\n" +
                "[ENTRY 002] Efficiency increased by 347%\n" +
                "[ENTRY 003] Archived by Data Archivist trainee\n"
                )
            file.write(content)
            print(content)
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError as e:
        print(e)


if __name__ == "__main__":
    ft_archive_creation()

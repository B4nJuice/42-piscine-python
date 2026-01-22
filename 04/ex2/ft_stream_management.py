#!/usr/bin/env python3

import sys


def standard_print(content: str) -> None:
    sys.stdout.write("[STANDARD] " + content + "\n")


def alert_print(content: str) -> None:
    sys.stderr.write("[ALERT] " + content + "\n")


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    standard_print(f"Archive status from {archivist_id}: {status_report}")
    alert_print("System diagnostic: Communication channels verified")
    standard_print("Data transmission complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()

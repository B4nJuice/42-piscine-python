#!/usr/bin/env python3

import sys


def standard_print(content: str) -> None:
    sys.stdout.write("[STANDARD] " + content + "\n")


def alert_print(content: str) -> None:
    sys.stderr.write("[ALERT] " + content + "\n")


def ft_input(demand: str) -> str:
    sys.stdout.write(demand)
    sys.stdout.flush()
    response = sys.stdin.readline().replace("\n", "")
    return response


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = ft_input("Input Stream active. Enter archivist ID: ")
    status_report = ft_input("Input Stream active. Enter status report: ")

    print()

    standard_print(f"Archive status from {archivist_id}: {status_report}")
    alert_print("System diagnostic: Communication channels verified")
    standard_print("Data transmission complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()

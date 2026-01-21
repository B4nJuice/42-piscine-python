#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    '''
    Displays the program name and its arguments.
    '''
    argv = sys.argv
    argc = len(argv)
    program_name = argv[0]

    print("=== Command Quest===")
    if argc < 2:
        print("No arguments provided")
    print(f"Program name: {program_name}")
    if argc >= 2:
        print(f"Arguments received: {argc - 1}")
        for i, arg in enumerate(argv[1:], start=1):
            print(f"Argument {i} : {arg}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()

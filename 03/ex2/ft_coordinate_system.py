#!/usr/bin/env python3

import sys
import math


def calculate_distance(coord1: tuple[int, int, int],
                       coord2: tuple[int, int, int]) -> None:
    '''
    Calculates and prints the Euclidean distance between two 3D coordinates.
    '''
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {coord1} and {coord2}: {distance}")


def parse_coordinates() -> list[tuple[int, int, int]]:
    argv = sys.argv
    argc = len(argv)

    if (argc != 2):
        raise Exception("Parsing error: only one argument has to be given :\
 [(x, y, z,), (x, y, z,) ...]")

    string_to_parse = argv[1]
    string_to_parse = string_to_parse.strip("[]")
    string_to_parse = string_to_parse.replace(" ", "")

    coords = string_to_parse.split("),")

    tuples_coords = []

    for coord in coords:
        coord = coord.strip("()")

        print(f"\nParsing coordinates: \"{coord}\"")

        point = coord.split(",")

        try:
            tuple_coord = tuple(map(int, point))
            if len(tuple_coord) != 3:
                raise Exception("Parsing error: coordinates take only 3 values\
: (x, y, z)")
            tuples_coords.append(tuple_coord)
            print(f"Parsed position: {tuple_coord}")
            calculate_distance((0, 0, 0), tuple_coord)
        except Exception as e:
            print(f"Parsing error: {e}")

    return tuples_coords


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    '''
    Creates a 3D coordinate position from x, y, and z values.
    '''
    coord = []

    coord.append(x)
    coord.append(y)
    coord.append(z)

    coord = tuple(coord)

    print(f"Position created: {coord}")
    calculate_distance((0, 0, 0), coord)

    return (coord)


def get_xyz_coord(coord: tuple[int, int, int]) -> str:
    '''
        Returns a formatted string representing the x, y, and z values of a 3D
        coordinate by unpacking the tuple.
    '''
    x, y, z = coord

    return (f"x={x}, y={y}, z={z}")


def ft_coordinate_system() -> None:
    '''
    Demonstrates the creation, parsing, and distance calculation of 3D
    coordinates.
    '''
    coords = []

    starting_pos = create_position(10, 20, 5)
    coords.append(starting_pos)

    try:
        parsed_coords = parse_coordinates()

        for parsed_coord in parsed_coords:
            coords.append(parsed_coord)

        print("\n=== Unpacking demonstration: ===")

        n_coords = len(coords)

        for i, coord in enumerate(coords):
            if i != n_coords - 1:
                player_pos = get_xyz_coord(coord)
                next_player_pos = get_xyz_coord(coords[i + 1])

                print(f"\nPlayer position: {player_pos}")
                print(f"Player move to {next_player_pos}")
                calculate_distance(coord, coords[i + 1])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    ft_coordinate_system()

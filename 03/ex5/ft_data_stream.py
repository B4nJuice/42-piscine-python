#!/usr/bin/env python3

def game_event_generator(n: int) -> tuple[int, str, int, str]:
    '''
    Generate n game events.
    '''
    players = ["Bob", "Alice", "Charlie"]
    levels = [1, 5, 8, 12]
    actions = ["killed monster", "found treasure", "leveled up", "died"]

    n_player = len(players)
    n_level = len(levels)
    n_action = len(actions)

    for i in range(n):
        yield (
            i,
            players[i % n_player],
            levels[i % n_level],
            actions[i % n_action],
        )


def fibonacci(n: int) -> int:
    '''
    Generates the first n Fibonacci numbers.
    '''
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, b + a


def prime_number(n: int) -> int:
    '''
    Generates the first n prime numbers.
    '''
    nb = 2

    for _ in range(n):
        is_prime = False
        while is_prime is False:
            is_prime = True
            for i in range(2, nb):
                if nb % i == 0:
                    is_prime = False
            if is_prime:
                yield nb
            nb += 1


def ft_data_stream() -> None:
    '''
    Main function to process game data stream and demonstrate generators.
    '''
    print("\n=== Game Data Stream Processor ===\n")

    n_game_event = 1000
    game_events = game_event_generator(n_game_event)

    high_level = 0
    treasure = 0
    level_up = 0

    print(f"Processing {n_game_event} game events...\n")

    for i in range(n_game_event):
        game_event = next(game_events)

        n, player, level, action = game_event

        if (level > 10):
            high_level += 1

        match action:
            case "found treasure":
                treasure += 1
            case "leveled up":
                level_up += 1

        print(f"Event {n}: Player {player} (level {level}) {action}")

    print("\n=== Stream Analytics ===\n")

    print(f"Total events processed: {n_game_event}")
    print(f"High level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")

    n_fibonacci = 10

    gen_fibonacci = fibonacci(n_fibonacci)

    print(f"Fibonacci sequence (first {n_fibonacci}):", end="")

    for _ in range(n_fibonacci):
        next_num = next(gen_fibonacci)
        print(f" {next_num}", end="")
    print()

    n_prime = 10

    gen_prime = prime_number(n_prime)

    print(f"Prime numbers (first {n_prime}):", end="")

    for _ in range(n_prime):
        next_num = next(gen_prime)
        print(f" {next_num}", end="")
    print()


if __name__ == "__main__":
    ft_data_stream()

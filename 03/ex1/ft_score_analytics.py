#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    '''
    Displays analytics for player scores provided as command-line arguments.
    '''
    argv = sys.argv
    argc = len(argv)

    player_count = argc - 1
    player_scores = []

    high_score = None
    low_score = None

    if argc < 2:
        print("No scores provided. Usage: ./ft_score_analytics.py\
 <score1> <score2> ...")
        return
    for arg in argv[1:]:
        try:
            score = int(arg)

            player_scores.append(score)

            if high_score is None or high_score < score:
                high_score = score
            if low_score is None or low_score > score:
                low_score = score
        except Exception:
            print(f"Oops, {arg} is not a valid score.")
            return

    total_score = sum(player_scores)
    average_score = total_score / player_count
    score_range = high_score - low_score

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {player_scores}")
    print(f"Total players: {player_count}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    ft_score_analytics()

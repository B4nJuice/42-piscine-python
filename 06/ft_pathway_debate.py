#!/usr/bin/env python3

from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy.transmutation


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")

    print()

    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold(): " + lead_to_gold())
    print("stone_to_gem(): " + stone_to_gem())

    print()

    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone(): " + philosophers_stone())
    print("elixir_of_life(): " + elixir_of_life())

    print()

    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          + alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone(): "
          + alchemy.transmutation.philosophers_stone())

    print()

    print("Both pathways work! Absolute: clear, Relative: concise")

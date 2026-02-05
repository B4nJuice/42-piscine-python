#!/usr/bin/env python3

import alchemy.grimoire as grim


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")

    print()

    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): "
          + grim.validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"): "
          + grim.validate_ingredients("dragon scales"))

    print()

    print("Testing spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\")"
          + grim.record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\")"
          + grim.record_spell("Dark Magic", "shadow"))

    print()

    print("Testing late import technique:")
    print("record_spell(\"Lightning\", \"air\")"
          + grim.record_spell("Lightning", "air"))

    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")

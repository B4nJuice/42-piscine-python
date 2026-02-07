#!/usr/bin/env python3

from typing import Any
from .CreatureCard import CreatureCard
from .Card import Rarity


def add_mana(game_state: dict[str], quantity: int) -> None:
    new_quantity = game_state.get("available_mana") + quantity
    game_state.update({"available_mana": new_quantity})


def try_play(card: CreatureCard, game_state: dict[str, Any]) -> None:
    available_mana: int = game_state.get("available_mana")
    playable_state: bool = card.is_playable(available_mana)

    print(f"Playing {card.name} with {available_mana} mana available:")
    print(f"Playable : {playable_state}")
    if playable_state:
        play_result: dict[str, str | int] = card.play(game_state)
        add_mana(game_state, -play_result.get("mana_used"))
        print(f"Play result : {play_result}")


def try_attack(card: CreatureCard, target: CreatureCard) -> None:
    print(f"{card.name} attacks {target.name}")
    attack_result = card.attack_target(target)
    print(f"Attack result: {attack_result}")


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    print()

    print("Testing Abstract Base Class Design:")

    print()

    try:
        fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon",
            5,
            Rarity.LEGENDARY.value,
            7,
            5
        )

        print(f"CreatureCard Info:\n{fire_dragon.get_card_info()}")

        print()

        game_state: dict[str, int] = {"available_mana": 6}
        try_play(fire_dragon, game_state)

        print()

        goblin_warrior: CreatureCard = CreatureCard(
            "Goblin Warrior",
            3,
            Rarity.RARE.value,
            4,
            6
        )

        try_attack(fire_dragon, goblin_warrior)

        print()

        print(f"Testing insufficient mana ({game_state.get('available_mana')}\
 available)")
        try_play(fire_dragon, game_state)

        print()

        print("Abstract pattern successfully demonstrated!")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

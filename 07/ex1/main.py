#!/usr/bin/env python3

from ex1 import (
        SpellCard,
        SpellEffectType,
        NumType,
        ArtifactCard,
        ArtifactEffectType,
        Deck
    )
from ex0 import Rarity, CreatureCard, Card


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")

    print()

    print("Building deck with different card types...")

    deck: Deck = Deck()

    fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon",
            5,
            Rarity.LEGENDARY.value,
            5,
            7
        )

    lightning_bolt: SpellCard = SpellCard(
            "Lightning Bolt",
            3,
            Rarity.COMMON.value,
            SpellEffectType.DAMAGE.value,
            3,
            {"num": 1, "num_type": NumType.EXACT}
        )

    mana_crystal: ArtifactCard = ArtifactCard(
            "Mana Crysral",
            2,
            Rarity.EPIC.value,
            ArtifactEffectType.MANA.value,
            1,
            -1
        )

    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    print(deck.get_deck_stats())

    print()

    print("Drawing and playing cards:")

    print()

    deck.shuffle()

    game_state: dict[str, int] = {"available_mana": 100}

    while len(deck.cards):
        card: Card = deck.draw_card()
        print(f"Drew: {card.name}")
        print(f"Play result: {card.play(game_state)}")
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")

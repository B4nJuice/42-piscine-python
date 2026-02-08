#!/usr/bin/env python3

from ex1 import SpellCard, SpellEffectType, NumType, ArtifactCard, ArtifactEffectType, Deck
from ex0 import Rarity, CreatureCard


if __name__ == "__main__":
    test_spell: SpellCard = SpellCard(
            "spell",
            49,
            Rarity.COMMON.value,
            SpellEffectType.DAMAGE.value,
            2,
            {"num": 3, "num_type": NumType.MAX}
        )

    test_creature: CreatureCard = CreatureCard(
            "creature", 49, Rarity.COMMON.value, 1, 5
        )

    game_state = {"available_mana": 100}

    print(test_creature.play(game_state))

    targets = []
    targets.append(test_creature)

    print(test_creature.get_card_info())

    print(test_spell.play(game_state))
    print(test_spell.resolve_effect([test_creature]))

    print(test_creature.get_card_info())

    print(game_state.get("available_mana"))

    test_artifact = ArtifactCard("artifact", 2, Rarity.LEGENDARY.value, ArtifactEffectType.MANA.value, 50, -1)

    print(test_artifact.play(game_state))
    print(test_artifact.activate_ability(game_state))

    print(game_state.get("available_mana"))

    deck = Deck()
    deck.add_card(test_creature)
    deck.add_card(test_artifact)
    deck.add_card(test_spell)

    deck.shuffle()

    print(deck.draw_card().name)

    print(deck.get_deck_stats())

from ex3 import CardFactory
from ex0 import Card, CreatureCard, Rarity
from ex1 import (
                    ArtifactCard,
                    SpellCard,
                    SpellEffectType,
                    ArtifactEffectType,
                    NumType,
                    Deck
                 )
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_or_power = name_or_power.lower()
            match name_or_power:
                case "dragon":
                    return CreatureCard(
                            "Fire Dragon",
                            5,
                            Rarity.RARE.value,
                            3,
                            8
                        )

                case "goblin":
                    return CreatureCard(
                            "Goblin Warrior",
                            5,
                            Rarity.RARE.value,
                            5,
                            5
                        )

                case "minautor":
                    return CreatureCard(
                            "Minautor",
                            7,
                            Rarity.LEGENDARY.value,
                            5,
                            10
                        )

                case _:
                    return CreatureCard(
                            "Fire spirit",
                            2,
                            Rarity.COMMON.value,
                            1,
                            3
                        )
        elif isinstance(name_or_power, int):
            return CreatureCard(
                            "Elemental spirit",
                            name_or_power,
                            Rarity.UNCOMMON.value,
                            2,
                            name_or_power
                        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_or_power = name_or_power.lower()

            match name_or_power:
                case "fireball":
                    return SpellCard(
                        "Fireball",
                        3,
                        Rarity.COMMON.value,
                        SpellEffectType.DAMAGE.value,
                        3,
                        {"num_type": NumType.MAX, "num": 3}
                    )

                case "poison":
                    return SpellCard(
                        "Poison Malediction",
                        7,
                        Rarity.LEGENDARY.value,
                        SpellEffectType.DAMAGE.value,
                        3,
                        {"num_type": NumType.MIN, "num": 1}
                    )

                case _:
                    return SpellCard(
                        "Angel Dust",
                        3,
                        Rarity.UNCOMMON.value,
                        SpellEffectType.BUFF.value,
                        5,
                        {"num_type": NumType.EXACT, "num": 1}
                    )

        elif isinstance(name_or_power, int):
            return SpellCard(
                        "Potion of Healing",
                        name_or_power,
                        Rarity.COMMON.value,
                        SpellEffectType.DAMAGE.value,
                        name_or_power,
                        {"num_type": NumType.MAX, "num": 3}
                    )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArtifactCard(
            "Mana Crystal",
            3,
            Rarity.COMMON.value,
            ArtifactEffectType.MANA.value,
            2,
            3
        )

    def create_themed_deck(self, size: int) -> dict:
        creatures: dict[str, callable | list[str]] = {
            "function": self.create_creature,
            "types":
                ["dragon", "goblin", "minautor", "fire_spirit"]
            }
        spells: dict[str, callable | list[str]] = {
            "function": self.create_spell,
            "types":
                ["fireball", "poison"]
            }
        artifacts: dict[str, callable | list[str]] = {
            "function": self.create_artifact,
            "types":
                ["mana_crystal"]
            }

        deck: Deck = Deck()

        for _ in range(size):
            card_type: dict[str, callable | list[str]] = (
                random.choice([creatures, spells, artifacts])
            )

            deck.add_card(
                card_type.get("function")(
                    random.choice(card_type.get("types"))
                )
            )

        return {"deck": deck}

    def get_supported_types(self) -> dict:
        creatures: list[str] = [
                    "dragon",
                    "goblin",
                    "minautor",
                    "fire_spirit",
                    "elemental_spirit"
                ]
        spells: list[str] = [
                    "fireball",
                    "poison",
                    "angel_dust",
                    "potion_of_healing"
                ]
        artifacts: list[str] = [
                    "mana_crystal"
                ]

        supported_types: dict[str, list[str]] = {}
        supported_types.update({"creatures": creatures})
        supported_types.update({"spells": spells})
        supported_types.update({"artifacts": artifacts})

        return supported_types

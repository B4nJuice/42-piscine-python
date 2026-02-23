from ex0 import Card
from ex1 import SpellCard
from ex2 import Combatable, Magical
from enum import Enum


class CombatType(Enum):
    MELEE = "melee"
    DISTANCE = "distance"
    PSY = "psy"


class EliteCard(Card, Combatable, Magical):
    def __init__(
                self,
                name: str,
                cost: int,
                rarity: str,
                attack: int,
                health: int,
                mana: int,
                defense: int,
                combat_type: CombatType
            ) -> None:
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.set_health(health)
        self.set_mana(mana)
        self.set_combat_type(combat_type)
        self.set_defense(defense)

    def attack(self, target: Card) -> dict:
        attack_result: dict[str, str | int] = {}

        attack_result.update({"attacker": self.name})
        attack_result.update({"target": target.name})
        attack_result.update({"damage": self.attack_power})
        attack_result.update({"combat_type": self.combat_type.value})

        return attack_result

    def defend(self, incomming_damage: int) -> dict:
        defense_result: dict[str, str | bool] = {}

        defense_result.update({"defender": self.name})

        damage_taken = max(0, incomming_damage - self.defense)
        self.health -= damage_taken
        defense_result.update({"damage_taken": damage_taken})
        defense_result.update({
                "damage_blocked": incomming_damage - damage_taken
            })
        defense_result.update({"still_alive": self.health > 0})

        return defense_result

    def get_combat_stats(self) -> dict:
        combat_stats: dict[str, int | str] = {}

        combat_stats.update({"attack": self.attack})
        combat_stats.update({"defense": self.defense})
        combat_stats.update({"combat_type": self.combat_type.value})

        return combat_stats

    def cast_spell(self, targets: list[Card], spell: SpellCard) -> dict:
        if self.mana >= spell.cost:
            self.mana -= spell.cost
        else:
            raise Exception(f"Not enough mana to cast {spell.name}.")

        spell.resolve_effect(targets)

        cast_result: dict[str, str | list | int] = {}

        cast_result.update({"caster": self.name})
        cast_result.update({"spell": spell.name})
        cast_result.update({"targets": [target.name for target in targets]})
        cast_result.update({"mana_used": spell.cost})

        return cast_result

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount < 1:
            raise ValueError(
                    "Channel mana amount has to be a positive integer."
                )
        self.mana += amount

        channel_result: dict[str, int] = {}

        channel_result.update({"channeled": amount})
        channel_result.update({"total_mana": self.mana})

        return channel_result

    def get_magic_stats(self) -> dict:
        magic_stats: dict[str, int] = {}

        magic_stats.update({"total_mana": self.mana})

        return magic_stats

    def play(self, game_state: dict) -> dict:
        play_result: dict[str, str | int] = {}
        available_mana: int = game_state.get("available_mana")

        if self.is_playable(available_mana):
            play_result.update({"card_played": self.name})
            play_result.update({"mana_used": self.cost})
            play_result.update({"effect": "EliteCard summoned to battlefield"})

            game_state.update({"available_mana": available_mana - self.cost})

            self.on_board = True

            return play_result

        return None

    def set_combat_type(self, combat_type: CombatType) -> None:
        if not isinstance(combat_type, CombatType):
            raise ValueError("Combat type has to be in the CombatType Enum.")
        self.combat_type: int = combat_type

    def set_defense(self, defense: int) -> None:
        if not isinstance(defense, int) or defense < 0:
            raise ValueError("Defense has to be a non-negative integer.")
        self.defense: int = defense

    def set_mana(self, mana: int) -> None:
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("Mana has to be a non-negative integer.")
        self.mana: int = mana

    def set_attack(self, attack: int) -> None:
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack has to be a non-negative integer.")
        self.attack_power: int = attack

    def set_health(self, health: int) -> None:
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health has to be a non-negative integer.")
        self.health: int = health

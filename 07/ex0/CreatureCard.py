from typing import Any
from .Card import Card


class CreatureCard(Card):
    def __init__(
                self,
                name: str,
                cost: int,
                rarity: str,
                attack: int,
                health: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.set_health(health)

    def set_attack(self, attack: int) -> None:
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack has to be a non-negative integer.")
        self.attack: int = attack

    def set_health(self, health: int) -> None:
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health has to be a non-negative integer.")
        self.health: int = health

    def get_card_info(self) -> dict[str, str | int]:
        card_info: dict[str, str | int] = super().get_card_info()

        card_info.update({"type": "Creature"})
        card_info.update({"attack": self.attack})
        card_info.update({"health": self.health})

        return card_info

    def play(self, game_state: dict[str, Any]) -> dict[str, str | int] | None:
        play_result: dict[str, str | int] = {}
        available_mana: int = game_state.get("available_mana")

        if self.is_playable(available_mana):
            play_result.update({"card_played": self.name})
            play_result.update({"mana_used": self.cost})
            play_result.update({"effect": "Creature summoned to battlefield"})

            game_state.update({"available_mana": available_mana - self.cost})

            self.on_board = True

            return play_result

        return None

    def attack_target(self, target: 'CreatureCard') -> dict[str, str | bool]:
        attack_result: dict[str, str | bool] = {}

        attack_result.update({"attacker": self.name})
        attack_result.update({"target": target.name})
        target.health -= self.attack
        attack_result.update({"damage_dealt": self.attack})
        attack_result.update({"combat_resolved": not target.health > 0})

        return attack_result

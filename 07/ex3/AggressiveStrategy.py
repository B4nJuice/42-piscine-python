from ex3 import GameStrategy
from ex0 import Card, CreatureCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana: int = 7

        actions: dict[str, int | list[Card | str]] = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }

        hand.sort(
                key=lambda x: (
                    0 if isinstance(x, CreatureCard)
                    else 1, x.cost
                )
        )

        for card in hand:
            if card.cost <= available_mana:
                available_mana -= card.cost
                actions["mana_used"] += card.cost
                actions["cards_played"].append(card)

                hand.remove(card)
                battlefield.append(card)

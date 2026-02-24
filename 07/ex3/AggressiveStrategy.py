from ex3 import GameStrategy
from ex0 import Card, CreatureCard
from ex1 import SpellCard, SpellEffectType, NumType


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

        for card in battlefield:
            if isinstance(card, CreatureCard):
                actions["damage_dealt"] += card.attack
                actions["targets_attacked"].append(
                        self.prioritize_targets(["Enemy Player"])
                    )

            elif isinstance(card, SpellCard):
                if SpellCard.effect_type == SpellEffectType.DAMAGE.value:
                    match SpellCard.num_target.get("num_type"):
                        case NumType.EXACT:
                            if SpellCard.num_target.get("num_type") == 1:
                                actions["damage_dealt"] += card.effect_power

                        case NumType.MIN:
                            if SpellCard.num_target.get("num_type") <= 1:
                                actions["damage_dealt"] += card.effect_power

                        case NumType.MAX:
                            if SpellCard.num_target.get("num_type") >= 1:
                                actions["damage_dealt"] += card.effect_power

                        case _:
                            continue
                    actions["targets_attacked"].append(
                            self.prioritize_targets(["Enemy Player"])
                        )

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        available_targets = [
                x for x in available_targets if (
                        isinstance(x, CreatureCard) or isinstance(x, str)
                    )
            ]

        available_targets.sort(
                key=lambda x: (
                    0 if isinstance(x, CreatureCard)
                    else 1, getattr(x, "health", float("inf"))
                )
        )

        return available_targets

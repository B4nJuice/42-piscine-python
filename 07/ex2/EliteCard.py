from ex0 import Card
from ex2 import Combatable, Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self) -> None:
        pass

    def attack(self, target: Card) -> dict:
        pass

    def defend(self, incomming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, targets: list[Card]) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

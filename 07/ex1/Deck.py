from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
from random import randint


class Deck():
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card):
        if not isinstance(card, Card):
            raise ValueError("Cards in deck have to be cards objects.")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True

        return False

    def shuffle(self) -> None:
        new_deck: list[Card] = []
        len_deck = len(self.cards)

        for i in range(len_deck):
            card_index: int = randint(0, len_deck - i - 1)
            new_deck.append(self.cards.pop(card_index))

        self.cards = new_deck

    def draw_card(self) -> Card:
        return (self.cards.pop())

    def get_deck_stats(self) -> dict[str, int | float]:
        deck_stats: dict[str, int | float] = {}
        len_deck: int = len(self.cards)

        deck_stats.update({"total_cards": len_deck})
        deck_stats.update({"creatures": len(
                [card for card in self.cards if isinstance(card, CreatureCard)]
            )})
        deck_stats.update({"spells": len(
                [card for card in self.cards if isinstance(card, SpellCard)]
            )})
        deck_stats.update({"artifacts": len(
                [card for card in self.cards if isinstance(card, ArtifactCard)]
            )})

        total_cost: int = sum([card.cost for card in self.cards])
        avg_cost: float = total_cost / len_deck

        deck_stats.update({"avg_cost": avg_cost})

        return deck_stats

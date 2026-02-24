from ex3 import CardFactory, GameStrategy
from ex1 import Deck
from ex0 import Card


class GameEngine():
    def __init__(self):

        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(
                self,
                factory: CardFactory,
                strategy: GameStrategy
            ) -> None:

        self.factory: CardFactory = factory
        self.strategy: GameStrategy = strategy

    def simulate_turn(self) -> dict:
        if not (getattr(self, "factory", False)
                and getattr(self, "strategy", False)):
            raise Exception("Please configure engine before simulating turn.")

        deck_size: int = 10
        deck: Deck = self.factory.create_themed_deck(deck_size).get("deck")

        self.cards_created += deck_size

        deck.shuffle()

        hand: list[Card] = []

        for _ in range(5):
            hand.append(deck.draw_card())

        hand_str: list[str] = []

        for card in hand:
            hand_str.append(f"{card.name} ({card.cost})")

        print(f"Simulating {self.strategy.get_strategy_name()} turn...")
        print(f"Hand: {hand_str}")

        actions: dict[str, int | list[str]] =\
            self.strategy.execute_turn(hand, [])

        self.turns_simulated += 1
        self.total_damage += actions.get("damage_dealt")

        return actions

    def get_engine_status(self) -> dict:
        engine_status: dict[str, int | str] = {}

        engine_status.update({"turns_simulated": self.turns_simulated})
        engine_status.update({"strategy_used": self.strategy.name})
        engine_status.update({"total_damage": self.total_damage})
        engine_status.update({"card_created": self.cards_created})

        return engine_status

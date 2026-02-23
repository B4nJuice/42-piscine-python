from ex3 import CardFactory, GameStrategy


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
        pass

    def get_engine_status(self) -> dict:
        engine_status: dict[str, int | str] = {}

        engine_status.update({"turns_simulated": self.turns_simulated})
        engine_status.update({"strategy_used": self.strategy.name})
        engine_status.update({"total_damage": self.total_damage})
        engine_status.update({"card_created": self.cards_created})

        return engine_status

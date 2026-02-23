from ex3 import CardFactory, GameStrategy


class GameEngine():
    def __init__(self):
        pass

    def configure_engine(
                self,
                factory: CardFactory,
                strategy: GameStrategy
            ) -> None:
        pass

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass

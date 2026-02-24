from ex3 import (
        FantasyCardFactory,
        AggressiveStrategy,
        CardFactory,
        GameEngine,
        GameStrategy
    )

if __name__ == "__main__":
    factory: CardFactory = FantasyCardFactory()
    strategy: GameStrategy = AggressiveStrategy()
    game_engine: GameEngine = GameEngine()

    game_engine.configure_engine(factory, strategy)

    print("=== DataDeck Game Engine ===")

    print()

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print()

    actions: dict[str, int | list[str]] = game_engine.simulate_turn()

    print()

    print("Game Report:")
    print(actions)

    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

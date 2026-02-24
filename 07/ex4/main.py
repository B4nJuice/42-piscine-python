from ex4 import TournamentCard, TournamentPlatform
from ex0 import Rarity


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")

    fire_dragon: TournamentCard = TournamentCard(
            "Fire Dragon",
            0,
            Rarity.EPIC.value,
            15,
            4,
            4,
            1200
        )

    ice_wizard: TournamentCard = TournamentCard(
            "Ice Wizard",
            0,
            Rarity.EPIC.value,
            10,
            6,
            4,
            1150
        )

    print("Registering Tournament Cards...")

    tournament_platform: TournamentPlatform = TournamentPlatform()
    fire_dragon_id: str = tournament_platform.register_card(fire_dragon)
    ice_wizard_id: str = tournament_platform.register_card(ice_wizard)

    print()

    for card_id, card in tournament_platform.cards.items():
        print(f"- {card.name} (ID: {card_id})")
        print(f"- Interfaces:\
 {[interface.__name__ for interface in card.__class__.__bases__]}")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")
        print()

    print("Creating tournament match...")

    match_result: dict[str, int | str] = tournament_platform.create_match(
                                                            'fire_dragon_001',
                                                            'ice_wizard_001'
                                                        )
    print(f"Match Result: {match_result}")

    print()

    tournament_leaderboard: list[TournamentCard] =\
        tournament_platform.get_leaderboard()

    print("Tournament Leaderboard")
    for pos, card in enumerate(tournament_leaderboard):
        print(f"{pos + 1}. {card.name} - Rating: {card.rating}\
 ({card.wins}-{card.losses})")

    print()

    platform_report: dict[str, int | str] =\
        tournament_platform.generate_tournament_report()

    print("Platform Report:")
    print(platform_report)

    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

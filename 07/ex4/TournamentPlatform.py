from ex4 import TournamentCard
import random


class TournamentPlatform():
    def __init__(self):
        self.match_played: int = 0
        self.cards = {}

    def register_card(self, card: TournamentCard) -> str:
        id_name: str = card.name.replace(" ", "_").lower()
        card_keys = list(self.cards.keys())
        id_num: int = sum(1 for cid in card_keys if cid.startswith(id_name) and
                          len(id_name) + 3 == len(cid)) + 1

        card_id: str = f"{id_name}_{'0' * (3 - len(str(id_num)))}{id_num}"

        self.cards.update({card_id: card})

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError(
                "Cards need to be registered before creating a match."
            )

        cards = [card1_id, card2_id]
        random.shuffle(cards)

        self.match_played += 1

        while True:
            for idx, card in enumerate(cards):
                attacker: TournamentCard = self.cards[card]
                defender: TournamentCard = self.cards[cards[1 - idx]]

                attack_result: dict[str, int | str] = attacker.attack(defender)
                defender.health -= attack_result.get("damage_dealt")
                if defender.health <= 0:
                    attacker.wins += 1
                    defender.losses += 1
                    k: int = 32
                    attacker_p: float = (
                        1 /
                        (1 + pow(10, ((
                            attacker.calculate_rating() -
                            defender.calculate_rating()
                            )
                            / 400)))
                        )
                    defender_p: float = (
                        1 /
                        (1 + pow(10, ((
                            defender.calculate_rating() -
                            attacker.calculate_rating()
                            )
                            / 400)))
                        )
                    attacker.set_rating(
                        round(attacker.calculate_rating() + k*(1 - attacker_p))
                    )
                    defender.set_rating(
                        round(defender.calculate_rating() + k*(0 - defender_p))
                    )
                    return {
                        "winner": card,
                        "loser": cards[1 - idx],
                        "winner_rating": attacker.rating,
                        "loser_rating": defender.rating
                    }

    def get_leaderboard(self) -> list:
        card_list: list[TournamentCard] = list(self.cards.values())
        card_list.sort(key=lambda x: -x.rating)

        return card_list

    def generate_tournament_report(self) -> dict:
        tournament_report: dict[str, int | str] = {}

        tournament_report.update({"total_cards": len(self.cards)})
        tournament_report.update({"match_played": self.match_played})

        all_ratings: list[int] = [
                card.rating for card in list(self.cards.values())
            ]
        total_rating: int = sum(all_ratings)
        avg_rating: int = total_rating / max(1, len(all_ratings))

        tournament_report.update({"avg_rating": avg_rating})
        tournament_report.update({"platform_status": "active"})

        return tournament_report

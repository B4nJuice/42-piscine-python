from ex0 import Card
from ex2 import Combatable
from ex4 import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
                    self,
                    name: str,
                    cost: int,
                    rarity: str,
                    health: int,
                    attack_power: int,
                    defense_power: int,
                    rating: int = 1000
                ):
        self.set_name(name)
        self.set_rarity(rarity)
        self.set_cost(cost)
        self.set_health(health)
        self.set_attack(attack_power)
        self.set_defense(defense_power)
        self.set_rating(rating)

        self.wins: int = 0
        self.losses: int = 0

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        damage_dealt: int = max(
            target.defend(self.attack_power).get("damage_taken"), target.health
        )

        attack_result: dict[str, int | str] = {}
        attack_result.update({"attacker": self.name})
        attack_result.update({"target": target.name})
        attack_result.update({"damage_dealt": damage_dealt})

        return attack_result

    def defend(self, incoming_damage: int) -> dict:
        damage_taken: int = max(0, incoming_damage - self.defense_power)

        defense_result: dict[str, int | str] = {}
        defense_result.update({"defender": self.name})
        defense_result.update({"damage_taken": damage_taken})
        defense_result.update(
            {"damage_defended": min(incoming_damage, self.defense_power)}
        )

        return defense_result

    def get_combat_stats(self) -> dict:
        combat_stats: dict[str, int | str] = {}

        combat_stats.update({"attack": self.attack_power})
        combat_stats.update({"defense": self.defense_power})

        return combat_stats

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> dict:
        tournament_stats: dict[str, int | str] = {}

        tournament_stats.update({"name": self.name})
        tournament_stats.update({"rating": self.rating})
        tournament_stats.update({"wins": self.wins})
        tournament_stats.update({"losses": self.losses})

        return tournament_stats

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("Wins have to be a non-negative integer.")
        self.wins = wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("Losses have to be a non-negative integer.")
        self.losses = losses

    def get_rank_info(self) -> dict:
        rank_info: dict[str, int | str] = {}

        rank_info.update({"name": self.name})
        rank_info.update({"rating": self.rating})
        rank_info.update({"wins": self.wins})
        rank_info.update({"losses": self.losses})

        return rank_info

    def set_attack(self, attack_power: int) -> None:
        if not isinstance(attack_power, int) or attack_power < 0:
            raise ValueError("Attack has to be a non-negative integer.")
        self.attack_power: int = attack_power

    def set_defense(self, defense_power: int) -> None:
        if not isinstance(defense_power, int) or defense_power < 0:
            raise ValueError("Defense has to be a non-negative integer.")
        self.defense_power: int = defense_power

    def set_rating(self, rating: int) -> None:
        if not isinstance(rating, int) or rating < 0:
            raise ValueError("Rating has to be a non-negative integer.")
        self.rating: int = rating

    def set_health(self, health: int) -> None:
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health has to be a non-negative integer.")
        self.health: int = health

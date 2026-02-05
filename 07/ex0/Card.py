from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.set_name(name)
        self.set_cost(cost)
        self.set_rarity(rarity)

    def set_name(self, name: str) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError("Name cannot be empty.")
        self.name = name

    def set_rarity(self, rarity: str) -> None:
        if not isinstance(rarity, str) or rarity == "":
            raise ValueError("Rarity cannot be empty.")
        self.rarity = rarity

    def set_cost(self, cost: int) -> None:
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost has to be a non-negative integer.")
        self.cost: int = cost

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict[str, str | int]:
        card_info: dict[str, str | int] = {}

        card_info.update({"name": self.name})
        card_info.update({"cost": self.cost})
        card_info.update({"rarity": self.rarity})

        return card_info

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana

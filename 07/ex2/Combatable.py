from abc import ABC, abstractmethod
from ex0 import Card


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Card) -> dict:
        pass

    @abstractmethod
    def defend(self, incomming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass

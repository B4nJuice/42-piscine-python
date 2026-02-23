from abc import ABC, abstractmethod
from ex0 import Card


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, targets: list[Card]) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass

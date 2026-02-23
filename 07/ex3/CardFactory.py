from abc import ABC, abstractclassmethod
from ex0 import Card


class CardFactory(ABC):
    @abstractclassmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractclassmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractclassmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractclassmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractclassmethod
    def get_supported_types(self) -> dict:
        pass

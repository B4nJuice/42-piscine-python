from typing import Any
from ex0 import Card
from enum import Enum


class ArtifactEffectType(Enum):
    MANA = "mana"


class ArtifactCard(Card):
    def __init__(
                self,
                name: str,
                cost: int,
                rarity: str,
                effect_type: str,
                effect_power: int,
                durability: int
            ) -> None:
        super().__init__(name, cost, rarity)

        self.set_effect_type(effect_type)
        self.set_effect_power(effect_power)
        self.set_durability(durability)
        self.set_effect_description()

    def set_effect_type(self, effect_type: str) -> None:
        if not isinstance(effect_type, str) or effect_type == "":
            raise ValueError("Effect type cannot be empty.")

        for effect in ArtifactEffectType:
            if effect.value == effect_type:
                self.effect_type: str = effect_type
                return

        raise ValueError(
                "Effect type has to be in the ArtifactEffectType enum."
            )

    def set_effect_power(self, effect_power: int) -> None:
        if not isinstance(effect_power, int) or effect_power <= 0:
            raise ValueError("Effect power has to be a positive integer.")
        self.effect_power: int = effect_power

    def set_durability(self, durability: int) -> None:
        if not isinstance(durability, int) or (
            durability <= 0 and durability != -1
                ):
            raise ValueError("Durability has to be a non-negative integer\
(-1 mean infinite durability).")

        self.durability: int = durability
        self.base_durability: str = str(durability)
        if durability == -1:
            self.base_durability = "Permanent"

    def play(
                self,
                game_state: dict[str, Any]
            ) -> dict[str, str | int] | None:
        play_result: dict[str, str | int] = {}
        available_mana: int = game_state.get("available_mana")

        if self.is_playable(available_mana):
            play_result.update({"card_played": self.name})
            play_result.update({"mana_used": self.cost})
            play_result.update({"effect": self.effect_description})

            game_state.update({"available_mana": available_mana - self.cost})

            return play_result

        return None

    def activate_ability(
                self,
                game_state: dict[str, Any]
            ) -> dict[str, str | int]:
        artifact_result: dict[str, str | int] = {}

        durability: str | int = None

        if self.durability != -1:
            self.durability -= 1
            durability = self.durability
        else:
            durability = "Permanent"

        match self.effect_type:
            case ArtifactEffectType.MANA.value:
                available_mana: int = game_state.get("available_mana")
                game_state.update({
                        "available_mana": available_mana
                        + self.effect_power
                    })

        artifact_result.update({"card_played": self.name})
        artifact_result.update({"ability_activated": self.effect_description})
        artifact_result.update({"durability_remaining": durability})

        return artifact_result

    def set_effect_description(self) -> str:

        match self.effect_type:
            case ArtifactEffectType.MANA.value:
                self.effect_description: str = (
                    f"{self.base_durability}: +{self.effect_power}\
 mana per turn."
                )

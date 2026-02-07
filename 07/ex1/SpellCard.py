from typing import Any
from enum import Enum
from ex0 import Card, CreatureCard


class SpellEffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class NumType(Enum):
    MIN = "min"
    MAX = "max"
    EXACT = "exactly"


class SpellCard(Card):
    def __init__(
                self,
                name: str,
                cost: int,
                rarity: str,
                effect_type: str,
                effect_power: int,
                num_target: dict[str, int | NumType]
            ) -> None:
        super().__init__(name, cost, rarity)

        self.set_effect_type(effect_type)
        self.set_effect_power(effect_power)
        self.set_num_target(num_target)

    def set_effect_type(self, effect_type: str) -> None:
        if not isinstance(effect_type, str) or effect_type == "":
            raise ValueError("Effect type cannot be empty.")

        for effect in SpellEffectType:
            if effect.value == effect_type:
                self.effect_type = effect_type
                return

        raise ValueError("Effect type has to be in the SpellEffectType enum.")

    def set_effect_power(self, effect_power: int) -> None:
        if not isinstance(effect_power, int) or effect_power <= 0:
            raise ValueError("Effect power has to be a positive integer.")
        self.effect_power = effect_power

    def set_num_target(self, num_target: dict[str, int | NumType]) -> None:
        num: int = num_target.get("num")
        if not isinstance(num, int) or num <= 0:
            raise ValueError(
                "The number of targets has to be a positive integer."
            )

        num_type: NumType = num_target.get("num_type")
        if num_type not in NumType:
            raise ValueError("The num_type has to be in the NumType Enum.")

        self.num_target = num_target

    def get_effect_description(self) -> str:
        action: str = None
        unity: str = None

        match self.effect_type:
            case SpellEffectType.BUFF.value:
                action = "Buff"
                unity = "attack"

            case SpellEffectType.DEBUFF.value:
                action = "Debuff"
                unity = "attack"

            case SpellEffectType.DAMAGE.value:
                action = "Deal"
                unity = "damage"

            case SpellEffectType.HEAL.value:
                action = "Heal"
                unity = "Health points"

        num = self.num_target.get("num")
        num_type = self.num_target.get("num_type").value

        return f"{action} {self.effect_power} {unity} to targets.\
 ({num_type} {num} targets)"

    def play(
                self,
                game_state: dict[str, Any],
                targets: list[CreatureCard]
            ) -> dict[str, str | int] | None:
        play_result: dict[str, str | int] = {}
        available_mana: int = game_state.get("available_mana")

        if self.is_playable(available_mana):
            play_result.update({"card_played": self.name})
            play_result.update({"mana_used": self.cost})
            play_result.update({"effect": self.get_effect_description()})

            game_state.update({"available_mana": available_mana - self.cost})

            spell_result: dict[str, list[str]] = self.resolve_effect(targets)

            play_result.update(spell_result)

            self.consumed = True

            return play_result

        return None

    def resolve_effect(
                self,
                targets: list[CreatureCard]
            ) -> dict[str, str | int | list]:
        for target in targets:
            if not isinstance(target, CreatureCard):
                raise ValueError("Spell targets has to be creatures.")

        n_targets: int = len(targets)

        num = self.num_target.get("num")
        num_type = self.num_target.get("num_type")

        result: bool = False

        match num_type:
            case NumType.EXACT:
                result = num == n_targets

            case NumType.MIN:
                result = num <= n_targets

            case NumType.MAX:
                result = num >= n_targets

        if result is False:
            raise ValueError(f"Invalid number of targets ({num_type} {num})")

        match self.effect_type:
            case SpellEffectType.BUFF.value:
                for target in targets:
                    target.attack += self.effect_power

            case SpellEffectType.DEBUFF.value:
                for target in targets:
                    target.attack -= self.effect_power

            case SpellEffectType.HEAL.value:
                for target in targets:
                    target.health += self.effect_power

            case SpellEffectType.DAMAGE.value:
                for target in targets:
                    target.health -= self.effect_power

        spell_result: dict[str, list[str]] = {}

        spell_result.update({"card_played": self.name})
        spell_result.update({"mana_used": self.cost})
        spell_result.update({"targets": [target.name for target in targets]})

        return spell_result

    def get_card_info(self) -> dict[str, str | int]:
        card_info: dict[str, str | int] = super().get_card_info()

        card_info.update({"effect": self.get_effect_description})

        return card_info

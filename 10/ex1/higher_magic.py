from typing import Any, Callable, Union


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args: Any, **kwds: Any) -> tuple[Any, Any]:
        return spell1(*args, **kwds), spell2(*args, **kwds)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any, **kwds: Any) -> Any:
        return base_spell(*args, **kwds) * multiplier

    return amplified


def conditional_caster(
            condition: Callable,
            spell: Callable
        ) -> Union[Callable, str]:
    if condition():
        def casted(*args: Any, **kwds: Any) -> Any:
            return spell(*args, **kwds)

        return casted
    return "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args: Any, **kwds: Any) -> list[Any]:
        return [spell(*args, **kwds) for spell in spells]

    return sequence


def fireball() -> int:
    return 10


def heal_potion() -> str:
    return "Heal potion used"


def print_42() -> int:
    print("42")
    return 42


def print_heal_potion() -> str:
    print(heal_potion())
    return heal_potion()


if __name__ == "__main__":
    combined_spell: callable = spell_combiner(fireball, heal_potion)

    print("Testing spell combiner...")
    print(f"Combined spell result: {combined_spell()}")

    print()

    print("Testing power amplifier...")
    print(f"Original: {fireball()},\
 Amplified: {power_amplifier(fireball, 3)()}")

    print()

    print("Testing conditional caster...")
    print(f"True: {conditional_caster(lambda: True, heal_potion)()}")
    print(f"False: {conditional_caster(lambda: False, heal_potion)}")

    print()

    spells: list[callable] = [print_42, print_heal_potion]

    print("Testing spell sequence...")
    print(spell_sequence(spells)())

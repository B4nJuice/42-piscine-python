def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda: (spell1(), spell2())


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda: base_spell() * multiplier


def conditional_caster(condition: bool, spell: callable) -> callable:
    if condition():
        return lambda: spell()
    return "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda: [spell() for spell in spells]


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

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda: (spell1(), spell2())


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda: base_spell() * multiplier


def conditional_caster(condition: bool, spell: callable) -> callable | str:
    if condition:
        return lambda: spell()
    return "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda: [spell(i) for i, spell in enumerate(spells)]


def fireball() -> int:
    return 10


def heal_potion() -> str:
    return "Heal potion used"


if __name__ == "__main__":
    combined_spell: callable = spell_combiner(fireball, heal_potion)

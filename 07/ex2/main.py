from ex2 import EliteCard, CombatType
from ex1 import SpellCard, SpellEffectType, NumType
from ex0 import Rarity, CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Ability System ===")

    print()

    print("EliteCard capabilities:")
    for _cls in EliteCard.__bases__:
        method_list = [
            method for method in dir(_cls) if method.startswith('_') is False
        ]
        print(f"- {_cls.__name__}: {method_list}")

    print()

    print("Playing Arcane Warrio (Elite Card): ")

    print()

    enemy1: CreatureCard = CreatureCard(
            "Enemy1",
            0,
            Rarity.COMMON.value,
            5,
            1000
        )

    enemy2: CreatureCard = CreatureCard(
            "Enemy2",
            0,
            Rarity.COMMON.value,
            5,
            1000
            )

    arcane_warrior: EliteCard = EliteCard(
            "Arcane Warrior",
            1,
            Rarity.LEGENDARY.value,
            5,
            10,
            8,
            3,
            CombatType.MELEE
        )

    print("Combat phase:")

    print(f"Attack result: {arcane_warrior.attack(enemy1)}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print()

    fireball: SpellCard = SpellCard(
            "Fireball",
            4,
            Rarity.UNCOMMON.value,
            SpellEffectType.DAMAGE.value,
            3,
            {"num": 3, "num_type": NumType.MAX}
        )

    print("Magic phase:")

    print(f"Spell cast:\
{arcane_warrior.cast_spell([enemy1, enemy2], fireball)}")
    print(f"Mana Channel: {arcane_warrior.channel_mana(3)}")

    print()

    print("Multiple interface implementation successful!")

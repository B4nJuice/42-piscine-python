def mage_counter() -> callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:

    def power(power_to_add: int) -> int:
        nonlocal initial_power
        initial_power += power_to_add
        return initial_power

    return power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchant(item_name: str) -> str:
        nonlocal enchantment_type

        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    memory: dict[str, any] = {}

    def store(key: str, value: any) -> None:
        memory.update({key: value})

    def recall(key: str) -> any:
        return memory.get(key, 'Memory not found')

    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    counter: callable = mage_counter()

    print("Testing mage counter...")
    for i in range(3):
        print(f"Call {i+1}: {counter()}")

    print()

    power_adder: callable = spell_accumulator(10)

    print("Testing spell accumulator...")
    for i in range(5):
        print(f"Adding {i}: {power_adder(i)}")

    print()

    flaming_enchant: callable = enchantment_factory("Flaming")

    print("Testing enchantment factory...")
    print(f"Enchanting sword: {flaming_enchant('Sword')}")
    print(f"Enchanting bow: {flaming_enchant('Bow')}")

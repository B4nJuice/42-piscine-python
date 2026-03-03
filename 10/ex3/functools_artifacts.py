import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    real_operation: callable = operations.get(operation)

    if real_operation is None:
        raise ValueError(f"Unknown operation : {operation}")

    return functools.reduce(real_operation, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, "fire"),
        'ice_enchant': functools.partial(base_enchantment, 50, "ice"),
        'lightning_enchant': functools.partial(
            base_enchantment, 50, "lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(arg: any) -> str:
        raise NotImplementedError('Unsupported type')

    cast_spell.register(
        str,
        lambda arg: 'Enchanting ' + arg
    )
    cast_spell.register(
        int,
        lambda arg: f'Casting spell with power {arg}'
    )
    cast_spell.register(
        list,
        lambda arg: f'Combining spells : {arg}'
    )

    return cast_spell


def enchanter(power: int, element: str, target: str) -> str:
    return f"Enchanting: {target} to -> '{element} {target}' power {power} !"


if __name__ == "__main__":
    int_list: list[int] = [10, 5, 3]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(int_list, 'add')}")
    print(f"Product: {spell_reducer(int_list, 'multiply')}")
    print(f"Max: {spell_reducer(int_list, 'max')}")
    print(f"Min: {spell_reducer(int_list, 'min')}")

    print()

    print("Testing partial enchanting...")

    partial_callable: dict[str, callable] = partial_enchanter(enchanter)

    print(f"{partial_callable.get('fire_enchant')('sword')}")
    print(f"{partial_callable.get('ice_enchant')('shield')}")
    print(f"{partial_callable.get('lightning_enchant')('axe')}")

    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print()

    dispatch: callable = spell_dispatcher()

    print("Testing spell dispatcher...")

    print(f"Str dispatch: {dispatch('sword')}")
    print(f"Int dispatch: {dispatch(10)}")
    print(f"List dispatch: {dispatch(['fireball', 'lightning'])}")

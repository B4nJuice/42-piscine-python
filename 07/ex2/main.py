from ex2 import EliteCard


if __name__ == "__main__":
    print("=== DataDeck Ability System ===")

    print()

    print("EliteCard cpabilities:")
    for _cls in EliteCard.__bases__:
        method_list = [
            method for method in dir(_cls) if method.startswith('_') is False
        ]
        print(f"- {_cls.__name__}: {method_list}")

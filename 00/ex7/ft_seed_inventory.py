def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_type = None
    match unit:
        case "packets":
            unit_type = f"{quantity} packets available"
        case "grams":
            unit_type = f"{quantity} grams total"
        case "area":
            unit_type = f"covers {quantity} square meters"
    if unit_type is not None:
        print(f'{seed_type.capitalize()} seeds: {unit_type}')
    else:
        print("Unknown unit type")

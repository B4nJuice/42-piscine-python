def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result: str = validate_ingredients(ingredients)

    spell_state: str = "Error"

    if validation_result.endswith("INVALID"):
        spell_state = "recorded"
    else:
        spell_state = "rejected"

    return f"Spell {spell_state}: {spell_name} ({validation_result})"

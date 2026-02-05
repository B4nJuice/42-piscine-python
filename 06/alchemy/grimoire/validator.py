def validate_ingredients(ingredients: str) -> str:
    for element in [
                "fire",
                "water",
                "earth",
                "air"
            ]:
        if element in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

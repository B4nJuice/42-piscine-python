def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None:
        raise ValueError("plant_name cannot be None.")
    if water_level < 1 or water_level > 10:
        raise ValueError("water_level has to be between 1 and 10")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("sunlight_hours has to be between 2 and 12")
    return f"{plant_name} is perfect !"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 2, 5))
    except ValueError as error:
        print(f"Error : {error}")

# Faire des classes qui inherit de ValueError

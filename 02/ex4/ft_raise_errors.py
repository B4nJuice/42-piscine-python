#!/usr/bin/env python3

class GardenError(ValueError):
    '''
        Class for garden relative errors.
    '''
    def __init__(self, message="An undefined GardenError occured."):
        super().__init__(message)


class InvalidName(GardenError):
    '''
        Exception raised for invalid plant names.
    '''
    def __init__(self, message="plant_name cannot be empty."):
        super().__init__(message)


class WaterError(GardenError):
    '''
        Exception raised for errors related to water level.
    '''
    def __init__(self, w_level):
        if w_level > 10:
            super().__init__(f"water_level {w_level} is too high (max 10).")
        elif w_level < 1:
            super().__init__(f"water_level {w_level} is too low (min 1).")
        else:
            super().__init__("An undetermined WaterError occured.")


class SunlightError(GardenError):
    '''
        Exception raised for errors related to sunlight hours.
    '''
    def __init__(self, s_hours):
        if s_hours > 10:
            super().__init__(f"sunlight_hours {s_hours} is too high (max 12).")
        elif s_hours < 2:
            super().__init__(f"sunlight_hours {s_hours} is too low (min 2).")
        else:
            super().__init__("An undetermined SunlightError occured.")


def check_plant_health(plant_name, water_level, sunlight_hours):
    '''
        check_plant_health is a function that checks the health of a plant
        based on its name, water level, and sunlight hours. It raises
        appropriate errors if any of the parameters are invalid.
    '''
    if plant_name is None or plant_name == "":
        raise InvalidName
    if water_level < 1 or water_level > 10:
        raise WaterError(water_level)
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise SunlightError(sunlight_hours)
    return f"{plant_name} is perfect !"


def test_plant_checks():
    '''
        test_plant_checks is a function that tests the
        check_plant_health function and raises appropriate errors.
    '''
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 2, 5))
    except ValueError as error:
        print(f"Error : {error}")
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 2, 5))
    except ValueError as error:
        print(f"Error : {error}")
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 5))
    except ValueError as error:
        print(f"Error : {error}")
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 2, 0))
    except ValueError as error:
        print(f"Error : {error}")
    print("\nAll error raising tests completed!")

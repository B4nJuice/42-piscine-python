class GardenError(Exception):
    '''
        Base class for garden-related errors.
    '''
    def __init__(self, message="An undefined error occured"):
        super().__init__(message)


class PlantError(GardenError):
    '''
        Exception raised for errors related to plant.
    '''
    def __init__(self, plant):
        super().__init__(f"The {plant} is wilting!")


class WaterError(GardenError):
    '''
        Exception raised for errors related to water.
    '''
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def take_water_from_tank(amount):
    '''
        take_water_from_tank is a function that simulates taking water
        from a water tank. If the requested amount exceeds the available
        water (100 units), it raises a WaterError.
    '''
    if amount > 100:
        raise WaterError
    else:
        amount -= 100


def get_plant_status(health, plant):
    '''
        get_plant_status is a function that checks the health of a plant.
        If the health is less than or equal to 0, it raises a PlantError.
    '''
    if health <= 0:
        raise PlantError(plant)


def test_custom_errors():
    '''
        test_custom_errors is a function that tests custom garden errors.
    '''
    print("=== Custom Garden Errors===")
    try:
        print("\nTesting WaterError...")
        take_water_from_tank(150)
    except WaterError as e:
        print(f"Caught a garden error : {e}")
    try:
        print("\nTesting PlantError...")
        get_plant_status(-2, "tomato")
    except PlantError as e:
        print(f"Caught a garden error : {e}")
    try:
        print("\nTesting catching all garden errors...")
        take_water_from_tank(150)
    except WaterError as e:
        print(f"Caught a garden error : {e}")
    try:
        get_plant_status(0, "rose")
    except GardenError as e:
        print(f"Caught a garden error : {e}")
    print("\nAll custome error types work correctly!")

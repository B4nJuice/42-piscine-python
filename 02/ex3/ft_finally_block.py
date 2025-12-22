def water_plants(plant_list):
    '''
        water_plants is a function that waters a list of plants,
        handling errors and ensuring cleanup with a finally block.
    '''
    print("Opening watering system...")
    try:
        for plant in plant_list:
            print("watering " + plant)
        print("Watering completed successfully!")
    except Exception as error:
        print(f"Error: {error} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_waterubg_system():
    ''''
        test_waterubg_system is a function that tests the watering system
        with and without errors, ensuring cleanup always happens.
    '''
    print("=== Garden Watering System ===")
    good_plant_list = ["tomato", "lettuce", "carrots"]
    print("\nTesting normal watering...")
    water_plants(good_plant_list)
    bad_plant_list = ["tomato", None, "carrots"]
    print("\nTesting with error...")
    water_plants(bad_plant_list)
    print("\nCleanup always happens, even with errors!")

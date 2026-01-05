#!/usr/bin/env python3

def check_temperature(temp_str):
    '''
        check_temperature is a function that check if it parameter, temp_str
        can be converted to an int and if the resulting int is within an
        acceptable range for plant growth (0 to 40 degrees Celsius).
    '''
    max_temp = 40
    min_temp = 0
    try:
        print(f"Testing temperature: {temp_str}")
        temp_int = int(temp_str)
        if temp_int < min_temp:
            print(f"Error: {temp_int}°C is too cold for plants", end=' ')
            print(f" (min {min_temp})°C")
        elif temp_int > max_temp:
            print(f"Error: {temp_int}°C is too hot for plants", end=' ')
            print(f" (max {max_temp})°C")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    '''
        test_temperature_input is a function that tests the check_temperature
        function with various inputs to ensure it handles exceptions properly.
    '''
    print("=== Garden temperature checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")

def garden_operations():
    '''
        garden_opertations is a function that raise different errors
    '''
    int("abc")
    print(10 / 0)
    not_in_a_dict = {"test": 0, "abc": "abc"}
    print(not_in_a_dict["error"])
    open("not_a_file", 'r')


def test_error_types():
    '''
        test_error_types is a function that tests different error types
        and handles them appropriately.
    '''
    print("=== Garden Error Types ===")
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    try:
        print("\nTesting ZeroDivisionError...")
        print(10 / 0)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    try:
        print("\nTesting KeyError...")
        not_in_a_dict = {"test": 0, "abc": "abc"}
        print(not_in_a_dict["error"])
    except KeyError as error:
        print(f"Caught KeyError: {error}")
    try:
        print("\nTesting FileNotFoundError...")
        open("not_a_file", 'r')
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    try:
        print("\nTesting multiple errors together...")
        int("abc")
        not_in_a_dict = {"test": 0, "abc": "abc"}
        print(not_in_a_dict["error"])
    except (ValueError, KeyError) as error:
        print(f"Caught an error: {error} - but program continue")
    print("\nAll error types tested successfully!")

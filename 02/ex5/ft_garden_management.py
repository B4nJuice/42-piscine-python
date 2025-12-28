class GardenError(Exception):
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


class InvalidInt(GardenError):
    '''
        Exception raised for invalid int.
    '''
    def __init__(self, message="An undefined InvalidInt error occured."):
        super().__init__(message)


class WaterError(GardenError):
    '''
        Exception raised for water related errors.
    '''
    def __init__(self, message="An undefined WaterError error occured."):
        super().__init__(message)


def is_a_valid_int(n):
    if n is None or int(n) != n:
        return False
    return True


class Plant:
    def __init__(self, name, height, age):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def set_name(self, name):
        if name is None or name == "":
            raise InvalidName
        self.__name = name.capitalize()

    def get_name(self):
        return (self.__name)

    def set_height(self, height):
        if is_a_valid_int(height) is False:
            raise InvalidInt("height has to be a valid int.")
        self.__height = height

    def get_height(self):
        return (self.__height)

    def set_age(self, age):
        if is_a_valid_int(age) is False:
            raise InvalidInt("age has to be a valid int.")
        self.__age = age

    def get_age(self):
        return (self.__age)
    
    def set_water_level(self, water_level):
        if is_a_valid_int(water_level) is False:
            raise InvalidInt("water_level has to be a valid int")
        if water_level < 0:
            raise WaterError(f"water_level cannot be {water_level} (min 0)")
        if water_level > 100:
            raise WaterError(f"water_level cannot be {water_level} (max 100)")
        self.__water_level = water_level
    
    def get_water_level(self):
        return (self.__water_level)

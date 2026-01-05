#!/usr/bin/env python3

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


def is_a_valid_int(n) -> bool:
    '''
        check if the parameter is a valid int
    '''
    if n is None or int(n) != n:
        return False
    return True


class GardenManager:
    '''Represent a garden owned by a person and containing plants.'''
    def __init__(self, owner):
        '''Initialize a Garden for `owner` with empty plant lists.'''
        if owner is None or owner == "":
            raise GardenError("Garden Manager name error :\
owner name cannot be empty.")
        self.__owner = owner.capitalize()
        self.__plants = []
        self.__plants_num = 0

    def get_owner(self):
        '''Return the capitalized owner name.'''
        return (self.__owner)

    def get_plants(self) -> 'list':
        '''Return the internal list of plant entries (dicts).'''
        return (self.__plants)

    def get_plants_num(self) -> int:
        '''Return the number of plants added to this garden.'''
        return (self.__plants_num)

    def add_plant(self, plant) -> None:
        '''Add a plant instance to the garden under `type`.

        `plant` should be an instance of SecurePlant (or subclass).
        `type` is a string among: Tree, Vegetable, Flower.
        '''
        self.__plants.append(plant)
        self.__plants_num += 1
        name = plant.get_name()
        owner = self.get_owner()
        print(f"Added {name} to {owner}'s garden.")

    def garden_report(self):
        '''Print a detailed report about plants and counts in this garden.'''
        owner = self.get_owner()
        print(f"\n=== {owner}'s Garden Report ===\n")
        print("Plants in garden:")
        plants = self.get_plants()
        for plant in plants:
            plant.print_plant()
        print(f"\nPlants added: {self.get_plants_num()}")

    def water_all(self):
        '''
            water all plant inside the garden
        '''
        for plant in self.get_plants():
            plant_name = plant.get_name()
            try:
                water_level = plant.get_water_level()
                plant.set_water_level(water_level + 1)
                print(f"{plant_name} has been watered, water level : \
{water_level + 1}")
            except GardenError as e:
                print(f"{plant_name} : {e}")
            finally:
                print(f"water_all() executed on {plant_name} \n")

    def check_all(self):
        '''
            checks all plant inside the garden
        '''
        for plant in self.get_plants():
            plant_name = plant.get_name()
            try:
                print(plant.check_plant_health())
            except GardenError as e:
                print(f"{plant_name} : {e}")
            finally:
                print(f"check_all() executed on {plant_name} \n")


class Plant:
    def __init__(self, name, height, age, min_water, max_water):
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)
        self.set_min_max_water(min_water, max_water)
        self.set_water_level(self.get_min_water())

    def set_name(self, name):
        '''
            change the plant name
        '''
        if name is None or name == "":
            raise InvalidName
        self.__name = name.capitalize()

    def set_min_max_water(self, min_water, max_water):
        '''
            change the min and max water level
        '''
        if is_a_valid_int(min_water) is False:
            raise InvalidInt("min_water has to be a valid int.")
        if is_a_valid_int(max_water) is False:
            raise InvalidInt("max_water has to be a valid int.")
        if (min_water >= max_water):
            raise WaterError("max_water has to be greater than min_water.")
        if (min_water < 0 or max_water < 0):
            raise WaterError("min_water and max_water has to be\
a positive value.")
        self.__min_water = min_water
        self.__max_water = max_water

    def get_min_water(self):
        '''
            return the min water level
        '''
        return (self.__min_water)

    def get_max_water(self):
        '''
            return the max water level
        '''
        return (self.__max_water)

    def get_name(self):
        '''
            return the plant name
        '''
        return (self.__name)

    def set_height(self, height):
        '''
            change the plant height
        '''
        if is_a_valid_int(height) is False or height < 0:
            raise InvalidInt("height has to be a valid positive int.")
        self.__height = height

    def get_height(self):
        '''
            return the plant height
        '''
        return (self.__height)

    def set_age(self, age):
        '''
            change the plant age
        '''
        if is_a_valid_int(age) is False or age < 0:
            raise InvalidInt("age has to be a valid positive int.")
        self.__age = age

    def get_age(self):
        '''
            return the plant age
        '''
        return (self.__age)

    def set_water_level(self, water_level):
        '''
            change the plant water level
        '''
        if is_a_valid_int(water_level) is False:
            raise InvalidInt("water_level has to be a valid int")
        min_water = self.get_min_water()
        max_water = self.get_max_water()
        if water_level < min_water:
            raise WaterError(f"water_level cannot be {water_level} (min \
{min_water})")
        if water_level > max_water:
            raise WaterError(f"water_level cannot be {water_level} (max \
{max_water})")
        self.__water_level = water_level

    def get_water_level(self):
        '''
            return the plant water level
        '''
        return (self.__water_level)

    def print_plant(self) -> None:
        '''
            print_plant() is a method that display informations about a plant
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        water_level = self.get_water_level()
        print(f'{name}: {height}cm, {age} day{(age > 0) * "s"} old,\
water level : {water_level}')

    def check_plant_health(self):
        '''
            check_plant_health is a function that checks the health of a plant
            based on its name, water level, and sunlight hours. It raises
            appropriate errors if any of the parameters are invalid.
        '''
        plant_name = self.get_name()
        water_level = self.get_water_level()
        min_water = self.get_min_water()
        max_water = self.get_max_water()
        if plant_name is None or plant_name == "":
            raise InvalidName
        if water_level < min_water or water_level > max_water:
            raise WaterError(f"Watter Error : {plant_name}' water_level has to\
be between {min_water} and {max_water}, here {water_level}")
        return f"{plant_name} is perfect !"


plant_list = [
    {
        "name": "Rose",
        "height": 10,
        "age": 10,
        "min_water": 5,
        "max_water": 100
    },
    {
        "name": "Nasturtium",
        "height": 10,
        "age": 10,
        "min_water": 40,
        "max_water": 41
    },
    {
        "name": "Tulip",
        "height": -10,
        "age": 10,
        "min_water": 5,
        "max_water": 100
    },
    {
        "name": "Lys",
        "height": 10,
        "age": -10,
        "min_water": 5,
        "max_water": 100
    },
    {
        "name": "Poppy",
        "height": 10,
        "age": 10,
        "min_water": 105,
        "max_water": 100
    },
]


def tester():
    gam = GardenManager("Bob")
    for plant in plant_list:
        try:
            name = plant["name"]
            height = plant["height"]
            age = plant["age"]
            min_water = plant["min_water"]
            max_water = plant["max_water"]
            plant_instance = Plant(name, height, age, min_water, max_water)
            print(f"\nPlant {name} created.")
            gam.add_plant(plant_instance)
        except GardenError as e:
            print(f"Error on plant adding {e}")
        finally:
            print(f"GardenManager.add_plant() executed on {name}\n")
    gam.water_all()
    gam.check_all()
    gam.water_all()


tester()

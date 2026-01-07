#!/usr/bin/env python3

class SecurePlant:
    '''
        SecurePlant class is a class that contains all the informations about
        a Plant but with encapsulation to secure the modification of the
        attributes
    '''
    def __init__(self, name, age, height, grow_speed, max_height) -> None:
        self.name = name.capitalize()
        self.grow_speed = grow_speed
        self.max_height = max_height
        if self.set_age(age) is False:
            self.__age = 0
        if self.set_height(height) is False:
            self.__height = 0
        self.starting_height = self.get_height()

    def get_age(self) -> int:
        '''
            get_age() is a method that return the age of the plant
        '''
        return self.__age

    def set_age(self, age) -> bool:
        '''
            set_age() is a method that set the age of the plant with security
            (age cannot be a negative value)
        '''
        if age >= 0:
            self.__age = age
            print(f'{self.name}: Age updated: {age} day{(age > 1) * "s"} [OK]')
            return True
        else:
            print(f'{self.name}: Invalid operation : age {age} day. [KO]')
            return False

    def get_height(self) -> int:
        '''
            get_height() is a method that return the height of the plant
        '''
        return self.__height

    def set_height(self, height) -> bool:
        '''
            set_height() is a method that set the height of the plant
            with security (height cannot be a negative value or greater than
            the max height).
        '''
        if height >= 0:
            self.__height = height
            if self.__height > self.max_height:
                self.__height = self.max_height
            print(f'{self.name}: height updated: {self.__height} [OK]')
            return True
        else:
            print(f'{self.name}: Invalid operation : height {height}cm. [KO]')
            return False

    def print_plant(self) -> None:
        '''
            print_plant() is a method that display informations about a plant
        '''
        name = self.name
        age = self.get_age()
        height = self.get_height()
        print(f'{name}: {height}cm, {age} day{(age > 0) * "s"} old')


def ft_plant_factory(plant_list):
    '''
        ft_plant_factory() is a factory for the class Plant, it creates plants
        depending of attributes on the list on dict.
    '''
    created_plants = []
    print("\n=== Plant Factory Output ===\n")
    for plant in plant_list:
        name = plant["name"]
        age = plant["age"]
        height = plant["height"]
        grow_speed = plant["grow_speed"]
        max_height = plant["max_height"]
        new_plant = SecurePlant(name, age, height, grow_speed, max_height)
        created_plants.append(new_plant)
    print("\n=== Created plants ===\n")
    for plant in created_plants:
        plant.print_plant()
    return (created_plants)


def ft_garden_security():
    '''
        ft_garden_security() init the garden an display is status
    '''

    plant_list = [
        {
            "name": "Rose",
            "age": -10,
            "height": -25,
            "grow_speed": 2,
            "max_height": 80
        },
        {
            "name": "Oak",
            "age": 365,
            "height": 200,
            "grow_speed": 0,
            "max_height": 1500
        },
        {
            "name": "Cactus",
            "age": 90,
            "height": 5,
            "grow_speed": 1,
            "max_height": 30
        },
        {
            "name": "Sunflower",
            "age": 45,
            "height": 80,
            "grow_speed": 2,
            "max_height": 100
        },
        {
            "name": "Fern",
            "age": 120,
            "height": 15,
            "grow_speed": 1,
            "max_height": 50
        }
    ]

    created_plants = ft_plant_factory(plant_list)
    print("\n=== Garden Security System ===\n")
    created_plants[0].set_age(10)
    created_plants[0].set_height(100)
    created_plants[3].set_age(0)
    created_plants[4].set_age(-1)
    created_plants[4].set_height(-10)
    print("\n=== Current plants ===\n")
    for plant in created_plants:
        plant.print_plant()


if __name__ == "__main__":
    ft_garden_security()

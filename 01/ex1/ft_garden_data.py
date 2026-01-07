#!/usr/bin/env python3

class Plant:
    '''
        Plant class is a class that contains all the informations about a Plant
    '''
    def __init__(self, name, age, height):
        self.name = name.capitalize()
        self.age = age
        self.height = height

    def print_plant(self):
        '''
            print_plant() is a method that display informations about a plant
        '''
        name = self.name
        age = self.age
        height = self.height
        print(f'{name}: {height}cm ,{age} day{(age > 0) * "s"} old')


def ft_garden_data():
    '''
        ft_garden_data() display informations about your garden and the
        different plants
    '''
    plant1 = Plant("Rose", 30, 25)
    plant2 = Plant("Sunflower", 45, 80)
    plant3 = Plant("Rose", 120, 15)
    print('=== Garden Plant Registry ===')
    plant1.print_plant()
    plant2.print_plant()
    plant3.print_plant()


if __name__ == "__main__":
    ft_garden_data()

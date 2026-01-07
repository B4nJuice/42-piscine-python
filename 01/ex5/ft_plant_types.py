#!/usr/bin/env python3

class SecurePlant:
    '''
        SecurePlant class is a class that contains all the informations about
        a Plant but with encapsulation to secure the modification of the
        attributes
    '''
    def __init__(self, name, age, height, grow_speed, max_height) -> None:
        self.__name = name.capitalize()
        self.__grow_speed = grow_speed
        self.__max_height = max_height
        if self.set_age(age) is False:
            self.__age = 0
        if self.set_height(height) is False:
            self.__height = 0
        self.__starting_height = self.get_height()

    def get_name(self) -> str:
        '''
            get_name() is a method that return the name of the plant
        '''
        return (self.__name)

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
        name = self.get_name()
        if age >= 0:
            self.__age = age
            print(f'{name}: Age updated: {age} day{(age > 1) * "s"} [OK]')
            return True
        else:
            print(f'{name}: Invalid operation : age {age} day. [KO]')
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
            name = self.get_name()
            if self.__height > self.__max_height:
                self.__height = self.__max_height
            print(f'{name}: height updated: {self.__height} [OK]')
            return True
        else:
            print(f'{name}: Invalid operation : height {height}cm. [KO]')
            return False

    def print_plant(self) -> None:
        '''
            print_plant() is a method that display informations about a plant
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        print(f'{name}: {height}cm, {age} day{(age > 0) * "s"} old')


class Flower(SecurePlant):
    '''
        Flower is a class that inherit from SecurePlant and has specific
        attributes for the flower
    '''
    def __init__(self, name, age, height, grow_speed, max_height,
                 color) -> None:
        super().__init__(name, age, height, grow_speed, max_height)
        self.__color = color
        self.__bloomed = False

    def get_color(self) -> str:
        '''
            get_color() method return the flower's color
        '''
        return (self.__color)

    def bloom(self) -> None:
        '''
            bloom() method set the flower at bloomed
        '''
        if (self.__bloomed is False):
            self.__bloomed = True
            print(f'{self.get_name()} is blooming beautiffuly!')
        else:
            print(f'{self.get_name()} is already bloomed.')

    def change_color(self, color) -> None:
        '''
            change_color() method change the flower's color
        '''
        self.__color = color
        print(f'{self.get_name()} changed it color to {self.get_color}!')

    def print_flower(self) -> None:
        '''
            print_flower() is a method that display informations about a flower
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        color = self.get_color()
        print(f'{name} (Flower): {height}cm, {age}', end=' ')
        print(f'day{(age > 0) * "s"}, {color} color')

    def factory(self, name, age, height, grow_speed, max_height,
                color) -> 'Flower':
        '''
            factory() method is a factory that create an instance of a flower
        '''
        return (Flower(name, age, height, grow_speed, max_height, color))


class Tree(SecurePlant):
    '''
        Tree is a class that inherit from SecurePlant and has specific
        attributes for the tree
    '''
    def __init__(self, name, age, height, grow_speed, max_height,
                 trunk_diameter, max_trunk_diameter) -> None:
        super().__init__(name, age, height, grow_speed, max_height)
        self.__max_trunk_diameter = max_trunk_diameter
        if (trunk_diameter > max_trunk_diameter):
            self.__trunk_diameter = max_trunk_diameter
        else:
            self.__trunk_diameter = trunk_diameter

    def produce_sade(self) -> None:
        '''
            produce_shade() method produce the shade of the tree
        '''
        shade_area = self.__trunk_diameter / 10 * self.get_height() / 100
        print(f'{self.get_name()} provides {shade_area} square meter', end='')
        print(f'{(shade_area > 1) * "s"} of shade!')

    def get_trunk_diameter(self) -> int:
        '''
            get_trunk_diameter() method return the trunk diameter of the tree
        '''
        return (self.__trunk_diameter)

    def print_tree(self):
        '''
            print_tree() is a method that display informations about a tree
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        trunk_diameter = self.get_trunk_diameter()
        print(f'{name} (Tree): {height}cm, {age}', end=' ')
        print(f'day{(age > 0) * "s"}, {trunk_diameter}cm diameter')

    def factory(self, name, age, height, grow_speed, max_height,
                trunk_diameter, max_trunk_diameter) -> 'Tree':
        '''
            factory() method is a factory that create an instance of a tree
        '''
        return (Tree(name, age, height, grow_speed, max_height,
                     trunk_diameter, max_trunk_diameter))


class Vegetable(SecurePlant):
    '''
        Vegetable is a class that inherit from SecurePlant and has specific
        attributes for the vegetable
    '''
    def __init__(self, name, age, height, grow_speed, max_height,
                 harvest_season, nutritional_value) -> None:
        super().__init__(name, age, height, grow_speed, max_height)
        self.__harvest_season = harvest_season
        self.__nutritonal_value = nutritional_value

    def get_harvest_seson(self) -> str:
        '''
            get_harvest_season() method return the vegetable's harvest season
        '''
        return (self.__harvest_season)

    def get_nutritional_value(self) -> str:
        '''
            get_nutritional_value() mathod return the vegetable's nutritional
            value
        '''
        return (self.__nutritonal_value)

    def print_vegetable(self):
        '''
            print_vegetable() is a method that display informations about a
            vegetable
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        harvest_season = self.get_harvest_seson()
        print(f'{name} (Vegetable): {height}cm, {age}', end=' ')
        print(f'day{(age > 0) * "s"}, {harvest_season} harvest,', end=' ')
        print(f'rich in {self.get_nutritional_value()}')

    def factory(self, name, age, height, grow_speed, max_height,
                harvest_season, nutritional_value) -> 'Vegetable':
        '''
            factory() method is a factory that create an instance of a
            vegetable
        '''
        return (Vegetable(name, age, height, grow_speed, max_height,
                          harvest_season, nutritional_value))


def ft_plant_types():
    print("=== Garden Plant Factory ===\n")
    rose = Flower("rose", 1, 15, 1, 80, "red")
    tulip = Flower("tulip", 3, 10, 2, 60, "white")
    oak = Tree("oak", 365, 500, 1, 1500, 50, 150)
    birch = Tree("birch", 120, 250, 1, 1000, 20, 50)
    tomato = Vegetable("tomato", 90, 80, 3, 200, "summer", "vitamin C")
    spinach = Vegetable("spinach", 10, 12, 1, 20, "winter", "omega 3")
    print("\n=== Garden Plant Types ===\n")
    rose.print_flower()
    rose.bloom()
    print("")
    tulip.print_flower()
    tulip.bloom()
    tulip.bloom()
    print("")
    oak.print_tree()
    oak.produce_sade()
    print("")
    birch.print_tree()
    birch.produce_sade()
    print("")
    tomato.print_vegetable()
    print("")
    spinach.print_vegetable()


if __name__ == "__main__":
    ft_plant_types()

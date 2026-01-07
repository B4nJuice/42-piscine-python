#!/usr/bin/env python3
class GardenManager:
    '''Manager for multiple gardens and convenience helpers.'''
    def __init__(self) -> 'GardenManager':
        '''Create an empty GardenManager.'''
        self.__garden_list = []

    class GardenStats:
        '''Small report class that computes aggregate stats for gardens.'''
        def __init__(self, garden_list):
            '''Compute and print aggregate statistics for a list of gardens.

            Args:
                garden_list: iterable of Garden instances to aggregate.
            '''
            total_garden = 0
            total_score = 0
            total_plants = 0
            total_flower = 0
            total_tree = 0
            total_vegetable = 0
            for garden in garden_list:
                total_garden += 1
                total_score += garden.get_score()
                total_plants += garden.get_plants_num()
                total_flower += garden.get_plant_type("Flower")
                total_tree += garden.get_plant_type("Tree")
                total_vegetable += garden.get_plant_type("Vegetable")
            print(f"Garden managed : {total_garden}")
            print(f"Total score : {total_score}")
            print(f"Total plants : {total_plants}")
            print(f"\nTotal flower : {total_flower}")
            print(f"Total tree : {total_tree}")
            print(f"Total vegetable : {total_vegetable}")

    def create_garden(self, owner) -> 'Garden':
        '''Create a Garden for `owner`, register it and return it.'''
        garden = Garden(owner)
        self.__garden_list.append(garden)
        return (garden)

    @classmethod
    def create_garden_network(cls, garden_list) -> 'GardenManager':
        '''Create a GardenManager pre-populated with `garden_list`.'''
        manager = cls()
        for garden in garden_list:
            manager.__garden_list.append(garden)
        return manager

    def list_gardens(self):
        '''Print a short listing (index, owner, score).

        Prints one line per managed garden.
        '''
        i = 0
        for garden in self.__garden_list:
            print(f"[{i}] owner : {garden.get_owner()}", end=", ")
            print(f"score : {garden.get_score()}")
            i += 1

    def get_garden(self, index) -> 'Garden':
        '''Return the Garden at `index` in the manager's list.'''
        return (self.__garden_list[index])

    def get_stats(self):
        '''Compute and print aggregate statistics for all managed gardens.'''
        self.GardenStats(self.__garden_list)


class Garden:
    '''Represent a garden owned by a person and containing plants.'''
    def __init__(self, owner) -> 'Garden':
        '''Initialize a Garden for `owner` with empty plant lists.'''
        self.__owner = owner.capitalize()
        self.__plants = []
        self.__plants_num = 0
        self.__plants_type = {"Tree": 0, "Vegetable": 0, "Flower": 0}

    def __get_min(self) -> int:
        '''Return the minimum count among plant types.

        Checks Tree, Vegetable and Flower and returns the smallest value.
        '''
        min = self.__plants_type["Tree"]
        if self.__plants_type["Vegetable"] < min:
            min = self.__plants_type["Vegetable"]
        if self.__plants_type["Flower"] < min:
            min = self.__plants_type["Flower"]
        return (min)

    def get_score(self) -> int:
        '''Compute and return the garden score.

        The score is based on counts of plant types and bonuses for
        flowering/prize upgrades.
        '''
        score = self.__plants_type["Tree"]
        score += self.__plants_type["Vegetable"]
        score += self.__plants_type["Flower"]
        score += self.__get_min() * 5
        for plant in self.__plants:
            level = plant["plant"].__class__.__bases__[0]
            if level == FloweringPlant:
                score += 1
            elif level == PrizeFlower:
                score += 3
        return (score)

    def get_owner(self):
        '''Return the capitalized owner name.'''
        return (self.__owner)

    def get_plants(self) -> 'list':
        '''Return the internal list of plant entries (dicts).'''
        return (self.__plants)

    def get_plants_num(self) -> int:
        '''Return the number of plants added to this garden.'''
        return (self.__plants_num)

    def get_plant_type(self, type) -> int:
        '''Return the count of plants for a given type.'''
        return (self.__plants_type[type])

    def add_plant_type(self, type) -> None:
        '''Increment the internal counter for a given plant type.'''
        self.__plants_type[type] += 1

    def add_plant(self, plant, type) -> None:
        '''Add a plant instance to the garden under `type`.

        `plant` should be an instance of SecurePlant (or subclass).
        `type` is a string among: Tree, Vegetable, Flower.
        '''
        available_types = ["Tree", "Vegetable", "Flower"]
        type = type.capitalize()
        if type in available_types:
            self.__plants.append({"type": type, "plant": plant})
            self.__plants_num += 1
            self.add_plant_type(type)
            name = plant.get_name()
            owner = self.get_owner()
            print(f"Added {name} to {owner}'s garden.")
        else:
            print(f"{type} isn't an type.")

    @staticmethod
    def rebase(cls, *new_bases):
        '''Create a new class object that reuses `cls`'s dict.

        The returned type has the same name and dict but different bases.
        '''
        return type(cls.__name__, new_bases, dict(cls.__dict__))

    def upgrade_plant(self, plant):
        '''Upgrade a plant's inheritance to FloweringPlant then PrizeFlower.

        The function changes the instance's class so it gains behaviors from
        the target base classes. Existing instance attributes are preserved.
        '''
        cur_cls = plant.__class__
        if issubclass(cur_cls, SecurePlant):
            plant.__class__ = self.rebase(cur_cls, FloweringPlant)
            print(f"{plant.get_name()} has been upgraded !")
        elif issubclass(cur_cls, FloweringPlant):
            plant.__class__ = self.rebase(cur_cls, PrizeFlower)
            print(f"{plant.get_name()} has been upgraded !")

    def water_all(self):
        '''Call `upgrade_plant` for every plant in the garden.

        This simulates watering which may upgrade plants' inheritance.
        '''
        print(f"\nWatering all {self.__owner}'s garden plants...")
        for plant in self.__plants:
            self.upgrade_plant(plant["plant"])

    def garden_report(self):
        '''Print a detailed report about plants and counts in this garden.'''
        owner = self.get_owner()
        print(f"\n=== {owner}'s Garden Report ===\n")
        print("Plants in garden:")
        plants = self.get_plants()
        for plant in plants:
            print(" - ", end='')
            if plant["type"] == "Tree":
                plant["plant"].print_tree()
            elif plant["type"] == "Vegetable":
                plant["plant"].print_vegetable()
            elif plant["type"] == "Flower":
                plant["plant"].print_flower()
        print(f"\nPlants added: {self.get_plants_num()}")
        flower = self.__plants_type["Flower"]
        tree = self.__plants_type["Tree"]
        vegetable = self.__plants_type["Vegetable"]
        print(f"Plant types: {flower} Flower,", end=' ')
        print(f"{tree} Tree,", end=' ')
        print(f"{vegetable} Vegetable")
        print(f"Score : {self.get_score()}")


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
        if age >= 0:
            self.__age = age
            return True
        else:
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
            if self.__height > self.__max_height:
                self.__height = self.__max_height
            return True
        else:
            return False

    def print_plant(self) -> None:
        '''
            print_plant() is a method that display informations about a plant
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        print(f'{name}: {height}cm, {age} day{(age > 0) * "s"} old')
        print(self.__class__.__name__)

    def get_level(self):
        '''Return the immediate base class name used to determine "level".'''
        return (self.__class__.__bases__[0].__name__)


class FloweringPlant(SecurePlant):
    '''Marker class that represents a plant that can flower.

    This class inherits from SecurePlant and may be used as a base when
    upgrading plain SecurePlant instances.
    '''
    def __init__(self, name, age, height, grow_speed, max_height) -> None:
        '''Initialize a FloweringPlant; delegates to SecurePlant init.'''
        self.__grow_speed = grow_speed
        self.__max_height = max_height
        if self.set_age(age) is False:
            self.__age = 0
        if self.set_height(height) is False:
            self.__height = 0
        self.__starting_height = self.get_height()
        super().__init__(name, age, height, grow_speed, max_height)


class PrizeFlower(FloweringPlant):
    '''Marker class that represents a prize-level flowering plant.

    Instances of this class are considered upgraded beyond FloweringPlant.
    '''
    def __init__(self, name, age, height, grow_speed, max_height) -> None:
        '''Initialize a PrizeFlower; delegates to FloweringPlant init.'''
        self.__name = name.capitalize()
        self.__grow_speed = grow_speed
        self.__max_height = max_height
        if self.set_age(age) is False:
            self.__age = 0
        if self.set_height(height) is False:
            self.__height = 0
        self.__starting_height = self.get_height()
        super().__init__(name, age, height, grow_speed, max_height)


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
        print(f'{self.get_name()} changed it color to {self.get_color()}!')

    def print_flower(self) -> None:
        '''
            print_flower() is a method that display informations about a flower
        '''
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()
        color = self.get_color()
        print(f'{name} (Flower {self.get_level()}): {height}cm, {age}', end='')
        print(f' day{(age > 0) * "s"}, {color} color')

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
        print(f'{name} (Tree {self.get_level()}): {height}cm, {age}', end=' ')
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
        print(f'{name} (Vegetable {self.get_level()}): \
{height}cm, {age}', end=' ')
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


def tester():
    '''
        tester() is a function that test the garden manager with gardens and
        plants
    '''
    garden_list = [Garden("Bob"), Garden("Alice")]
    gman = GardenManager().create_garden_network(garden_list)

    f1 = Flower("rose", 1, 10, 5, 50, "red")
    t1 = Tree("oak", 5, 100, 2, 500, 30, 100)
    v1 = Vegetable("carrot", 0, 5, 10, 30, "Summer", "vitamin A")

    bob = gman.get_garden(0)
    alice = gman.get_garden(1)
    bob.add_plant(f1, "Flower")
    bob.add_plant(t1, "Tree")
    alice.add_plant(v1, "Vegetable")

    bob.garden_report()
    alice.garden_report()

    bob.water_all()
    alice.water_all()

    bob.garden_report()
    alice.garden_report()
    print()
    gman.get_stats()

    print("\n-- Plant actions --")
    for garden in (bob, alice):
        for entry in garden.get_plants():
            p = entry["plant"]
            name = p.get_name()
            print(f"\nActions for {name} (class: {p.__class__.__name__})")
            if hasattr(p, 'bloom'):
                try:
                    p.bloom()
                except Exception as e:
                    print("bloom() raised:", e)
            if hasattr(p, 'change_color'):
                try:
                    p.change_color('blue')
                except Exception as e:
                    print("change_color() raised:", e)
            if hasattr(p, 'produce_sade'):
                try:
                    p.produce_sade()
                except Exception as e:
                    print("produce_sade() raised:", e)


if __name__ == "__main__":
    tester()

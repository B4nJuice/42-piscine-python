#! python3

class Plant:
    def __init__(self, name, days_old, height, grow_speed, max_height) -> None:
        self.name = name
        self.days_old = days_old
        self.height = height
        self.starting_height = height
        self.grow_speed = grow_speed
        self.max_height = max_height

    def print_plant(self) -> None:
        name = self.name
        age = self.days_old
        height = self.height
        print(f'{name}: {height}cm ,{age} day{(age > 0) * "s"} old')


def ft_plant_factory(plant_list):
    created_plants = []
    for plant in plant_list:
        name = plant["name"]
        age = plant["age"]
        height = plant["height"]
        grow_speed = plant["grow_speed"]
        max_height = plant["max_height"]
        new_plant = Plant(name, age, height, grow_speed, max_height)
        created_plants.append(new_plant)
    print("=== Plant Factory Output ===")
    print("Created plants :")
    for plant in created_plants:
        plant.print_plant()
    return (created_plants)


plant_list = [
    {
        "name": "Rose",
        "age": 30,
        "height": 25,
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

ft_plant_factory(plant_list)

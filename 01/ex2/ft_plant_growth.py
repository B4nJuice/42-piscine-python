#! python3

class Plant:
    def __init__(self, name, days_old, height, grow_speed, max_height) -> None:
        self.name = name
        self.days_old = days_old
        self.height = height
        self.starting_height = height
        self.grow_speed = grow_speed
        self.max_height = max_height

    def grow(self, days) -> None:
        for i in range(days):
            self.height += self.grow_speed
            if (self.height >= self.max_height):
                self.height = self.max_height
                return ()

    def age(self, days) -> None:
        self.days_old += days

    def print_plant(self) -> None:
        name = self.name
        age = self.days_old
        height = self.height
        print(f'{name}: {height}cm, {age} day{(age > 0) * "s"} old')

    def get_info(self) -> int:
        return (self.height - self.starting_height)


def create_garden():
    plant1 = Plant("Rose", 0, 1, 5, 80)
    week_lenght = 7
    day = 0
    print(f'=== Day {day} ===')
    plant1.print_plant()
    day += week_lenght
    plant1.grow(week_lenght)
    plant1.age(week_lenght)
    print(f'=== Day {day} ===')
    plant1.print_plant()
    print(f'Growth this week: +{plant1.get_info()}cm')


create_garden()

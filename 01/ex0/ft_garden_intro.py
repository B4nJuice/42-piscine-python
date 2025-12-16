def ft_garden_intro():
    plant = "Rose"
    height = 25
    age = 30
    print('=== Welcome to My Garden ===\n')
    print(f'Plant: {plant}')
    print(f'Height: {height}cm')
    print(f'Age: {age} day{(age > 1) * "s"}\n')


if __name__ == "__main__":
    ft_garden_intro()
    print('\n=== End of Program ===')

def ft_count_harvest_recursive(harvesting_day=None, current_day=None):
    if harvesting_day is not None:
        if current_day < harvesting_day:
            print(f'Day {current_day + 1}')
            ft_count_harvest_recursive(harvesting_day, current_day + 1)
        else:
            print("Harvest time!")
    else:
        ft_count_harvest_recursive(int(input("Days until harvest: ")), 0)

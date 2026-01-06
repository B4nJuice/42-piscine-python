#!/usr/bin/env python3

class Item:
    def __init__(self, name, type, rarity, value, quantity):
        self.item = dict(name=name, type=type, rarity=rarity, value=value,
                         quantity=quantity)

    def set_quantity(self, quantity):
        self.item.update({"quantity": quantity})

    def get_name(self):
        return (self.item["name"])

    def get_type(self):
        return (self.item["type"])

    def get_rarity(self):
        return (self.item["rarity"])

    def get_value(self):
        return (self.item["value"])

    def get_quantity(self):
        return (self.item["quantity"])


class Player:
    def __init__(self, name):
        self.__name = name
        self.__inventory = {
            "items": []
        }

    def get_name(self):
        return (self.__name)

    def get_inventory(self):
        return (self.__inventory)

    def get_items(self):
        inventory = self.get_inventory()
        return (inventory["items"])

    def add_item(self, item):
        items = self.get_items()

        for inventory_item in items:
            if inventory_item.get_name() == item.get_name():
                new_quantiy = item.get_quantity()+inventory_item.get_quantity()
                item.set_quantity(new_quantiy)
                return

        items.append(item)

    def get_inventory_value(self):
        items = self.get_items()
        total_value = 0

        for item in items:
            value = item.get_value()
            quantity = item.get_quantity()
            total_value += value*quantity

        return (total_value)

    def print_item(self, item):
        name = item.get_name()
        type = item.get_type()
        rarity = item.get_rarity()
        quantity = item.get_quantity()
        value = item.get_value()
        total_value = value * quantity

        print(f"{name} ({type}, {rarity}): {quantity}x @ {value} gold each\
 = {total_value} gold.")

    def print_inventory(self):
        player_name = self.get_name()
        print(f"=== {player_name}'s Inventory ===")

        items = self.get_items()
        item_count = 0

        categories = {}
        categories_keys = categories.keys()

        for item in items:
            quantity = item.get_quantity()
            item_count += quantity

            type = item.get_type()
            type_count = 0
            if type in categories_keys:
                type_count = categories[type]
            type_count += quantity
            categories.update({type: type_count})

            self.print_item(item)

        inventory_value = self.get_inventory_value()
        print(f"\nInventory value: {inventory_value} gold")

        print(f"Item count: {item_count}")

        print("Categories:", end=" ")
        for key in categories_keys:
            print(f"{key}({categories[key]}),", end=" ")
        print()


test = Player("Test")

sword = Item("Sword", "weapon", "rare", 500, 1)
potion = Item("Potion", "consumable", "common", 50, 5)
shield = Item("Shield", "armor", "uncommon", 200, 1)

test.add_item(sword)
test.add_item(potion)
test.add_item(shield)

test.print_inventory()

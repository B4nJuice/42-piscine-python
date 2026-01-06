#!/usr/bin/env python3

class Item:
    def __init__(self, name, type, rarity, value, quantity):
        self.item = dict(name=name, type=type, rarity=rarity, value=value,
                         quantity=quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            quantity = 0
        self.item.update({"quantity": quantity})

    def add_quantity(self, quantity):
        cur_quantity = self.get_quantity()
        new_quantity = cur_quantity + quantity
        if new_quantity < 0:
            new_quantity = 0

        self.set_quantity(new_quantity)

        quantity_added = new_quantity-cur_quantity
        return (quantity_added)

    def remove_quantity(self, quantity):
        return (-self.add_quantity(-quantity))

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

    def copy_item(self):
        name = self.get_name()
        type = self.get_type()
        rarity = self.get_rarity()
        value = self.get_value()

        new_item = Item(name, type, rarity, value, 1)
        return new_item


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
        print(f"\n=== {player_name}'s Inventory ===")

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

    def get_item_in_inventory(self, name):
        items = self.get_items()

        for item in items:
            item_name = item.get_name()
            if item_name == name:
                return (item)
        return None

    def give(self, player, item_name, quantity):
        item = self.get_item_in_inventory(item_name)

        print(f"\n=== Transaction: {self.get_name()} gives {player.get_name()}\
 {quantity} {item_name} ===")

        if item is not None:
            quantity = item.remove_quantity(quantity)
            item_copy = item.copy_item()
            item_copy.set_quantity(quantity)
            player.add_item(item_copy)
            print("Transaction successful!")
        else:
            print("Transaction failed.")


alice = Player("Alice")
bob = Player("Bob")

sword = Item("Sword", "weapon", "rare", 500, 1)
potion = Item("Potion", "consumable", "common", 50, 5)
shield = Item("Shield", "armor", "uncommon", 200, 1)

alice.add_item(sword)
alice.add_item(potion)
alice.add_item(shield)

alice.print_inventory()
bob.print_inventory()

alice.give(bob, "Potion", 2)

alice.print_inventory()
bob.print_inventory()

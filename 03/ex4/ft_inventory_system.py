#!/usr/bin/env python3

class Item:
    '''
    Represents an item with a name, type, rarity, value, and quantity.
    '''
    def __init__(self, name, type, rarity, value, quantity):
        self.item = dict(name=name, type=type, rarity=rarity, value=value,
                         quantity=quantity)

    def set_quantity(self, quantity):
        '''
        Sets the quantity of the item. If quantity is negative, sets it to 0.
        '''
        if quantity < 0:
            quantity = 0
        self.item.update({"quantity": quantity})

    def add_quantity(self, quantity):
        '''
        Adds the specified quantity to the current quantity of the item.
        If the resulting quantity is negative, sets it to 0.
        '''
        cur_quantity = self.get_quantity()
        new_quantity = cur_quantity + quantity
        if new_quantity < 0:
            new_quantity = 0

        self.set_quantity(new_quantity)

        quantity_added = new_quantity - cur_quantity
        return quantity_added

    def remove_quantity(self, quantity):
        '''
        Removes the specified quantity from the current quantity of the item.
        If the resulting quantity is negative, sets it to 0.
        '''
        return -self.add_quantity(-quantity)

    def get_name(self):
        '''
        Returns the name of the item.
        '''
        return self.item.get("name")

    def get_type(self):
        '''
        Returns the type of the item.
        '''
        return self.item.get("type")

    def get_rarity(self):
        '''
        Returns the rarity of the item.
        '''
        return self.item.get("rarity")

    def get_value(self):
        '''
        Returns the value of the item.
        '''
        return self.item.get("value")

    def get_quantity(self):
        '''
        Returns the quantity of the item.
        '''
        return self.item.get("quantity")

    def copy_item(self):
        '''
        Returns a copy of the item with quantity set to 1.
        '''
        name = self.get_name()
        type = self.get_type()
        rarity = self.get_rarity()
        value = self.get_value()

        new_item = Item(name, type, rarity, value, 1)
        return new_item


class Player:
    '''
    Represents a player with a name and an inventory of items.
    '''
    def __init__(self, name):
        self.__name = name
        self.__inventory = {
            "items": []
        }

    def get_name(self):
        '''
        Returns the name of the player.
        '''
        return self.__name

    def get_inventory(self):
        '''
        Returns the inventory of the player.
        '''
        return self.__inventory

    def get_items(self):
        '''
        Returns the list of items in the player's inventory.
        '''
        inventory = self.get_inventory()
        return inventory.get("items")

    def add_item(self, item):
        '''
        Adds an item to the player's inventory. If the item already exists,
        updates the quantity.
        '''
        items = self.get_items()

        for inventory_item in items:
            if inventory_item.get_name() == item.get_name():
                new_quantity = item.get_quantity()\
                    + inventory_item.get_quantity()
                item.set_quantity(new_quantity)
                return

        items.append(item)

    def get_inventory_value(self):
        '''
        Returns the total value of all items in the player's inventory.
        '''
        items = self.get_items()
        total_value = 0

        for item in items:
            value = item.get_value()
            quantity = item.get_quantity()
            total_value += value * quantity

        return total_value

    def get_item_count(self):
        '''
        Returns the total number of items in the player's inventory.
        '''
        items = self.get_items()
        item_count = 0

        for item in items:
            quantity = item.get_quantity()
            item_count += quantity

        return item_count

    def print_item(self, item):
        '''
        Prints the details of a single item.
        '''
        name = item.get_name()
        type = item.get_type()
        rarity = item.get_rarity()
        quantity = item.get_quantity()
        value = item.get_value()
        total_value = value * quantity

        print(f"{name} ({type}, {rarity}): {quantity}x @ {value} gold each\
 = {total_value} gold.")

    def print_inventory(self):
        '''
        Prints the details of all items in the player's inventory.
        '''
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
            type_count = categories.get(type, 0)
            type_count += quantity
            categories.update({type: type_count})

            self.print_item(item)

        inventory_value = self.get_inventory_value()
        print(f"\nInventory value: {inventory_value} gold")

        print(f"Item count: {item_count}")

        print("Categories:", end=" ")
        for key in categories_keys:
            print(f"{key}({categories.get(key)}),", end=" ")
        print()

    def get_item_in_inventory(self, name):
        '''
        Returns the item with the specified name from the player's inventory.
        If the item is not found, returns None.
        '''
        items = self.get_items()

        for item in items:
            item_name = item.get_name()
            if item_name == name:
                return item
        return None

    def give(self, player, item_name, quantity):
        '''
        Gives the specified quantity of the item with the specified name to
        another player.
        '''
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

    def get_items_name_by_rarity(self, rarity):
        '''
        Returns a list of items in the player's inventory that match
        the specified rarity.
        '''
        items = self.get_items()

        matched_items = []

        for item in items:
            item_rarity = item.get_rarity()
            if item_rarity == rarity:
                item_name = item.get_name()
                matched_items.append(item_name)

        return matched_items

    def get_least_abundant_item(self) -> tuple[str, int]:
        items = self.get_items()

        searched_item = None

        for item in items:
            if searched_item is None\
                    or searched_item.get_quantity() > item.get_quantity():
                searched_item = item
        return (searched_item.get_name(), searched_item.get_quantity())

    def get_most_abundant_item(self) -> tuple[str, int]:
        items = self.get_items()

        searched_item = None

        for item in items:
            if searched_item is None\
                    or searched_item.get_quantity() < item.get_quantity():
                searched_item = item
        return (searched_item.get_name(), searched_item.get_quantity())


def ft_inventory_system():
    '''
    Demonstrates the inventory system with two players and some items.
    '''
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

    print("\n=== Inventory Analytics ===\n")

    mv_player = None
    mi_player = None

    mv_player_value = None
    mi_player_count = None

    for player in (alice, bob):
        inventory_value = player.get_inventory_value()
        item_count = player.get_item_count()

        if mv_player is None or mv_player_value < inventory_value:
            mv_player = player
            mv_player_value = inventory_value

        if mi_player is None or mi_player_count < item_count:
            mi_player = player
            mi_player_count = item_count

    mv_player_name = mv_player.get_name()

    print(f"Most valuable player: {mv_player_name} ({mv_player_value} gold)")

    mi_player_name = mi_player.get_name()

    print(f"Most items: {mi_player_name} ({mi_player_count} items)")

    rare_items = []

    for player in (alice, bob):
        player_rare_items = player.get_items_name_by_rarity("rare")
        for item in player_rare_items:
            rare_items.append(item)

    print(f"Rare items: {','.join(rare_items)}")

    print("\n=== Alice's inventory statistics ===\n")
    least_name, least_quantity = alice.get_least_abundant_item()
    print(f"Least abundant: {least_name} ({least_quantity} unit\
{'s'*(least_quantity > 1)})")
    most_name, most_quantity = alice.get_most_abundant_item()
    print(f"Most abundant: {most_name} ({most_quantity} unit\
{'s'*(most_quantity > 1)})")

    print("\n=== Dictionary Properties Demo ===\n")
    bob_items = bob.get_items()

    for item in bob_items:
        item_keys = item.item.keys()
        item_values = item.item.values()
        print(f"Dictionnary keys: {item_keys}")
        print(f"Dictionnary values: {item_values}")

    print(f"Sample lookup : - 'Potion' in inventory : \
{bob.get_item_in_inventory('Potion') is not None}")

    print(f"Sample lookup : - 'Sword' in inventory : \
{bob.get_item_in_inventory('Sword') is not None}")


if __name__ == "__main__":
    ft_inventory_system()

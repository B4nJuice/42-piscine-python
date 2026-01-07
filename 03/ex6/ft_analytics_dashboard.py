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

        quantity_added = new_quantity-cur_quantity
        return (quantity_added)

    def remove_quantity(self, quantity):
        '''
        Removes the specified quantity from the current quantity of the item.
        If the resulting quantity is negative, sets it to 0.
        '''
        return (-self.add_quantity(-quantity))

    def get_name(self):
        '''
        Returns the name of the item.
        '''
        return (self.item["name"])

    def get_type(self):
        '''
        Returns the type of the item.
        '''
        return (self.item["type"])

    def get_rarity(self):
        '''
        Returns the rarity of the item.
        '''
        return (self.item["rarity"])

    def get_value(self):
        '''
        Returns the value of the item.
        '''
        return (self.item["value"])

    def get_quantity(self):
        '''
        Returns the quantity of the item.
        '''
        return (self.item["quantity"])

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
    def __init__(self, name, score=0, achievements=[]):
        self.__name = name
        self.__inventory = {
            "items": []
        }
        self.__score = score
        self.__achievements = set(achievements)

    def get_name(self):
        '''
        Returns the name of the player.
        '''
        return (self.__name)

    def get_inventory(self):
        '''
        Returns the inventory of the player.
        '''
        return (self.__inventory)

    def get_score(self):
        '''
            return the player score
        '''
        return (self.__score)

    def set_score(self, score):
        '''
            set the player score
        '''
        self.__score = score

    def get_achievements(self):
        return (self.__achievements)

    def get_items(self):
        '''
        Returns the list of items in the player's inventory.
        '''
        inventory = self.get_inventory()
        return (inventory["items"])

    def add_item(self, item):
        '''
        Adds an item to the player's inventory. If the item already exists,
        updates the quantity.
        '''
        items = self.get_items()

        for inventory_item in items:
            if inventory_item.get_name() == item.get_name():
                new_quantiy = item.get_quantity()+inventory_item.get_quantity()
                item.set_quantity(new_quantiy)
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
            total_value += value*quantity

        return (total_value)

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
        '''
        Returns the item with the specified name from the player's inventory.
        If the item is not found, returns None.
        '''
        items = self.get_items()

        for item in items:
            item_name = item.get_name()
            if item_name == name:
                return (item)
        return None

    def give(self, player, item_name, quantity):
        '''
        Gives the specified quantity of the item with the specified name to
        another player. If the item is not found in the inventory, or if the
        quantity to give is greater than the quantity in the inventory, the
        transaction fails.
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

    def add_achievement(self, achievement):
        achievements = self.get_achievements()

        if achievement not in achievements:
            achievements.add(achievement)

    def print_achievements(self):
        '''
            print_achievements is a method that prints the player's name
            and their achievements.
        '''
        name = self.name
        achievements = self.get_achievements()
        print(f"Player {name} achievements : {achievements}")


def is_rare_achievement(achievement, achievement_player, player_list):
    '''
        is_rare_achievement is a function that checks if an achievement
        is rare (i.e., obtained by only one player) among a list of players.
    '''
    for player in player_list:
        if player != achievement_player:
            player_achievements = player.get_achievements()
            if achievement in player_achievements:
                return False
        return True


def ft_analytics_dashboard():
    bob = Player("Bob")
    alice = Player("Alice")

    bob.set_score(10)
    alice.set_score(500)

    player_list = [bob, alice]

    print("\n=== List Comprehension Examples ===\n")

    player_score_list = []

    for player in player_list:
        player_score = player.get_score()
        player_score_list.append(player_score)

    print(f"Players score: {player_score_list}")

    player_name_list = []

    for player in player_list:
        player_name = player.get_name()
        player_name_list.append(player_name)

    print(f"Active players: {player_name_list}")

    sword = Item("Sword", "weapon", "rare", 500, 1)
    potion = Item("Potion", "consumable", "common", 50, 5)
    shield = Item("Shield", "armor", "uncommon", 200, 1)

    bob.add_item(sword)
    bob.add_item(potion)
    bob.add_item(shield)

    print("\n=== Dict Comprehension Examples ===\n")

    bob_items = bob.get_items()

    print("Raw items in inventory:\n")

    for item in bob_items:
        print(item.item)

    scores_dict = {}

    for player in player_list:
        player_name = player.get_name()
        player_score = player.get_score()
        scores_dict.update({player_name: player_score})

    print("\nPlayers score:\n")
    print(scores_dict)

    print("\n=== Set Comprehension Examples ===\n")

    player_set = set([])

    for player in player_list:
        player_name = player.get_name()
        player_set.add(player_name)

    print(f"Unique players: {player_set}")

    bob.add_achievement("first_kill")
    bob.add_achievement("enemy_slayer")

    alice.add_achievement("first_kill")
    alice.add_achievement("perfectionist")

    achievement_set = set([])

    for player in player_list:
        player_achievements = player.get_achievements()
        for achievement in player_achievements:
            achievement_set.add(achievement)

    print(f"Unique achievements: {achievement_set}")

    print("\n=== Combined analysis ===\n")

    total_players = len(player_list)
    total_unique_achievements = len(achievement_set)
    total_score = sum(player_score_list)
    average_score = total_score / total_players

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Total players: {average_score}")


if __name__ == "__main__":
    ft_analytics_dashboard()

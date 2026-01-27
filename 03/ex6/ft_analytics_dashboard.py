#!/usr/bin/env python3

class Item:
    '''
    Represents an item with a name, type, rarity, value, and quantity.
    '''
    def __init__(self,
                 name: str,
                 type: str,
                 rarity: str,
                 value: int,
                 quantity: int) -> None:
        self.item = dict(name=name, type=type, rarity=rarity, value=value,
                         quantity=quantity)

    def set_quantity(self, quantity: int) -> None:
        '''
        sets the quantity of the item. If quantity is negative, sets it to 0.
        '''
        if quantity < 0:
            quantity = 0
        self.item.update({"quantity": quantity})

    def add_quantity(self, quantity: int) -> int:
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

    def remove_quantity(self, quantity: int) -> int:
        '''
        Removes the specified quantity from the current quantity of the item.
        If the resulting quantity is negative, sets it to 0.
        '''
        return (-self.add_quantity(-quantity))

    def get_name(self) -> str:
        '''
        Returns the name of the item.
        '''
        return (self.item.get("name"))

    def get_type(self) -> str:
        '''
        Returns the type of the item.
        '''
        return (self.item.get("type"))

    def get_rarity(self) -> str:
        '''
        Returns the rarity of the item.
        '''
        return (self.item.get("rarity"))

    def get_value(self) -> int:
        '''
        Returns the value of the item.
        '''
        return (self.item.get("value"))

    def get_quantity(self) -> int:
        '''
        Returns the quantity of the item.
        '''
        return (self.item.get("quantity"))

    def copy_item(self) -> "Item":
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
    def __init__(self,
                 name: str,
                 score: int = 0,
                 achievements: list[str] = []) -> None:
        self.__name = name
        self.__inventory = {
            "items": []
        }
        self.__score = score
        self.__achievements = set(achievements)

    def get_name(self) -> str:
        '''
        Returns the name of the player.
        '''
        return (self.__name)

    def get_inventory(self) -> dict:
        '''
        Returns the inventory of the player.
        '''
        return (self.__inventory)

    def get_score(self) -> int:
        '''
            return the player score
        '''
        return (self.__score)

    def set_score(self, score: int) -> None:
        '''
            set the player score
        '''
        self.__score = score

    def get_achievements(self) -> set[str]:
        return (self.__achievements)

    def get_items(self) -> list[Item]:
        '''
        Returns the list of items in the player's inventory.
        '''
        inventory = self.get_inventory()
        # use .get to avoid KeyError if structure changes
        return (inventory.get("items", []))

    def add_item(self, item: Item) -> None:
        '''
        Adds an item to the player's inventory. If the item already exists,
        updates the quantity.
        '''
        items = self.get_items()

        for inventory_item in items:
            if inventory_item.get_name() == item.get_name():
                new_quantity = item.get_quantity() + \
                    inventory_item.get_quantity()
                item.set_quantity(new_quantity)
                return

        items.append(item)

    def get_inventory_value(self) -> int:
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

    def print_item(self, item: Item) -> None:
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

    def print_inventory(self) -> None:
        '''
        Prints the details of all items in the player's inventory.
        '''
        player_name = self.get_name()
        print(f"\n=== {player_name}'s Inventory ===")

        items = self.get_items()
        item_count = 0

        categories: dict[str, int] = {}
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

    def get_item_in_inventory(self, name: str) -> Item:
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

    def give(self, player: "Player", item_name: str, quantity: int) -> None:
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

    def add_achievement(self, achievement: str) -> None:
        achievements = self.get_achievements()

        if achievement not in achievements:
            achievements.add(achievement)

    def print_achievements(self) -> None:
        '''
            print_achievements is a method that prints the player's name
            and their achievements.
        '''
        name = self.get_name()
        achievements = self.get_achievements()
        print(f"Player {name} achievements : {achievements}")


def ft_analytics_dashboard() -> None:
    bob = Player("Bob")
    alice = Player("Alice")

    bob.set_score(10)
    alice.set_score(500)

    player_list = [bob, alice]

    print("\n=== list Comprehension Examples ===\n")

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

    print("\n=== dict Comprehension Examples ===\n")

    bob_items = bob.get_items()

    print("Raw items in inventory:\n")

    for item in bob_items:
        print(item.item)

    scores_dict: dict[str, int] = {}

    for player in player_list:
        player_name = player.get_name()
        player_score = player.get_score()
        scores_dict.update({player_name: player_score})

    print("\nPlayers score:\n")
    print(scores_dict)

    print("\n=== set Comprehension Examples ===\n")

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
    top_performer = sorted(player_list, reverse=True, key=Player.get_score)[0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_performer.get_name()}\
 ({top_performer.get_score()} points, {len(top_performer.get_achievements())})"
         )


if __name__ == "__main__":
    ft_analytics_dashboard()

#!/usr/bin/env python3

class Player:
    def __init__(self, name, achievements):
        self.name = name
        self.achievements = set(achievements)

    def print_achievements(self):
        '''
            print_achievements is a method that prints the player's name
            and their achievements.
        '''
        name = self.name
        achievements = self.achievements
        print(f"Player {name} achievements : {achievements}")

    @staticmethod
    def compare_achievements(player1, player2):
        '''
            (outdated)
            compare_achievements is a static method that compares the
            achievements of two players and prints their common and
            unique achievements.
        '''
        common_achievements = []
        player1_unique_achievements = []
        player2_unique_achievements = []

        for achievement in player1.achievements:
            if achievement in player2.achievements:
                common_achievements.append(achievement)
            else:
                player1_unique_achievements.append(achievement)

        for achievement in player2.achievements:
            if achievement in player1.achievements:
                common_achievements.append(achievement)
            else:
                player2_unique_achievements.append(achievement)

        common_achievements = set(common_achievements)
        player1_unique_achievements = set(player1_unique_achievements)
        player2_unique_achievements = set(player2_unique_achievements)

        print(f"{player1.name} vs {player2.name} common: \
{common_achievements}")
        print(f"{player1.name} unique: {player1_unique_achievements}")
        print(f"{player2.name} unique: {player2_unique_achievements}")


def is_rare_achievement(achievement, achievement_player, player_list):
    '''
        is_rare_achievement is a function that checks if an achievement
        is rare (i.e., obtained by only one player) among a list of players.
    '''
    for player in player_list:
        if player != achievement_player:
            if achievement in player.achievements:
                return False
    return True


def ft_achievement_tracker():
    '''
        ft_achievement_tracker is a function that creates players with
        achievements, prints their achievements, and performs analytics
        on the achievements.
    '''
    alice_achievements = ['first_kill', 'level_10', 'treasure_hunter',
                          'speed_demon']
    bob_achievements = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    charlie_achievements = ['level_10', 'treasure_hunter', 'boss_slayer',
                            'speed_demon', 'perfectionist']

    alice = Player("Alice", alice_achievements)
    bob = Player("Bob", bob_achievements)
    charlie = Player("Charlie", charlie_achievements)

    print("=== Achievements Tracker System ===\n")

    alice.print_achievements()
    charlie.print_achievements()
    bob.print_achievements()

    print("\n=== Achievements Analytics ===\n")

    all_achievements = []
    player_list = (alice, bob, charlie)

    for player in player_list:
        for achievement in player.achievements:
            all_achievements.append(achievement)

    all_achievements = set(all_achievements)
    n_all_achievements = len(all_achievements)

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {n_all_achievements}\n")

    common_to_all = alice.achievements.intersection(bob.achievements,
                                                    charlie.achievements)

    print(f"Common to all players: {common_to_all}")

    rare_achievements = []

    for player in player_list:
        for achievement in player.achievements:
            if is_rare_achievement(achievement, player, player_list):
                rare_achievements.append(achievement)

    rare_achievements = set(rare_achievements)

    print(f"Rare achievements (1 player): {rare_achievements}\n")

    # Player.compare_achievements(alice, bob)

    common_achievements = alice.achievements.intersection(bob.achievements)
    alice_unique = alice.achievements.difference(common_achievements)
    bob_unique = bob.achievements.difference(common_achievements)

    print(f"{alice.name} vs {bob.name} common: {common_achievements}")
    print(f"{alice.name} unique: {alice_unique}")
    print(f"{bob.name} unique: {bob_unique}")


if __name__ == "__main__":
    ft_achievement_tracker()

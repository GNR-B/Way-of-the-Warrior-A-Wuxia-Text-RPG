from battle import battle
from character import Enemy
import random

def explore(player):
    print("You can go to:")
    print("1. Dark Forest  2. Shaolin Temple  3. Luoyang City")
    place = input("Where do you want to go? ")
    if place == '1':
        print("You enter the Dark Forest...")
        if random.random() > 0.5:
            enemy = Enemy("Bandit", 40, 10)
            battle(player, enemy)
        else:
            print("You found a Health Potion!")
            player.inventory.append("Health Potion")
    elif place == '2':
        print("You train at Shaolin Temple. HP restored.")
        player.hp = min(100, player.hp + 30)
    elif place == '3':
        print("You bought a Health Potion at Luoyang market.")
        player.inventory.append("Health Potion")
    else:
        print("Unknown location.")

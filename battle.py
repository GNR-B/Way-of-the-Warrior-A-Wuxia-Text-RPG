import random

def battle(player, enemy):
    print(f"You encountered a {enemy.name}! Battle begins!")
    while player.hp > 0 and enemy.hp > 0:
        print(f"\nYour HP: {player.hp} | Enemy HP: {enemy.hp}")
        print("1. Normal Attack  2. Use Skill")
        choice = input("Choose your action: ")
        if choice == '1':
            damage = player.atk - random.randint(0, 3)
        elif choice == '2':
            damage = player.atk + 5
            print(f"You used your skill: {player.skill}!")
        else:
            print("Invalid action. Defaulting to Normal Attack.")
            damage = player.atk

        enemy.hp -= damage
        print(f"You dealt {damage} damage to {enemy.name}!")

        if enemy.hp <= 0:
            print(f"You defeated {enemy.name}!")
            player.gain_exp(10)
            return

        enemy_damage = enemy.atk - random.randint(0, 2)
        player.hp -= enemy_damage
        print(f"{enemy.name} hit you for {enemy_damage} damage!")

    if player.hp <= 0:
        print("You were defeated... Game Over.")
        exit()

from character import create_player, Character
from map import explore
from utils import print_divider

def main():
    print("Welcome to *Way of the Warrior: A Wuxia Text RPG*!")
    name = input("Enter your warrior name: ")
    player = create_player(name)

    while True:
        print_divider()
        print(f"{player.name} [{player.school}] - HP: {player.hp}")
        print("1. Explore the map")
        print("2. Check status")
        print("3. Use item")
        print("4. Exit game")
        choice = input("Your action: ")
        if choice == '1':
            explore(player)
        elif choice == '2':
            player.show_status()
        elif choice == '3':
            player.use_item()
        elif choice == '4':
            print("Thanks for playing! Farewell, warrior.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

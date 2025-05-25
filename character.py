class Character:
    def __init__(self, name, school, hp, atk, defense, skill):
        self.name = name
        self.school = school
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.skill = skill
        self.inventory = ["Health Potion"]
        self.exp = 0
        self.level = 1

    def show_status(self):
        print(f"Name: {self.name} | School: {self.school} | Level: {self.level}")
        print(f"HP: {self.hp} | ATK: {self.atk} | DEF: {self.defense} | Skill: {self.skill}")
        print(f"Inventory: {', '.join(self.inventory)}")

    def use_item(self):
        if "Health Potion" in self.inventory:
            self.hp += 20
            self.inventory.remove("Health Potion")
            print("You used a Health Potion. Recovered 20 HP.")
        else:
            print("You have no usable items.")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"You gained {amount} EXP!")
        if self.exp >= 30:
            self.level += 1
            self.exp -= 30
            self.hp += 10
            self.atk += 2
            self.defense += 1
            print(f"🎉 You leveled up to Level {self.level}!")
            print("Stats increased: +10 HP, +2 ATK, +1 DEF")

class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

def create_player(name):
    print("Choose your martial arts school:")
    print("1. Shaolin  2. Wudang  3. Emei  4. Huashan  5. Beggar Sect")
    choice = input("Enter number: ")
    if choice == '1':
        return Character(name, "Shaolin", 100, 15, 10, "Arhat Fist")
    elif choice == '2':
        return Character(name, "Wudang", 90, 12, 12, "Tai Chi Sword")
    elif choice == '3':
        return Character(name, "Emei", 80, 18, 8, "Nine Yin Claw")
    elif choice == '4':
        return Character(name, "Huashan", 75, 20, 6, "Dugu Sword")
    elif choice == '5':
        return Character(name, "Beggar Sect", 85, 16, 9, "Dragon Palm")
    else:
        print("Invalid choice. Defaulting to Huashan.")
        return Character(name, "Huashan", 75, 20, 6, "Dugu Sword")

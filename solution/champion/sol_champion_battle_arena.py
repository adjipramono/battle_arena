import random

MAX_HP = 100


def show_status(hero_hp, monster_hp):
    print("=== STATUS ===")
    print("Hero HP:", hero_hp)
    print("Monster HP:", monster_hp)


def roll_damage(low=5, high=15):
    return random.randint(low, high)


def attack(hp, damage):
    hp = hp - damage
    if hp < 0:
        hp = 0
    return hp


def heal(hp, amount=15, max_hp=MAX_HP):
    hp = hp + amount
    if hp > max_hp:
        hp = max_hp
    return hp


def get_choice():
    """Keep asking until the player types a valid choice."""
    while True:
        choice = input("Choose (a)ttack or (h)eal: ").strip().lower()
        if choice in ("a", "h"):
            return choice
        print("Invalid choice. Type a or h.")


def enemy_choice(monster_hp):
    """Decide what the monster does. When it is badly hurt, it sometimes heals."""
    if monster_hp < 30 and random.randint(1, 3) == 1:
        return "heal"
    return "attack"


def play_game():
    hero_hp = MAX_HP
    monster_hp = MAX_HP

    while hero_hp > 0 and monster_hp > 0:
        show_status(hero_hp, monster_hp)
        choice = get_choice()

        if choice == "a":
            damage = roll_damage()
            monster_hp = attack(monster_hp, damage)
            print("Hero hits for", damage)
        else:
            hero_hp = heal(hero_hp)
            print("Hero heals!")

        if monster_hp > 0:
            if enemy_choice(monster_hp) == "heal":
                monster_hp = heal(monster_hp)
                print("Monster heals!")
            else:
                damage = roll_damage()
                hero_hp = attack(hero_hp, damage)
                print("Monster hits for", damage)

    if hero_hp == 0:
        return "lose"
    return "win"


def main():
    while True:
        result = play_game()
        if result == "win":
            print("You win! The monster is defeated.")
        else:
            print("You lose! The hero has fallen.")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


main()
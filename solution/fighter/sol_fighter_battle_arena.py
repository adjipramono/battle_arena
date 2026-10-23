import random


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


def heal(hp, amount=15, max_hp=100):
    hp = hp + amount
    if hp > max_hp:
        hp = max_hp
    return hp


hero_hp = 100
monster_hp = 100

while hero_hp > 0 and monster_hp > 0:
    show_status(hero_hp, monster_hp)
    choice = input("Choose (a)ttack or (h)eal: ").strip().lower()

    if choice == "a":
        damage = roll_damage()
        monster_hp = attack(monster_hp, damage)
        print("Hero hits for", damage)
    elif choice == "h":
        hero_hp = heal(hero_hp)
        print("Hero heals!")
    else:
        print("Invalid choice. You lose your turn!")

    if monster_hp > 0:
        damage = roll_damage()
        hero_hp = attack(hero_hp, damage)
        print("Monster hits for", damage)

if hero_hp == 0:
    print("You lose! The hero has fallen.")
else:
    print("You win! The monster is defeated.")
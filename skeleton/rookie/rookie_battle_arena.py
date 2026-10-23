import random


# ---------- STAGE 1: the building blocks ----------

def show_status(hero_hp, monster_hp):
    print("=== STATUS ===")
    print("Hero HP:", hero_hp)
    print("Monster HP:", monster_hp)


def attack(hp, damage):
    hp = hp - damage
    if hp < 0:
        hp = 0
    return hp


def roll_damage(low=5, high=15):
    # TODO 1: return a random whole number between low and high
    # Hint: random.randint(low, high)
    pass


def heal(hp, amount=15, max_hp=100):
    # TODO 2: add amount to hp
    # TODO 3: if hp is now more than max_hp, set it to max_hp
    # TODO 4: return the new hp
    pass


# ---------- STAGE 1 CHECKPOINT: test your functions ----------
# Remove the # at the start of each line to run these checks.
# print(attack(100, 12))   # expect 88
# print(attack(10, 25))    # expect 0
# print(heal(50, 15))      # expect 65
# print(heal(95))          # expect 100
# print(roll_damage())     # expect a number from 5 to 15


# ---------- STAGE 2: the game ----------
# The while loop repeats everything indented under it,
# as long as BOTH hero_hp and monster_hp are above 0.
hero_hp = 100
monster_hp = 100

while hero_hp > 0 and monster_hp > 0:
    show_status(hero_hp, monster_hp)
    choice = input("Choose (a)ttack or (h)eal: ")

    if choice == "a":
        # TODO 5: roll damage, then use attack() on monster_hp
        # TODO 6: print "Hero hits for" and the damage
        pass
    elif choice == "h":
        # TODO 7: use heal() on hero_hp
        # TODO 8: print "Hero heals!"
        pass
    else:
        print("Invalid choice. You lose your turn!")

    if monster_hp > 0:
        # TODO 9: the monster attacks the hero (roll damage, use attack() on hero_hp)
        # TODO 10: print "Monster hits for" and the damage
        pass

if hero_hp == 0:
    print("You lose! The hero has fallen.")
else:
    print("You win! The monster is defeated.")
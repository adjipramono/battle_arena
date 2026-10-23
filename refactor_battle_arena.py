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


hero_hp = 100
monster_hp = 100

# Round 1
show_status(hero_hp, monster_hp)
damage = roll_damage()
monster_hp = attack(monster_hp, damage)
print("Hero hits for", damage)
damage = roll_damage()
hero_hp = attack(hero_hp, damage)
print("Monster hits for", damage)

# Round 2
show_status(hero_hp, monster_hp)
damage = roll_damage()
monster_hp = attack(monster_hp, damage)
print("Hero hits for", damage)
damage = roll_damage()
hero_hp = attack(hero_hp, damage)
print("Monster hits for", damage)
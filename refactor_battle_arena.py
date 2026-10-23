import random


# def show_status(hero_hp, monster_hp):
#     print("=== STATUS ===")
#     print("Hero HP:", hero_hp)
#     print("Monster HP:", monster_hp)


# def roll_damage(low=10, high=30):
#     return random.randint(low, high)


def attack(hp=100, damage=10):
    hp = hp - damage
    if hp < 0:
        hp = 0
    return hp

def heal(hp, amount=15, max_hp=100):
    hp = hp + amount
    if hp > max_hp:
        hp = max_hp
    return hp

monster_hp = 100
monster_hp_after_attack = attack(monster_hp, 10)
# it should return 90
monster_hp_after_heal = heal(monster_hp_after_attack, 20)
# it should return 100

print("Monster HP after attack:", monster_hp_after_attack)

print("Monster HP after heal:", monster_hp_after_heal)



# hero_hp = 100
# monster_hp = 100

# # Round 1
# show_status(hero_hp, monster_hp)
# # No neeed to change this line, just use the roll_damage() function
# damage = roll_damage()
# monster_hp = attack(monster_hp, damage)
# print("Hero hits for", damage)
# # No neeed to change this line, just use the roll_damage() function
# damage = roll_damage()
# hero_hp = attack(hero_hp, damage)
# print("Monster hits for", damage)

# # Round 2
# show_status(hero_hp, monster_hp)
# # No neeed to change this line, just use the roll_damage() function
# damage = roll_damage()
# monster_hp = attack(monster_hp, damage)
# print("Hero hits for", damage)
# # No neeed to change this line, just use the roll_damage() function
# damage = roll_damage()
# hero_hp = attack(hero_hp, damage)
# print("Monster hits for", damage)
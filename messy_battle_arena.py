import random

hero_hp = 100
monster_hp = 100

# Round 1
print("=== STATUS ===")
print("Hero HP:", hero_hp)
print("Monster HP:", monster_hp)
damage = random.randint(5, 15)
monster_hp = monster_hp - damage
if monster_hp < 0:
    monster_hp = 0
print("Hero hits for", damage)
damage = random.randint(5, 15)
hero_hp = hero_hp - damage
if hero_hp < 0:
    hero_hp = 0
print("Monster hits for", damage)

# Round 2
print("=== STATUS ===")
print("Hero HP:", hero_hp)
print("Monster HP:", monster_hp)
damage = random.randint(5, 15)
monster_hp = monster_hp - damage
if monster_hp < 0:
    monster_hp = 0
print("Hero hits for", damage)
damage = random.randint(5, 15)
hero_hp = hero_hp - damage
if hero_hp < 0:
    hero_hp = 0
print("Monster hits for", damage)
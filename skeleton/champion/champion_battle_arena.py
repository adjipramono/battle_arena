import random

MAX_HP = 100


# ---------- STAGE 1: the core functions ----------

def show_status(hero_hp, monster_hp):
    """Print the three-line status display."""
    # TODO: print "=== STATUS ===", then "Hero HP:" and "Monster HP:" with their values
    pass


def roll_damage(low=5, high=15):
    """Return a random whole number from low to high."""
    # TODO
    pass


def attack(hp, damage):
    """Return the new HP after the damage. Never below 0."""
    # TODO
    pass


def heal(hp, amount=15, max_hp=MAX_HP):
    """Return the new HP after healing. Never above max_hp."""
    # TODO
    pass


# ---------- STAGE 2: the smart pieces ----------

def get_choice():
    """Keep asking until the player types a valid choice. Return "a" or "h".
    Accept capitals and extra spaces. An invalid choice prints
    "Invalid choice. Type a or h." and asks again (no lost turn)."""
    # TODO
    pass


def enemy_choice(monster_hp):
    """Return "attack" or "heal".
    A monster with 30 HP or more always attacks.
    A monster under 30 HP heals about 1 time in 3, and attacks otherwise.
    This function decides only. It does not change any HP."""
    # TODO
    pass


def play_game():
    """Play one full game. Return "win" or "lose".
    HP values live inside this function. The hero acts first.
    If the monster is defeated, it does not get another turn."""
    # TODO
    pass


def main():
    """Play a game, print the result, then ask "Play again? (y/n): ".
    If the answer is not y, print "Thanks for playing!" and stop."""
    # TODO
    pass


# Start the game. Keep this as the last line of your file.
main()
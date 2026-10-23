# Week 4: Function Part II, Battle Arena

In class you learned **why** functions are worth writing: change something once, reuse code, read your program like a story, and test one piece at a time.

This folder is where you **prove it yourself**. You'll build a text-based game called the **Battle Arena**, where a hero fights a monster, and use functions to keep it clean.

You can finish it in class, or keep going at home.

---

## The Big Idea

> If you catch yourself copying and pasting, make a function.

Functions let you write a piece of code once and use it as many times as you like. When your boss (or your teacher) asks for a change, you edit **one place** instead of ten.

---

## What's in This Folder

```
w4/
├── README.md                        <- you are here
├── messy_battle_arena.py            <- the lecture demo WITHOUT functions
├── refactor_battle_arena.py         <- the same demo WITH functions
├── skeleton/                        <- START HERE: your station's starter code
│   ├── rookie/
│   │   ├── README.MD
│   │   └── rookie_battle_arena.py
│   ├── fighter/
│   │   ├── README.MD
│   │   └── fighter_battle_arena.py
│   └── champion/
│       ├── README.MD
│       └── champion_battle_arena.py

```

---

## Get the Files

On this GitHub page, click the green **Code** button, then **Download ZIP**. Unzip it, and open the `w4` folder in **VS Code**.

You already have **Python** and **VS Code** installed, so you're ready to go.

---

## Start Here: 3 Steps

### Step 1. Pick your station

| Station | Best for | What you do | Your folder |
|---|---|---|---|
| **Rookie** | You want guidance | Fill in the `TODO` comments in a starter file that already has part of the game | [`skeleton/rookie`](skeleton/rookie) |
| **Fighter** | You're comfortable and want a challenge | Write the functions and the game loop yourself, from a written spec | [`skeleton/fighter`](skeleton/fighter) |
| **Champion** | You want a stretch | Build extra functions, a smarter monster, and a play-again option | [`skeleton/champion`](skeleton/champion) |

Not sure? Pick the one that feels like a **good challenge**, not the easiest and not the hardest. You can always move up a level.

### Step 2. Read your station's README

Each station folder has its own `README.MD` with the full instructions, the messages your game must print, and **expected scenarios** so you can check your work:

- [Rookie instructions](skeleton/rookie/README.MD)
- [Fighter instructions](skeleton/fighter/README.MD)
- [Champion instructions](skeleton/champion/README.MD)

### Step 3. Write code in the skeleton file

Open your station's `*_battle_arena.py` file and start coding. Run it often. Small steps, then run, then fix.

---

## How to Run Your Game

1. In VS Code, open the **terminal** (Terminal menu, then New Terminal).
2. Move into your station's folder. For example, for Rookie:

   ```
   cd skeleton/rookie
   ```

3. Run your file:

   ```
   python rookie_battle_arena.py
   ```

   On some computers the command is `python3` instead of `python`. If one doesn't work, try the other.

Use the same steps for Fighter and Champion, with their own folder and file name.

---

## The Three Stages

Every station works through the same three stages.

| Stage | What you do | How you know you're done |
|---|---|---|
| **1. Build the core functions** | Write `show_status`, `roll_damage`, `attack`, and `heal`. Check each one **by itself** before building the game. | Each function gives the expected result from your station's README |
| **2. Build the game loop** | Put the functions together: show the status, ask attack or heal, the hero acts, the monster attacks, repeat until someone reaches 0 HP. | You can play a full game from start to finish |
| **3. Change requests** | Your "boss" asks for changes. Make each one and **count how many places you edited**. | Your counts are mostly **1** |

### Stage 3: the change requests

| Card | Change request | Who does it |
|---|---|---|
| 1 | Damage should be **8 to 18**, not 5 to 15 | Everyone |
| 2 | Add **critical hits**: a 20% chance to deal double damage | Everyone |
| 3 | Healing should restore **20 HP**, not 15 | Fighter and Champion |
| 4 | Show each HP value as a **health bar**, like `[#####-----]` | Champion |
| 5 | Add a **defend** action that halves the next hit | Champion |

Keep a scoreboard (in a notebook, or in a comment at the top of your file):

| Card | Places I edited | How long it took |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

If you edited more than one place, ask yourself: **could that code live in one function?**

---

## The Lecture Demo: Feel the Difference

Two files show the same two-round fight. Try this exercise to see why functions matter.

- [`messy_battle_arena.py`](messy_battle_arena.py): the code **copy-pasted**, with no functions.
- [`refactor_battle_arena.py`](refactor_battle_arena.py): the **same game** with three functions.

**Try it:** make these three changes in **each** file, and count how many places you edit.

1. Change the damage range from 5-15 to **8-18**.
2. Change the header from `=== STATUS ===` to `*** STATUS ***`.
3. Add **critical hits** (a 20% chance of double damage).

| Change | `messy_battle_arena.py` | `refactor_battle_arena.py` |
|---|---|---|
| Damage 8 to 18 | | |
| Change the header | | |
| Critical hits | | |

Then imagine the game had **10 rounds** instead of 2. That's the benefit of functions.

---

## Quick Reference: The Arena Functions

| Function | What it does | Gives back |
|---|---|---|
| `show_status(hero_hp, monster_hp)` | Prints the status display | Nothing (it prints) |
| `roll_damage(low=5, high=15)` | Picks a random damage number | A whole number from `low` to `high` |
| `attack(hp, damage)` | Subtracts damage from HP, never below 0 | The new HP |
| `heal(hp, amount=15, max_hp=100)` | Adds HP, never above the maximum | The new HP |

**Champion** adds `get_choice()`, `enemy_choice(monster_hp)`, `play_game()`, and `main()`.

**Remember:** a function can't change a variable outside it. It takes the value in and **hands the new value back**, so you store it:

```python
hero_hp = attack(hero_hp, damage)
```

If you forget to store the answer, `hero_hp` never changes.

---

## Stuck? Use the 6-Step Routine

1. **Reproduce:** what exact input causes the problem?
2. **Read** the error message, **last line first**.
3. **Locate:** find the line it points to.
4. **Guess:** say out loud what you think is wrong.
5. **Change one thing**, then run it again.
6. **Print the values:** if you're still stuck, `print()` your variables to see what they really hold.

### Errors you'll probably meet

| Error | Usually means |
|---|---|
| `SyntaxError` | Python can't read the code (a missing colon, or `=` where you meant `==`) |
| `IndentationError` | Lines aren't lined up |
| `NameError` | A name doesn't exist (a typo, or calling a function before defining it) |
| `TypeError` | Wrong type for the operation (often a function that gave back `None`) |

### Common Arena bugs

| What you see | Check this |
|---|---|
| A function gives back `None` | Did you use `return` instead of `print`? |
| HP never changes | Did you **store** what the function gave back? |
| The game never ends | Same as above: is the new HP being stored? |
| The monster attacks after it's defeated | Is the monster's turn inside `if monster_hp > 0:`? |

Still stuck after the routine? Ask a classmate or your teacher, and **explain the error message in your own words** first.

---

## Using the Solutions

The `solution` folder has a working version for each station. Use it well:

- **Try first.** Give it a real attempt before you look. Getting stuck is part of learning.
- **Look at one function at a time,** not the whole file.
- **Compare, don't copy.** Read the solution, close it, and write your own version. If you can't write it without peeking, you don't understand it yet.
- **Your code can be different and still correct.** If your game plays like the expected scenarios, it works.

---

## Finished? Level Up

- Done with **Rookie**? Try **Fighter**.
- Done with **Fighter**? Try **Champion**.
- Done with **Champion**? Design your own change request card, and challenge a classmate to make it with one edit.
- Want a bigger challenge? Add something new to your game: a second monster, a potion inventory, or a "flee" action. Plan which **functions** you'd need before you write any code.

---

## One Last Thing

At the start of the lesson you wrote an answer to **"Why bother writing functions?"**

Now that you've built the game, write a new answer in 2 or 3 sentences. Use **an example from your own game**.

> Example: *"Functions let you change something once. When the boss wanted critical hits, I only edited `roll_damage`, and it worked for the hero and the monster."*

Save your game, and keep this folder. Next session builds on it.
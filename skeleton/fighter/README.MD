# Station: Fighter

**Your goal:** Build a Battle Arena game from small **functions**, then prove how much easier functions make changes.

This handout gives you requirements, not step-by-step instructions. Decide the order yourself.

> **How to read this handout:** "Expected" shows what your program should do. Damage is **random**, so your numbers will differ from the examples. Where a number must be exact, the handout says so. Match the messages exactly.

---

## The Game

A hero fights a monster. Both start with **100 HP**. Each turn:

1. The game shows the status.
2. The player chooses to **attack** (`a`) or **heal** (`h`).
3. If the monster is still alive, the monster attacks the hero.
4. The game ends when someone reaches **0 HP**.

**Messages your game must print:**

| When | Message |
|---|---|
| The hero attacks | `Hero hits for` followed by the damage |
| The hero heals | `Hero heals!` |
| The monster attacks | `Monster hits for` followed by the damage |
| An invalid choice | `Invalid choice. You lose your turn!` |
| You win | `You win! The monster is defeated.` |
| You lose | `You lose! The hero has fallen.` |

**The status display** (printed at the start of every turn):
```
=== STATUS ===
Hero HP: 100
Monster HP: 100
```

---

## Your Starter File: `fighter_starter.py`

It gives you the starting HP values, the `import random` line, and the **`while` loop** header, which repeats everything indented under it as long as both HP values are above 0. Delete the placeholder `break` line when you start writing your turn.

`random.randint(low, high)` gives a random whole number from `low` to `high`, including both.

---

## Stage 1: Build and Test the Functions (15 min)

### Requirements

Write four functions. Each one does **one job**, and none of them uses a variable from outside.

1. **`show_status(hero_hp, monster_hp)`**: prints the three-line status display above.
2. **`roll_damage(low=5, high=15)`**: **returns** a random whole number from `low` to `high`. The range lives here, as default values.
3. **`attack(hp, damage)`**: **returns** the new HP after subtracting the damage. HP never goes below `0`.
4. **`heal(hp, amount=15, max_hp=100)`**: **returns** the new HP after adding `amount`. HP never goes above `max_hp`.

### Expected results

| Check | Expected |
|---|---|
| `attack(100, 12)` | `88` |
| `attack(10, 25)` | `0` (never below zero) |
| `heal(50, 15)` | `65` |
| `heal(95)` | `100` (never above the maximum) |
| `roll_damage()` | a whole number from `5` to `15` |

**Test each function by itself before you build the game.** Run `roll_damage()` several times: the number should change, but always stay in range.

### Hints

- A function that **prints** gives back `None`. If you need the answer, use `return`.
- Names matter. A good function name is a verb that says what it does.

**Checkpoint:** all five checks give the expected result.

---

## Stage 2: Build the Game Loop (15 min)

### Requirements

1. Each turn: show the status, ask `Choose (a)ttack or (h)eal: `, and carry out the choice.
2. **Attack:** roll damage, reduce the monster's HP, print `Hero hits for` and the damage.
3. **Heal:** increase the hero's HP, print `Hero heals!`.
4. **Anything else:** print `Invalid choice. You lose your turn!` The monster still attacks.
5. **Forgiving input:** the choice still works if the player types a capital letter or extra spaces, like `A` or ` h `.
6. **The monster's turn:** if the monster is alive, it rolls damage, attacks the hero, and prints `Monster hits for` and the damage.
7. **The end:** when the loop finishes, print who won.

### Remember

A function can't change a variable outside it. Take the value in, **hand the new value back**, and store it:

> `hero_hp = attack(hero_hp, damage)`

### Expected scenarios

**Scenario A: attacking** (your numbers will differ)
```
=== STATUS ===
Hero HP: 100
Monster HP: 100
Choose (a)ttack or (h)eal: a
Hero hits for 12
Monster hits for 9
```
Both damage numbers must be between 5 and 15. The next status shows the monster at `88` and the hero at `91`.

**Scenario B: healing at full health**
```
Choose (a)ttack or (h)eal: h
Hero heals!
Monster hits for 7
```
The hero heals from 100 and stays at 100. After the monster's hit, the hero is at `93`.

**Scenario C: an invalid choice**
```
Choose (a)ttack or (h)eal: x
Invalid choice. You lose your turn!
Monster hits for 8
```

**Scenario D: forgiving input**
```
Choose (a)ttack or (h)eal:  A 
Hero hits for 10
```
` A ` (a capital letter with spaces) works just like `a`.

**Scenario E: the monster is defeated**
```
Hero hits for 14
You win! The monster is defeated.
```
The game ends **immediately**. The monster does **not** get one last attack.

**Scenario F: the hero is defeated**
```
Monster hits for 11
You lose! The hero has fallen.
```

### Hints

- Search for string methods that remove spaces and change case.
- Your loop's condition already ends the game when someone hits 0. Check who won **after** the loop.
- If the monster keeps attacking after 0 HP, check the condition around its turn.

**Checkpoint:** you can play a full game from start to finish.

---

## Stage 3: Change Requests (12 min)

Your boss sends change requests. After **each one**, write on your scoreboard:

- **Places I edited:** how many places in your code did you change?
- **How long it took.**

### Card 1: "Damage should be 8 to 18."
**Expected:** damage for both the hero and the monster is between 8 and 18.

### Card 2: "Add critical hits: a 20% chance to deal double damage."
**Expected:** about 1 in 5 hits is a critical hit. Print `Critical hit!` when it happens and double that hit's damage. The hero **and** the monster can crit.

**Hint:** `random.randint(1, 5)` gives a number from 1 to 5. If it gives `1`, that's your 20% chance.

### Card 3: "Healing should restore 20 HP, not 15."
**Expected:** each heal restores 20 HP, still capped at 100. Your `Hero heals!` message does not need to change.

### The question for each card
**Where does the change belong?** If you designed your functions well, the answer is usually **one place**. If you edited more than one, ask: *could that code live in one function?*

---

## Done Checklist

- [ ] All four functions pass the Stage 1 checks
- [ ] The game plays from start to finish
- [ ] HP never goes below 0 or above 100
- [ ] `A` and ` h ` (capitals and spaces) work as choices
- [ ] The monster doesn't attack after it is defeated
- [ ] Cards 1 to 3 are done, and your scoreboard is filled in
- [ ] Game saved in your portfolio folder

**Finished early?** Try Cards 4 and 5 from the Champion handout (a health bar, and a defend action).
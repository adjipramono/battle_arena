# Station: Champion

**Your goal:** Build a Battle Arena that is organized like real software: small functions that each do one job, a smart monster, a play-again option, and changes that touch **one place**.

This handout gives you constraints and challenges, not steps. How you structure it is up to you.

> **How to read this handout:** "Expected" shows what your program should do. Damage is **random**, so your numbers will differ from the examples. Where something must be exact, the handout says so. Match the messages exactly.

---

## The Game

A hero fights a monster. Both start with **100 HP**. Each turn the player attacks (`a`) or heals (`h`), then the monster acts. The game ends when someone reaches **0 HP**.

**Messages your game must print:**

| When | Message |
|---|---|
| The hero attacks | `Hero hits for` followed by the damage |
| The hero heals | `Hero heals!` |
| The monster attacks | `Monster hits for` followed by the damage |
| The monster heals | `Monster heals!` |
| An invalid choice | `Invalid choice. Type a or h.` (then ask again) |
| You win | `You win! The monster is defeated.` |
| You lose | `You lose! The hero has fallen.` |
| After a game | `Play again? (y/n): ` |
| When the player quits | `Thanks for playing!` |

**The status display** (printed at the start of every turn):
```
=== STATUS ===
Hero HP: 100
Monster HP: 100
```

## Your Starter Files

**`champion_starter.py`** gives you the name and purpose of every function, with the bodies left for you. Read each description carefully: it is your spec. You write everything inside.

`random.randint(low, high)` gives a random whole number from `low` to `high`, including both.

---

## Stage 1: Build the Core Functions and Check Them (15 min)

### Requirements

1. A constant `MAX_HP = 100` at the top of your file.
2. **`show_status(hero_hp, monster_hp)`**: prints the status display.
3. **`roll_damage(low=5, high=15)`**: **returns** a random whole number from `low` to `high`.
4. **`attack(hp, damage)`**: **returns** the new HP. Never below `0`.
5. **`heal(hp, amount=15, max_hp=MAX_HP)`**: **returns** the new HP. Never above `max_hp`.

### Expected results

| Check | Expected |
|---|---|
| `attack(100, 12)` | `88` |
| `attack(10, 25)` | `0` |
| `heal(50, 15)` | `65` |
| `heal(95)` | `100` |
| `roll_damage()` | a whole number from `5` to `15` |

### Check each function by itself

Before you build the game, call each function on its own and look at the result.

1. Below your functions, temporarily add a `print(...)` line for each check in the table above.
2. Run the file. Compare each printed result with the **Expected** column.
3. For `roll_damage()`, run the file several times. The number should change, but always stay from `5` to `15`.
4. When everything matches, comment those lines out so they don't clutter your game.

### Hints

- Break one function on purpose (for example, remove the cap in `heal`) and confirm your check shows the wrong result. A check you've never seen fail might not be checking anything.
- A function that **prints** gives back `None`. If a check shows `None`, you probably forgot `return`.

**Checkpoint:** all five checks give the expected result.

---

## Stage 2: Build the Game with Smart Pieces (15 min)

### Requirements

1. **`get_choice()`**: keeps asking `Choose (a)ttack or (h)eal: ` until the player types a valid choice, then **returns** `"a"` or `"h"`.
   - Capital letters and extra spaces are accepted.
   - An invalid choice prints `Invalid choice. Type a or h.` and asks again. The player does **not** lose a turn.
2. **`enemy_choice(monster_hp)`**: **returns** `"attack"` or `"heal"`.
   - A healthy monster (30 HP or more) **always** attacks.
   - A badly hurt monster (under 30 HP) heals about **1 time in 3**, and attacks otherwise.
3. **`play_game()`**: plays **one full game** and **returns** `"win"` or `"lose"`. HP values live **inside** this function.
4. **`main()`**: plays a game, prints the winning or losing message, then asks `Play again? (y/n): `. If the answer isn't `y`, print `Thanks for playing!` and stop.
5. **One job per function.** `get_choice` asks and validates. `enemy_choice` decides. Neither of them changes HP.
6. The hero's turn happens first. If the monster is defeated, the game ends **immediately** and the monster doesn't act.

### Expected scenarios

**Scenario A: invalid input does not cost a turn**
```
Choose (a)ttack or (h)eal: zzz
Invalid choice. Type a or h.
Choose (a)ttack or (h)eal: a
Hero hits for 12
```

**Scenario B: forgiving input**
```
Choose (a)ttack or (h)eal:  A 
Hero hits for 10
```

**Scenario C: a hurt monster sometimes heals**
```
Hero hits for 13
Monster heals!
```
This happens only when the monster is under 30 HP, and not every time.

**Scenario D: a healthy monster always attacks**
```
Monster HP: 80
...
Monster hits for 9
```

**Scenario E: play again**
```
You win! The monster is defeated.
Play again? (y/n): y
=== STATUS ===
Hero HP: 100
Monster HP: 100
```
A new game starts with both HP values reset to 100.

**Scenario F: quitting**
```
You lose! The hero has fallen.
Play again? (y/n): n
Thanks for playing!
```

### Hints

- A function that decides (`enemy_choice`) should **return** a value, not change HP. That keeps each function to one job.
- Variables created inside `play_game` stay inside it. That's why `play_game` **returns** the result.
- Call `main()` once, at the bottom of your file, so the game starts when you run it.

**Checkpoint:** you can play several games in a row, then quit.

---

## Stage 3: Change Requests (12 min)

Your boss sends change requests. After **each one**, write on your scoreboard:

- **Places I edited.**
- **How long it took.**

### Card 1: "Damage should be 8 to 18."
**Expected:** all damage is between 8 and 18.

### Card 2: "Add critical hits: a 20% chance to deal double damage."
**Expected:** about 1 in 5 hits is a critical hit. Print `Critical hit!` and double that hit's damage. The hero and the monster can both crit.

### Card 3: "Healing should restore 20 HP, not 15."
**Expected:** each heal restores 20 HP, still capped at 100.

### Card 4: "Show the status as a health bar."
**Expected:** each HP line ends with a bar of 10 characters: one `#` for every 10 HP (rounded down), and `-` for the rest.

```
Hero HP: 100 [##########]
Monster HP: 55 [#####-----]
```

Write a helper function `health_bar(hp)`. It should pass these exact checks:

| Check | Expected |
|---|---|
| `health_bar(100)` | `"[##########]"` |
| `health_bar(91)` | `"[#########-]"` |
| `health_bar(55)` | `"[#####-----]"` |
| `health_bar(0)` | `"[----------]"` |

### Card 5: "Add a defend action that halves the next hit."
**Expected:** the player can choose `d`.

```
Choose (a)ttack, (h)eal, or (d)efend: d
Hero braces for the next hit!
Monster hits for 7
```

If the monster would have rolled 14, the hit is halved to 7 (round down). The defense lasts for **one** hit only. The prompt now lists all three choices, and an invalid choice now says `Invalid choice. Type a, h, or d.`

### The question for each card
**Where does the change belong?** With well-designed functions the answer is usually **one place** (Card 5 is the exception: it needs a small new function, one new variable, and `get_choice` must accept `d`). If you edited more than one place, ask: *could that code live in one function?*

---

## Done Checklist

- [ ] All five Stage 1 checks gave the expected results
- [ ] `get_choice`, `enemy_choice`, `play_game`, and `main` are separate functions that each do one job
- [ ] Invalid input does not cost the player a turn
- [ ] The play-again loop works and ends with `Thanks for playing!`
- [ ] Cards 1 to 5 are done, and your scoreboard is filled in
- [ ] Game saved in your portfolio folder

**Finished early?** Sit with a Rookie as a code buddy. Ask what they've tried first, and point at the bug instead of fixing it for them. Or design your own change request card and trade it with a classmate.
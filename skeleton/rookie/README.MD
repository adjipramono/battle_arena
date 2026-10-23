# Station: Rookie

**Your goal:** Build a Battle Arena game using **functions**, then prove how much easier functions make changes.

Take it one step at a time. Getting stuck is normal. Read the error message, then ask yourself what it's telling you.

> **How to read this handout:** "Expected" shows what your program should do. Damage is **random**, so your numbers will differ from the examples. Where a number must be exact, the handout says so.

---

## The Game

A hero fights a monster. Both start with **100 HP**. Each turn:

1. The game shows the status.
2. You choose to **attack** (`a`) or **heal** (`h`).
3. If the monster is still alive, the monster attacks you.
4. The game ends when someone reaches **0 HP**.

**Messages your game must print (match them exactly):**

| When | Message |
|---|---|
| The hero attacks | `Hero hits for` followed by the damage |
| The hero heals | `Hero heals!` |
| The monster attacks | `Monster hits for` followed by the damage |
| An invalid choice | `Invalid choice. You lose your turn!` |
| You win | `You win! The monster is defeated.` |
| You lose | `You lose! The hero has fallen.` |

---

## Your Starter File: `rookie_starter.py`

`show_status` and `attack` are already written. Read them first. You will fill in the **TODO** comments.

**Two things the starter gives you:**

- `random.randint(low, high)` gives a random whole number from `low` to `high`, including both.
- A **`while` loop** repeats everything indented under it, as long as the condition is True. Yours keeps going while both HP values are above 0.

---

## Stage 1: Build and Test the Functions (15 min)

### Your steps

1. **Finish `roll_damage` (TODO 1).** It should **return** a random whole number between `low` and `high`.
2. **Finish `heal` (TODOs 2 to 4).**
   - Add `amount` to `hp`.
   - If the new HP is more than `max_hp`, set it to `max_hp`.
   - **Return** the new HP.
3. **Test each function by itself.** In the starter file, find the lines that start with `# print(`. Remove the `#` to run each check.

### Expected results

| Check | Expected |
|---|---|
| `attack(100, 12)` | `88` |
| `attack(10, 25)` | `0` (never below zero) |
| `heal(50, 15)` | `65` |
| `heal(95)` | `100` (never above the maximum) |
| `roll_damage()` | a whole number from `5` to `15` |

Run `roll_damage()` several times. The number should change, but always stay in range.

### Hints

- Use `return`, not `print`, inside a function. A function that prints gives back `None`.
- `heal(95)` should give `100`, not `110`. Think about which line handles that.

**Checkpoint:** all five checks give the expected result. Then move to Stage 2.

---

## Stage 2: Build the Game Loop (15 min)

### Your steps

Fill in **TODOs 5 to 10** inside the `while` loop.

1. **When the player chooses `a` (TODOs 5 and 6):** roll damage, use `attack()` on `monster_hp`, and print `Hero hits for` and the damage.
2. **When the player chooses `h` (TODOs 7 and 8):** use `heal()` on `hero_hp`, and print `Hero heals!`.
3. **The monster's turn (TODOs 9 and 10):** the monster rolls damage, attacks the hero with `attack()` on `hero_hp`, and prints `Monster hits for` and the damage.

### Remember

A function can't change a variable outside it. Take the value in, **hand the new value back**, and store it:

> `hero_hp = attack(hero_hp, damage)` — if you forget to store the answer, `hero_hp` never changes.

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
Both damage numbers must be between 5 and 15. The next status should show the monster at `88` and the hero at `91` in this example.

**Scenario B: healing at full health**
```
Choose (a)ttack or (h)eal: h
Hero heals!
Monster hits for 7
```
The hero starts at 100 and heals. HP must **not** go above 100. After the monster's hit, the hero is at `93`.

**Scenario C: an invalid choice**
```
Choose (a)ttack or (h)eal: x
Invalid choice. You lose your turn!
Monster hits for 8
```
You lose your turn, but the monster still attacks.

**Scenario D: the monster is defeated**
```
Hero hits for 14
You win! The monster is defeated.
```
When the monster reaches 0 HP, the game ends **immediately**. The monster does **not** get one last attack.

**Scenario E: the hero is defeated**
```
Monster hits for 11
You lose! The hero has fallen.
```

### Hints

- Nothing prints `Monster hits` when the monster is already at 0. That's what the `if monster_hp > 0:` line is for.
- If your game never ends, check that you stored the result of `attack()`.

**Checkpoint:** you can play a full game from start to finish.

---

## Stage 3: Change Requests (12 min)

Your boss sends change requests. After **each one**, write on your scoreboard:

- **Places I edited:** how many places in your code did you change?
- **How long it took.**

### Card 1: "Damage should be 8 to 18."
**Expected:** after the change, damage for both the hero and the monster is between 8 and 18.

### Card 2: "Add critical hits: a 20% chance to deal double damage."
**Expected:** about 1 in 5 hits is a critical hit. Print `Critical hit!` when it happens, and double that hit's damage. Both the hero and the monster can crit.

**Hint:** `random.randint(1, 5)` gives a number from 1 to 5. If it gives `1`, that's your 20% chance.

### The question for each card
**Where does the change belong?** If you designed your functions well, the answer is usually **one place**. If you edited more than one, ask yourself: *could that code live in one function?*

---

## Done Checklist

- [ ] `roll_damage` and `heal` pass all five checks
- [ ] The game plays from start to finish
- [ ] HP never goes below 0 or above 100
- [ ] The monster doesn't attack after it is defeated
- [ ] Cards 1 and 2 are done, and your scoreboard is filled in
- [ ] Game saved in your portfolio folder

**Finished early?** Try Card 3 from the Fighter handout (healing restores 20 HP), or help a classmate. Ask what they've tried first, and point at the bug instead of fixing it for them.
# Chapter 14 — The Escape Room

> *"Two locks that work perfectly alone can still guard a door that opens for anyone —*
> *if nobody teaches them to listen to each other."*

---

Ninja Cat stopped at the mouth of a stone chamber and would not go one step further.

That, by itself, told them everything.

Inside, lit by torches that flickered without any wind to move them, stood a door

unlike any they'd found before. Heavy. Iron-banded. Humming, very faintly, like it

was thinking.

Two mechanisms were built into its face. A keypad, worn smooth by a thousand nervous

fingers. And beside it, a brass dial, numbered `1` through `20`, patient and silent.

"Oh, I like this room," said Captain Byte, already cracking his knuckles.

---

Dragon Debug set down his tea — an actual, genuine pause, the kind he almost never took.

"You've met both of these before," he said. "A keypad that judges a password. A dial

that waits for a guess. Separate rooms. Separate lessons."

"So this one's easy," said Captain Byte. "I already beat both."

"You beat them," said the dragon, "*apart.* This door only opens for a Builder who

can make them work **together** — one program, two locks, in the right order.

That is a different skill than either lock alone. It is, in fact, *the* skill that

turns a Builder's collection of tricks into one real piece of software."

TommyBot looked at the keypad, then the dial, then back at the keypad.

"...how hard can that be? We already have both pieces."

Dragon Debug almost smiled into his tea. "Wonderful last words. Let's find out."

---

TommyBot sat down at the console tucked beside the door and started typing —

confident, quick, barely pausing to think. This part felt familiar. Borrow the

bouncer's rules from the Password Checker. Borrow the guessing loop from the

Secret Treasure. Put them one after the other. Done.

```python
password = input("Vault password: ")

if len(password) < 8:
    print("Too short. The vault won't even listen.")
elif password == "pizza123":
    print("Nice try. Too obvious.")

secret = random.randint(1, 20)
guess = 0
attempts = 0
while guess != secret:
    guess = int(input("Combination (1-20): "))
    attempts = attempts + 1
    if guess < secret:
        print("Higher.")
    elif guess > secret:
        print("Lower.")
print("CLUNK! The vault opens in", attempts, "tries.")
```

"There," said TommyBot, sitting back. "Both locks. Both rules. Should be solid."

Captain Byte, who had been waiting with the patience of a Captain, immediately

leaned past and typed `abc` into the password prompt — just to see what would happen.

---

The console answered:

```
Vault password: abc
Too short. The vault won't even listen.
Combination (1-20):
```

It kept going.

It just... kept going. Asking for a combination. As if the password had never

mattered at all.

Captain Byte's eyes went very wide. "TommyBot. TommyBot, it's still letting me in."

He guessed his way through the dial in four tries, mostly luck, and the door

swung open with a satisfied *CLUNK* — having never once actually checked whether

his three-letter password had passed anything.

"FREE VAULT," Captain Byte announced to the empty chamber. "This is the best

security system I have ever met."

---

Sir Boolean, who had wandered over from somewhere to watch, went the color of

his own red flag — the closest a small stern knight can come to horrified.

"That is *not* how a lock is supposed to work," TommyBot said slowly, the

satisfaction from a minute ago draining right out. "The password check even

*said* it was too short. It printed the warning and then just... didn't stop

anything."

There it was again — that hot, sinking feeling. *I built this. I checked it.*

*How did I miss something the door itself was telling me?*

"That flush right there," said Dragon Debug, watching TommyBot's face, "has a

name. Even builders who've shipped a hundred programs feel it the first time an

*integration* bug bites them. Each lock, on its own, was correct. Watch —"

He typed a password of real length into the console by itself. It worked exactly

as Chapter 7 promised. He tried a lone guessing game. It worked exactly as

Chapter 6 promised.

"Both pieces are innocent," the dragon said. "That's what makes this kind of bug

sneaky. It isn't hiding *inside* either lock. It's hiding in the hallway *between*

them — the wiring nobody wrote."

---

TommyBot stared at the code for a long moment. Read it once. Read it again, slower

this time, the way the Riddle Theatre had taught back in Chapter 11.

"...the password check never actually *stops* anything," TommyBot said, almost to

itself. "It just prints a message and moves on to the next line. And the next

line is the combination lock. It doesn't care what happened above it — it just

runs. No matter what."

Dragon Debug said nothing. He didn't need to. He just watched TommyBot reach,

unprompted, for the keyboard.

"I need the combination lock to only happen if the password actually worked,"

TommyBot said. "Not printed underneath it — *inside* it. Like... a room you only

reach through a door that already opened."

```python
password = input("Vault password: ")

if len(password) < 8:
    print("Too short. The vault won't even listen.")
elif password == "pizza123":
    print("Nice try. Too obvious.")
else:
    secret = random.randint(1, 20)
    guess = 0
    attempts = 0
    while guess != secret:
        guess = int(input("Combination (1-20): "))
        attempts = attempts + 1
        if guess < secret:
            print("Higher.")
        elif guess > secret:
            print("Lower.")
    print("CLUNK! The vault opens in", attempts, "tries.")
```

One word. `else:`. And everything underneath it, tucked in a step, so it only

ever runs when neither warning above it fired.

TommyBot hit Run, typed `abc`, and this time the console simply said:

```
Vault password: abc
Too short. The vault won't even listen.
```

And stopped. No dial. No second chance. Exactly as a locked door should behave.

---

## 🧪 Testing Table

| Password tried | Expected | Actual (before `else`) | Actual (after `else`) |
|---|---|---|---|
| `abc` (too short) | Door stays shut, no combination asked | ❌ combination lock still opens | ✅ stops immediately |
| `pizza123` (the obvious one) | Door stays shut, no combination asked | ❌ combination lock still opens | ✅ stops immediately |
| a real password, 8+ letters | Combination lock appears, door opens on the right guess | ✅ worked (this path was never broken) | ✅ still works |

---

## 🐛 Debug Log

**My bug:** A password that failed with "Too short" still let the combination dial run — the vault opened for anyone who guessed the number, password or no password.

**What caused it?** The two locks were written one after the other, not one *inside* the other. Python doesn't know the second lock is supposed to depend on the first — it just runs every line in order, warning message or not, unless you tell it otherwise.

**How did I fix it?** Wrapped the whole combination lock inside an `else:` — so it only runs on the one path where neither warning above it fired. Two correct locks, finally wired to actually guard each other.

---

## 🧰 Toolbox Card

> *A program can be built entirely out of pieces that are each, individually, correct —*
> *and still be wrong. Correctness isn't just "does every piece work." It's "does the*
> ***order and shape** connect them the way the story needs." That's integration.*

---

## 🏗️ In the Real World

> Real teams test two different things, on purpose, and give them different names.
> A **unit test** checks one small piece alone — does the password rule work? Does
> the guessing loop work? An **integration test** checks whether the *pieces working
> together* still do the right thing — because, as TommyBot just found out, two
> correct pieces can still add up to a door with no lock at all.

---

## 🐉 Dragon Debug's Wisdom

> *"A lock isn't the metal. A lock is the **order** things have to happen in.*
> *Get the order right, and even simple pieces guard something real."*

---

Sir Boolean, satisfied that justice had been restored to the vault, gave a firm

nod and returned to his post — flags at the ready, dignity intact.

Professor Quackers had watched the entire ordeal from a nearby barrel and said,

as ever, nothing at all. Somehow it still felt like approval.

---

### ⭐ Achievement Unlocked

**Vault Breaker 🔓** — *You took two locks that each worked perfectly on their own and discovered that alone was never the point — you found the missing wire between them, and built the first door in the Guild that actually guards what it's supposed to.*

---

### To be continued...

From TommyBot's pocket, forgotten yet again — the encoded note sat exactly where

it always sat. Patient. Unread. Some locks, it seemed, take longer than an

afternoon to open.

"Two locks, working together," said Dragon Debug, watching the vault door swing

shut behind them for the night. "Tomorrow, you'll need *all* of them to."

Captain Byte looked back down the long road they'd walked — the counting, the

questions, the loops, the strings, the ciphers, the menus, the paint — and, for

once, didn't say anything at all.

→ *Next: Captain Byte's Treasure Quest v1 — where every trick becomes one game.* 🏴‍☠️

---

## 😄🧩🎨 Guild Extra

🧩 Guild Extra — The Fork in the Wall        (Riddle)

One wall. Two directions. Only one gets you out.

```python
direction = "LEFT"

if direction == "LEFT":
    print("The left wall slides away. You found the exit!")
elif direction == "RIGHT":
    print("A dead end. Sand pours in from the ceiling.")
else:
    print("Nothing happens. Pick LEFT or RIGHT.")
```

Expected output:
```
The left wall slides away. You found the exit!
```

🕵️ Try it: change `direction` to `"RIGHT"`, then to something silly
like `"UP"`, and run it each time. Three lines of code. Three different rooms.

---

## 🥋 Typing Dojo — Mission 009: The Vault

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

The Dojo has its own version of tonight's door — and it's exactly as unforgiving.

Two locks, stacked on one frame: the bouncer from Chapter 7, then the guessing

cave from Chapter 6, right underneath it. Nothing new to learn. Just two old

friends, finally on the same door.

**🥋 Tier I — Keyboard Ninja.** *("Slice your caps.")*

Type this. Run it.

```python
import random

password = input("Vault password: ")

if len(password) < 8:
    print("Too short. The vault won't even listen.")
elif password == "password":
    print("Really? 'password'? The vault laughs at you.")
else:
    secret = random.randint(1, 20)
    guess = 0
    attempts = 0
    while guess != secret:
        guess = int(input("Combination (1-20): "))
        attempts = attempts + 1
        if guess < secret:
            print("Higher.")
        elif guess > secret:
            print("Lower.")
    print("CLUNK! The vault opens in", attempts, "tries.")
```

Expected output:

```
Vault password: abc
Too short. The vault won't even listen.
```

```
Vault password: dragon-tea-42
Combination (1-20): 10
Lower.
Combination (1-20): 5
Higher.
Combination (1-20): 8
CLUNK! The vault opens in 3 tries.
```

**🕵️ Tier II — Conan's Challenge.** *("Do you have any clue?")*

Same vault — but **three typos** slipped in. No logic is broken. Only fingers.

```python
# The Vault
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

import random

 password = input("Vault password: ")

if lenn(password) < 8:
    print("Too short. The vault won't even listen.")
elif password == "password":
    print("Really? 'password'? The vault laughs at you.")
else:
    secret = random.randint(1, 20)
    guess = 0
    attempts = 0
    while guess =! secret:
        guess = int(input("Combination (1-20): "))
        attempts = attempts + 1
        if guess < secret:
            print("Higher.")
        elif guess > secret:
            print("Lower.")
    print("CLUNK! The vault opens in", attempts, "tries.")
```

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 7
    password = input("Vault password: ")
IndentationError: unexpected indent
```

**Excellent. Now the conversation begins.** Fix that stray leading space, run

again, and two more clues step forward — one in the bouncer's line (`lenn`),

one in the guesser's (`=!`). Fix all three, and it runs byte-for-byte like

the Tier I copy above. 🦑

🐉 Dragon Debug sips his tea. *"Interesting."*

Sir Boolean guards the top lock. The Cave guards the bottom. Old friends, one door.

Professor Quackers says nothing. Professor Quackers never does. 🦆

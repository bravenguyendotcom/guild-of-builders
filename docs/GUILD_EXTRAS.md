# 😄🧩🎨 GUILD_EXTRAS.md

### The composed Guild Extras library — Batch 1, Volume I (Chapters 1–15)

> **Status:** Batch 1 of `docs/GUILD_EXTRAS.md` (D-34). Composed fresh from
> `docs/GUILD_EXTRAS_SOURCE.md` — never copied from the raw brainstorm. Every extra is re-skinned
> to our cast, matched to its chapter's topic where possible, and — for riddles and art —
> bash-verified with real output pasted below.
> **Rotation:** 😄 Joke → 🧩 Riddle → 🎨 Art, one per chapter, from Chapter 1.
> **How to use:** drop the matching block into that chapter's Guild Extra slot (STYLE_GUIDE §4b).
> **Batch 2+** (Volumes II–IV) will grow this file later, per the build kit's batch plan.

---

## Chapter 1 — Captain Byte Sets Sail

😄 Guild Extra — The Captain's Boxes        (Joke)

Captain Byte asked Dragon Debug,
"What is a variable, really?"

Dragon Debug smiled into his tea.

"A variable is a cardboard box.
You can put anything inside.
And you get to write the label yourself."

Captain Byte grinned. "So my box could say `pizza`?"

"It could," said the dragon.
"But it will only ever hold
what you told it to hold.
Not what you were hoping for."

Captain Byte wrote it down anyway:

```python
pizza_slices = 12
```

"Just in case," he said.

---

## Chapter 2 — The Hungry Pizza Robot

🧩 Guild Extra — Quackers' Laugh Machine        (Riddle)

Professor Quackers never laughs.
He has never laughed once, in the whole story.

But run this, and see what the *ship* thinks he'd say:

```python
quack_level = 3
laughter = "Quack! " * quack_level

print("Professor Quackers rates that joke:")
print(laughter)
```

Expected output:
```
Professor Quackers rates that joke:
Quack! Quack! Quack! 
```

That trick — a piece of text, times a number — is the exact same trick
that made `"3" * 2` say `"33"` a few pages back.
Multiply text, and Python doesn't do math.
It just repeats the text, that many times.

---

## Chapter 3 — The Age Machine

🎨 Guild Extra — The Captain's First Spark        (Art)

Before doors and decisions, Captain Byte just wanted to see
something appear on the ship's screen. Something *his*.

```python
SPARK_SIZE = 3

print("*" * SPARK_SIZE)
print("*" * (SPARK_SIZE + 2))
print("*" * (SPARK_SIZE + 4))
```

Expected output:
```
***
*****
*******
```

🎨 Hack it: change `SPARK_SIZE` to `1` or `10` and run it again.
Same three lines. A completely different spark.

---

## Chapter 4 — The Ninja Health Check

😄 Guild Extra — TommyBot's Question        (Joke)

TommyBot looked at two variables on the screen.

```python
age = "13"
height = 13.0
```

"Wait," said TommyBot. "They're both 13.
Why do they look so different?"

The string sat up straight and said,
"Look at all these quote marks I get to wear!"

The float just floated there, dotted and proud,
and didn't say anything back.

Dragon Debug chuckled into his tea.

"`"13"` in quotes is text.
`13.0` with a dot is a number with a heartbeat.
Python never mixes the two by accident.
Only on purpose."

---

## Chapter 5 — Rock, Paper, Scissors

🧩 Guild Extra — The Honest Guard        (Riddle)

High on the rail, Ninja Cat set a small test
before the next door would open.

```python
ninja_home = True
threw_a_move = True

if ninja_home and threw_a_move:
    print("The shadow moves. The door swings open.")
else:
    print("Ninja Cat is not impressed. Try again.")
```

Expected output:
```
The shadow moves. The door swings open.
```

🕵️ Try it: change `threw_a_move` to `False` and run it again.
Both boxes have to say `True` for `and` to let you through.
One `False`, and the door stays shut.

---

## Chapter 6 — The Secret Treasure

🎨 Guild Extra — The Chest-Builder        (Art)

Captain Byte wanted the treasure chest to look like it was
actually *rising* out of the sand, floor by floor.

```python
FLOOR_COUNT = 4
floor = 1

while floor <= FLOOR_COUNT:
    print("#" * (floor * 2))
    floor = floor + 1
```

Expected output:
```
##
####
######
########
```

🎨 Hack it: change `FLOOR_COUNT` to `8` and watch the chest grow taller.
Same loop. A bigger chest.

---

## Chapter 7 — The Safe Password Checker

😄 Guild Extra — Sir Boolean's One Joke        (Joke)

Sir Boolean only ever carries two flags.
A green one that means **TRUE**.
A red one that means **FALSE**.

Someone once asked him for a third flag. Just in case.

He looked at them for a long moment.
Then raised the red one.

That's the whole joke.
Sir Boolean doesn't do maybe.

---

## Chapter 8 — The Recycling Robot

🧩 Guild Extra — The Bug Sweep        (Riddle)

Not everything on the salvage pile is a bug.
Some of it is just... mess. Run the sweep and see what gets squished.

```python
pile = ["typo", "loud snoring", "Error: missing tea", "silence", "Error: cold pizza"]

for item in pile:
    if "Error" in item:
        print("Squish! ->", item)
    else:
        print("Leave it, that's not a bug:", item)
```

Expected output:
```
Leave it, that's not a bug: typo
Leave it, that's not a bug: loud snoring
Squish! -> Error: missing tea
Leave it, that's not a bug: silence
Squish! -> Error: cold pizza
```

The word `in` is doing the checking here — it just asks,
*"is this smaller thing hiding somewhere inside the bigger thing?"*
That's how the robot tells a real bug from ordinary mess.

---

## Chapter 9 — The Palindrome Mirror

🎨 Guild Extra — The Mirror Cat        (Art)

Three lines of text, built from three labelled boxes.
Change the boxes, change the cat.

```python
EARS = "/\\_/\\"
EYES = "( o.o )"
MOUTH = " > ^ < "

print(EARS)
print(EYES)
print(MOUTH)
```

Expected output:
```
/\_/\
( o.o )
 > ^ < 
```

🎨 Hack it: change `EYES` to `( ^.^ )` and run it again.
Same cat. New mood.

---

## Chapter 10 — The Caesar Messenger

😄 Guild Extra — The Zero Rule        (Joke)

Captain Byte lined up his crew for the first message
and pointed at the front of the line.

"You. You're Letter Number One."

Dragon Debug shook his head. "Letter Number Zero."

"That's not fair! Nobody starts counting at zero!"

"Python does," said the dragon. "Every single time.
Once you know that one rule, ciphers, lists, and messages
all start making a lot more sense."

The crew member at the front just shrugged.
Being Zero wasn't so bad.

---

## Chapter 11 — The Riddle Theatre

🧩 Guild Extra — Maestro Monty's Pattern        (Riddle)

"Laaadies and gentle-Builders!" cried Maestro Monty,
throwing back the curtain.

"A drumroll, please — for a pattern hiding in plain sight!"

```python
steps = ["L", "R", "L", "R", "L", "R"]

for step in steps:
    print(step, end=" ")

print()
print("Pattern found: it's just L, R, repeating!")
```

Expected output:
```
L R L R L R 
Pattern found: it's just L, R, repeating!
```

Sir Quizzalot leaned in, very solemn. "A true knight never guesses the pattern."
He paused. "...He guesses it boldly. It's L, R. I said that first."

Monty sighed. He always says that first.

---

## Chapter 12 — Menus & Mini-Programs

🎨 Guild Extra — The Wallpaper Lever        (Art)

One box. One symbol. One line that repeats it.
That's the whole trick behind every menu border you'll ever draw.

```python
MY_PAINT = "\u2726"

print(MY_PAINT * 12)
```

Expected output:
```
✦✦✦✦✦✦✦✦✦✦✦✦
```

🎨 Hack it: change `MY_PAINT` to your own symbol — try `"="` or `"~"` —
and use it to draw the top border of your next menu.

---

## Chapter 13 — The Painter's Deck

😄 Guild Extra — Pycasso's Verdict        (Joke)

Professor Pycasso leaned over Captain Byte's shoulder
and studied a wall of broken code, deeply moved.

"A guitar string and a Python string have so much in common,"
he said. "Both of them just want to be *joined*."

Captain Byte blinked. "That's not — that has nothing to do with my bug."

"No," Pycasso agreed happily. "But look at the shape of that traceback.
Tragic. But honestly? A little beautiful."

He wandered off to go find more art in other people's errors.

---

## Chapter 14 — The Escape Room

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

## Chapter 15 — Treasure Quest v1 (capstone)

🎨 Guild Extra — The Victory Star        (Art)

One last spark, for the Builder who just shipped their first game.

```python
BOOM_FACTOR = 4
line = "*"

step = 0
while step < BOOM_FACTOR:
    spaces = BOOM_FACTOR - step
    print(" " * spaces + line)
    line = line + "**"
    step = step + 1
```

Expected output:
```
    *
   ***
  *****
 *******
```

🎨 Hack it: change `BOOM_FACTOR` to `8` and watch your victory star
grow as big as your first shipped game deserves.

---

🐉🍩 *Batch 1 complete — 15 extras, Chapters 1–15, rotation intact, every riddle and art
piece bash-verified. Batch 2 (Volume II) waits for that volume's real chapters to exist.*

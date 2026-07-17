# 😄🧩🎨 GUILD_EXTRAS.md

### The composed Guild Extras library — one file, growing batch by batch

> **Status:** Batch 1 (Volume I, Chapters 1–15) + Batch 2 (Volume II, Chapters 1–12) — 27 extras,
> composed fresh from `docs/GUILD_EXTRAS_SOURCE.md` (D-34). Never copied from the raw brainstorm.
> Every extra is re-skinned to our cast, matched to its chapter's topic where possible, and — for
> riddles and art — bash-verified with real output pasted below.
> **This is one continuous file, never split.** The rotation runs unbroken across volumes:
> Vol I Ch 15 ends on 🎨 Art, so Vol II Ch 1 opens on 😄 Joke.
> **Rotation:** 😄 Joke → 🧩 Riddle → 🎨 Art, one per chapter, from Chapter 1.
> **How to use:** drop the matching block into that chapter's Guild Extra slot (STYLE_GUIDE §4b).
> **Batch 3+** (Volumes III–IV) will grow this same file later, per the build kit's batch plan.
> **One item (Vol II Ch 1) is an original composition, not a catalog pull** — the catalog has no
> Big-O/planning gag, and `GUILD_EXTRAS_SOURCE.md` is explicit that it's a seed, not a cap. It's
> re-skinned to our cast, one screen, no code — same bar as every catalog joke. Everything else
> in both batches is a catalog item, freshly composed in-voice.

---

# 📘 Batch 1 — Volume I (Chapters 1–15)

## Volume I, Chapter 1 — Captain Byte Sets Sail

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

## Volume I, Chapter 2 — The Hungry Pizza Robot

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

## Volume I, Chapter 3 — The Age Machine

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

## Volume I, Chapter 4 — The Ninja Health Check

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

## Volume I, Chapter 5 — Rock, Paper, Scissors

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

## Volume I, Chapter 6 — The Secret Treasure

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

## Volume I, Chapter 7 — The Safe Password Checker

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

## Volume I, Chapter 8 — The Recycling Robot

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

## Volume I, Chapter 9 — The Palindrome Mirror

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

## Volume I, Chapter 10 — The Caesar Messenger

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

## Volume I, Chapter 11 — The Riddle Theatre

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

## Volume I, Chapter 12 — Menus & Mini-Programs

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

## Volume I, Chapter 13 — The Painter's Deck

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

## Volume I, Chapter 14 — The Escape Room

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

## Volume I, Chapter 15 — Treasure Quest v1 (capstone)

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

# 📗 Batch 2 — Volume II (Chapters 1–12)

## Volume II, Chapter 1 — The Map Grows

😄 Guild Extra — Oh... Query!        (Joke)

A new Navigator boards the ship, spyglass shaped like a giant letter O.

Captain Byte introduces the crew.
Lady-O-Query opens her logbook.

"Wonderful! Before we plan the whole voyage —
can I ask a quick question—"

The whole crew groans at once. **"Oh... Query!"**

She asks eleven quick questions instead of the one clean one she meant to ask.

Dragon Debug, very patiently, over his tea:
"You already have every answer you need, Navigator.
You're just asking for them one grain of sand at a time."

Lady-O-Query looks up, delighted, not even slightly offended.

"That," she says, "is exactly the kind of feedback
I'd love to gather more data on."

Somewhere in her family tree, a long time ago,
another sharp mind with a magnifying glass
once said something suspiciously similar.

---

## Volume II, Chapter 2 — The Knapsack

🧩 Guild Extra — The Lunch Box        (Riddle)

Too much loot, no pockets. Watch what one small word does to a bag.

```python
bag = ["a rusty compass"]
print("Your knapsack:", bag)

bag.append("a shiny doubloon")
print("Your knapsack:", bag)
```

Expected output:
```
Your knapsack: ['a rusty compass']
Your knapsack: ['a rusty compass', 'a shiny doubloon']
```

🕵️ Try it: `.append()` again, with anything you like.
Your knapsack never says no. It just gets heavier.

---

## Volume II, Chapter 3 — The Merchant's Wharf

🎨 Guild Extra — The Wharf Dog        (Art)

Every merchant's stall on the wharf has a dog. This one's yours to remix.

```python
EARS = " ^   ^ "
HEAD = "( o o )"
NOSE = " \\_-_/ "
TAIL = "   ~"

print(EARS)
print(HEAD)
print(NOSE)
print(TAIL)
```

Expected output:
```
 ^   ^ 
( o o )
 \_-_/ 
   ~
```

🎨 Hack it: change `TAIL` to `"  ~~~"` for a happier wag,
or swap `NOSE` for something sillier. Same four boxes. Your dog.

---

## Volume II, Chapter 4 — When Things Go Wrong

😄 Guild Extra — The Bad Liar        (Joke)

Captain Byte fed the ship a number where a word should be.
The screen turned red, top to bottom.

"Why," he groaned, "does it always turn red?
Can't it just... fail quietly? With some dignity?"

Dragon Debug shook his head, smiling.

"Programmers make terrible liars, Captain.
Every single mistake, printed out loud,
in the brightest red the terminal owns."

"That's not comforting."

"It's not meant to comfort you," said the dragon.
"It's meant to be *impossible to miss.*
An error that hides is far more dangerous
than one that shouts."

---

## Volume II, Chapter 5 — The Memory Stone

🧩 Guild Extra — BOO! Nothing Here        (Riddle)

Before the stone remembers anything, it remembers nothing at all.
Python has a word for exactly that kind of empty.

```python
save_file = None

if save_file is None:
    print("BOO! No save file here yet.")
else:
    print("Welcome back! Loading:", save_file)
```

Expected output:
```
BOO! No save file here yet.
```

🕵️ Try it: set `save_file = "chapter_5_save"` and run it again.
`None` isn't zero. It isn't empty text.
It's Python's honest way of saying *nothing has happened here yet.*

---

## Volume II, Chapter 6 — The Cartographer

🎨 Guild Extra — The World Generator        (Art)

Two small lists, and Ninja Cat can sketch a whole coastline
before you've finished your tea.

```python
import random

sky = ["cloud", "sunbeam", "star", "moon"]
ground = ["pine forest", "cliffside", "sandy cove", "rolling wave"]

print("Sky:", random.choice(sky))
print("Ground:", random.choice(ground))
```

Expected output (one real run — yours will land differently, that's the whole idea):
```
Sky: cloud
Ground: rolling wave
```

🎨 Hack it: add three more entries to `ground` — `"volcano"`, `"swamp"`, whatever you like —
and run it a few times. Two short lists. An endless map.

---

## Volume II, Chapter 7 — The Toolmakers' Guild

😄 Guild Extra — The Clean Room        (Joke)

The Toolmakers' Guild keeps every scroll on its own labelled shelf.
Captain Byte dumped his one giant scroll on the floor instead.

Dragon Debug picked it up, one line at a time.

"Python," he said, "is like a very clean room.
Move one thing two spaces to the left,
and the whole system screams about it."

"That seems... dramatic," said the Captain.

"It is," agreed the dragon. "But a clean room
is also the only kind where you can actually
*find* anything again. That's why we're about
to give every tool its own shelf."

---

## Volume II, Chapter 8 — The Bestiary

🧩 Guild Extra — The Wizard's Chest        (Riddle)

Every monster in the Bestiary lives behind one key. Guess it, and it's yours.

```python
chest = {"ruby": 50, "emerald": 80, "pearl": 20}

key = "emerald"
print("You reach for the word:", key)
print("The chest opens and gives you", chest[key], "gold pieces!")
```

Expected output:
```
You reach for the word: emerald
The chest opens and gives you 80 gold pieces!
```

🕵️ Try it: change `key` to `"pearl"` or `"ruby"` and run it again.
The chest never opens for a key it doesn't recognize —
try `"sapphire"` and see what Python says about that.

---

## Volume II, Chapter 9 — The Riddle Theatre Returns

🎨 Guild Extra — The Word-Pool Spell        (Art)

"A drumroll, please!" cried Maestro Monty. "For a spell composed
entirely by *chance!*"

```python
import random

verbs = ["Wobble", "Sparkle", "Grumble"]
nouns = ["biscuit", "kraken", "teacup"]
endings = ["until sunrise!", "or else!", "quite politely."]

print(random.choice(verbs), "the", random.choice(nouns), random.choice(endings))
```

Expected output (one real run — every run casts a different spell):
```
Sparkle the teacup until sunrise!
```

Sir Quizzalot, very solemn: "A true knight never doubts a spell he cast himself."
He pauses. "...Run it again. I want to see if it's funnier the second time."

🎨 Hack it: add your own words to any of the three lists and run it five times in a row.
Three short lists. An entire theatre's worth of nonsense.

---

## Volume II, Chapter 10 — The Standup

😄 Guild Extra — Twice As Large        (Joke)

Every morning, two minutes, the whole crew checks in.
Captain Byte, as usual, wanted to build everything at once.

"The glass is half empty," he sighed, staring at the backlog.

"Wrong problem," said Dragon Debug. "The glass isn't
half full, and it isn't half empty.

It's simply **twice as large** as it needed to be today."

Captain Byte blinked. Then crossed half the list off,
and kept only what today actually needed.

The standup took ninety seconds. A record.

---

## Volume II, Chapter 11 — Pycasso's Palette

🧩 Guild Extra — The Shout String        (Riddle)

Before the color arrives, Pycasso warms up with a smaller trick —
turning a whisper into a shout with one word.

```python
whisper = "the tangle is closer than you think"
shout = whisper.upper()

print("Quackers whispers:", whisper)
print("The ship shouts it back:", shout)
```

Expected output:
```
Quackers whispers: the tangle is closer than you think
The ship shouts it back: THE TANGLE IS CLOSER THAN YOU THINK
```

🕵️ Try it: `.lower()` does the exact opposite. Chain them —
`whisper.upper().lower()` — and see if you can guess the result before you run it.

---

## Volume II, Chapter 12 — Treasure Quest v2 (capstone)

🎨 Guild Extra — The Moving Tide        (Art)

One last piece, for the Builder whose game just grew up.
A list of steps, and a shape that seems to breathe.

```python
import time

wave_steps = [0, 1, 2, 3, 2, 1, 0]
symbol = "~"

for step in wave_steps:
    print(" " * step + symbol)
    time.sleep(0.1)
```

Expected output:
```
~
 ~
  ~
   ~
  ~
 ~
~
```

🎨 Hack it: make `wave_steps` longer — `[0, 1, 2, 3, 4, 3, 2, 1, 0]` — for a bigger swell,
or shrink the `time.sleep` for a choppier sea. Same seven lines of code.
A whole ocean, if you want one.

---

🐉🍩 *27 extras, Volumes I–II complete, one continuous rotation, every riddle and art piece
bash-verified. Batch 3 (Volume III) waits for that volume's real chapters to exist — same file,
appended, never split.*

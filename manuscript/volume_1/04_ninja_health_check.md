# Chapter 4 — The Ninja Health Check

> *"Some of the most important numbers in the world live between the whole ones."*

---

The wheel was the Captain's.

The Cliffs of Health rose up ahead —

tall, grey, and not the least bit friendly.

The ship slowed.

Then it beeped its hardest question yet:

```
To cross the Cliffs of Health,
knowing your age is not enough.
I must do maths — with your whole self.
Are you ready for the climb?
```

Captain Byte puffed out his chest.

"Ready? I've eaten a thousand pizzas.

I'm the *readiest* pirate on the sea!"

The ship, unimpressed, blinked one word:

```
Prove it.
```

---

Something moved in the rigging.

Quick.

Quiet.

The Captain barely saw it —

a shadow, a whisker, a flick of a tail —

and then, softly, it was standing on the deck.

A cat.

In a tiny black ninja hood.

She did not say hello.

Ninjas rarely do.

She simply flicked one paw,

and a small scroll spun across the deck

and landed, perfectly, at the Captain's feet.

---

Captain Byte unrolled it.

On it was a formula:

```
readiness = snack_fuel ÷ (wobble × wobble)
```

"Snack fuel!" cried the Captain. "Now *this* is my kind of maths."

Dragon Debug wandered over, tea in hand,

and read the scroll over the Captain's shoulder.

"Ah," he said. "The ship wants a real number.

Not stored. Not chosen.

*Calculated.*"

He pointed at the little signs.

"You've met these before, in school —

they just wear new clothes in Python."

> `*` means **times** (multiply).
> `/` means **divided by**.
> A program can do every sum you can — and never gets tired.

---

"So," said the dragon, "the ship needs two things from you.

How much **snack fuel** you're carrying.

And your **wobble** — how shaky your sea-legs are today."

Captain Byte cracked his knuckles.

He knew this trick now.

*Ask. Listen. Turn it into a number.*

He typed, fast and proud:

```python
snack_fuel = int(input("How much snack fuel? "))
wobble = int(input("How wobbly are your legs? "))
```

The ship asked for his snack fuel.

"Sixty!" said the Captain, typing `60`. "All pizza."

Then it asked about his wobble.

The Captain thought about the rolling sea,

the slippery deck,

his one slightly-too-full belly,

and typed: `1.5`.

The ship went **red**.

```
ValueError: invalid literal for int() with base 10: '1.5'
```

---

"BROKEN!" howled Captain Byte. "Again! I hate the cliffs!"

Ninja Cat did not move.

Dragon Debug took a slow, warm sip.

"Interesting," he said.

Which — you remember — means *lean in.*

"That growl in your chest is allowed, Captain," he said.

"Even dragons have wanted to throw a keyboard at the sea."

"It isn't broken, Captain. Read it.

You reached for `int`.

That was clever last time —

`int` is for **whole** numbers.

1, 2, 3, 60.

Nothing in between."

He set down his cup.

"But you didn't type a whole number.

You typed **one and a half.**

And `int` has no idea what to do

with the half."

The Captain stared at his `1.5`.

"...There's no *whole* way to be one-and-a-half wobbly," he admitted.

Dragon Debug smiled the good smile.

**"Excellent. Now the conversation begins."**

---

"Some numbers," said the dragon,

"live *between* the whole ones.

One and a half. Three point two. Ninety-nine point nine.

We call them **floats.**"

He wrote the fix, changing just one word:

```python
snack_fuel = float(input("How much snack fuel? "))
wobble = float(input("How wobbly are your legs? "))
```

"`float` is the tool for numbers with a **dot** in them.

The dot has a proper name — a *decimal point* —

but between us, it's just the dot

that lets a number be a little bit more,

or a little bit less,

than whole."

The Captain typed his answers again.

`60`.

`1.5`.

No red this time.

The ship simply... waited for the sum.

---

"Now the formula," said the dragon.

"Straight off the ninja's scroll."

```python
readiness = snack_fuel / (wobble * wobble)
```

"Read the brackets first — that's the rule, in maths and in Python.

`wobble * wobble` — your wobble, times itself.

*Then* the snack fuel is divided by that."

Captain Byte pressed Run.

The ship answered:

```
26.666666666666668
```

The Captain blinked.

"That's... a lot of sixes."

"It is," laughed the dragon.

"The true answer *is* that long.

But nobody needs a number

that runs off the edge of the deck."

---

"When a float gets messy," said the dragon,

"we can ask for it **rounded** —

tidied to just a few dots' worth."

```python
readiness = round(readiness, 1)
```

"`round` takes two things:

the number,

and how many digits to keep after the dot.

We asked for **1**."

The ship tried again:

```
26.7
```

"Much better," said the Captain. "A number I can wear to a party."

On the rigging rail, Ninja Cat gave the smallest nod.

From a shadow near the mast,

a familiar rubber duck watched it all.

He said nothing, of course.

Professor Quackers was *deeply* impressed by the silence of the cat.

Two masters. One conversation. No words at all.

"Quack," he offered, at last.

It was, for him, practically a speech.

---

"One thing left," said the dragon.

"A number on its own is just a number.

The ship still has to **decide** what it means."

Captain Byte grinned.

"Doors! I know doors! `if`, `elif`, `else`!"

"Now you're sailing," said the dragon.

Together they wrote the last piece —

three doors, biggest gate first,

every one of them kind:

```python
if readiness >= 25:
    print("Cliff-ready! Go, Captain!")
elif readiness >= 15:
    print("Steady — take the rope bridge.")
else:
    print("Rest first. Even ninjas nap.")
```

The Captain — sixty snacks strong — pressed Run.

The ship rang like a bell:

```
Cliff-ready! Go, Captain!
```

"HA!" he roared, and struck a pose on the rail.

"Told you. Readiest pirate on the sea."

---

"Builder — your turn," said the dragon,

turning to you.

"But not with *your* body.

Invent an adventurer.

Give them any snack fuel you like.

Any wobble at all — whole, or with a dot.

Then let the ship tell them how they'd fare on the climb."

So you did.

You made up your own hero.

You typed their numbers.

You pressed Run —

and the ship weighed them up,

did its careful maths,

and picked exactly the right door.

Whatever it said —

*charge the cliff*, *take the bridge*, or *have a nap* —

it was kind.

And it was *yours.*

Because a program that can measure

and a program that can decide

is starting to feel a lot like magic.

---

## 🐉 A riddle, before you sail on

Dragon Debug refilled his cup and turned to you.

"One question," he said. "Then we climb."

> *I'm the number that won't stay whole.*
> *A little dot splits me clean in two.*
> *Not quite one, not quite the next —*
> *I'm the in-between, and I'm true.*
>
> **What am I?**

Say it out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **`float`** — a number with a dot.

And if you got it — Builder, your program can now measure the world

as finely as it needs to.

---

## 🧰 Toolbox Card — float, operators & round

Numbers that aren't whole are **floats.**

```python
wobble = float(input("How wobbly? "))   # 1.5 is fine now
```

- `int` → whole numbers only (1, 2, 60).
- `float` → numbers with a **dot** (1.5, 3.2, 99.9).

And your program can do real maths:

`+` add · `-` subtract · `*` times · `/` divide

> Brackets go first. `(wobble * wobble)` happens
> before anything outside the brackets.

When a float gets long and messy, **tidy it:**

```python
round(26.666666, 1)   # → 26.7
```

`round` keeps only as many digits after the dot as you ask for.

---

## 🏗️ In the Real World

> Doctors, coaches, and scientists really do this —
> take a couple of measurements and divide one by another squared —
> to get a single health number. One famous one is called **BMI.**
>
> It's only ever a rough hint, never the whole story of a person.
> But the *maths* you just wrote is exactly the maths they use.

---

## 🐉 Dragon Debug's Wisdom

> *"Not everything worth measuring is whole.*
> *Learn to work in halves and hair's-breadths —*
> *and the world gets a great deal more honest."*

---

### ⭐ Achievement Unlocked

**Number Cruncher 🧮** — *Your program does real maths now. It multiplies, it divides, it works in decimals, and it tidies its answers. Give it numbers, and it will reason with them.*

---

### To be continued...

The Captain scrambled up the Cliffs of Health,

snack fuel high, wobble handled,

Ninja Cat flowing up the rock beside him

like water going the wrong way.

At the top, a fork in the path.

Two doors. One choice.

And crouched between them —

grinning, holding out three closed paws where a cat should have two —

something that wanted to play a **game.**

"Choose," it whispered.

"Rock. Paper. Or scissors.

But choose *fast* —

I never pick the same thing twice."

Captain Byte swallowed.

"How do I beat something that won't stay still?"

High above, Ninja Cat's eyes gleamed.

*Sometimes,* the moment seemed to say,

*you don't out-think chance.*

*You learn to play it.*

→ *Next: Rock, Paper, Scissors — and the magic of `random`.* ✊

---

## 😄 Guild Extra — TommyBot's Question

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

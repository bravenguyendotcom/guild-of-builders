# Chapter 5 — Rock, Paper, Scissors

> *"You cannot out-think chance. But you can invite it to play on your side."*

---

At the top of the Cliffs of Health,

the path split in two.

Two doors.

One choice.

And crouched right between them —

grinning —

was the creature from the cliffhanger.

It held out three closed paws.

Which was strange.

Because a cat only has two.

---

"Choose," it whispered.

"Rock. Paper. Or scissors.

Beat me, and a door opens.

But choose *fast* —

I never pick the same thing twice."

Captain Byte squinted.

The hood.

The whiskers.

The way it moved like water going the wrong way.

"...Wait," he said. "I *know* you."

The third paw melted into shadow.

Only two were left.

It was Ninja Cat.

Of course it was.

---

"You want to *play* me?" said the Captain, delighted.

"Easy! I'll just figure out what you'll throw,

and throw the thing that beats it. HA!"

Ninja Cat's eyes gleamed.

She threw.

He guessed.

He guessed wrong.

She threw again.

He guessed wrong again.

Every single time,

she was somewhere his brain wasn't.

"How," puffed the Captain,

"do you beat someone

you can't *predict?*"

---

Dragon Debug climbed up last,

tea somehow still warm.

He watched one round. Then two.

"Interesting," he said.

Which — you remember — means *lean in.*

"You're trying to out-*think* her, Captain.

But chance can't be out-thought.

That's what makes it chance."

He took a slow sip.

"You don't beat the ninja by being *smarter.*

You beat her by being *unpredictable too.*"

---

Captain Byte's eyes lit up.

"Then I'll make the *ship* play for me!

Computers are clever. It'll pick something sneaky!"

He typed, fast and proud:

```python
my_move = "rock"
print("I throw:", my_move)
```

He pressed Run.

`I throw: rock`

He pressed Run again.

`I throw: rock`

And again.

`I throw: rock`

Ninja Cat yawned.

She had already won three times.

---

"Ah," said Dragon Debug, gently.

"Here is a hard truth about computers, Captain.

They are wonderfully obedient.

You said 'rock.'

So it will say 'rock' —

today, tomorrow, a thousand times,

exactly the same."

He set down his cup.

"That's a *superpower* most of the time.

But right now?

The most obedient player

is the easiest one to beat."

The Captain slumped. "So the computer can't be surprising?"

"It can," said the dragon, smiling the good smile.

**"But only if we hand it a pinch of chance.**

**And chance lives in a toolbox we haven't opened yet."**

---

"Python keeps some tools switched *off* until you ask for them,"

said the dragon.

"Not because they're dangerous.

Just to keep your ship light.

You carry only the tools you need."

"The tool for chance is called **`random`**.

To wake it up, you **import** it —

you carry it up from the hold and onto the deck."

Captain Byte, never one to wait, dived straight for the fun part:

```python
ninja = random.choice(["rock", "paper", "scissors"])
```

He pressed Run.

The ship went **red**.

```
NameError: name 'random' is not defined.
Did you forget to import 'random'?
```

---

"OH, COME ON!" howled the Captain.

But then he stopped.

He looked closer.

"...Wait. I've met this red before.

Chapter one. The very first bug."

Dragon Debug's eyebrows rose, impressed.

"You *have.* A **`NameError`** —

the program meeting a word it doesn't know yet.

Last time, the fix was to introduce the name.

This time?"

The Captain grinned.

He read the ship's own hint out loud:

*"...Did you forget to import 'random'?"*

"The ship is *telling* me the fix!"

**"Excellent,"** said the dragon. **"Now the conversation begins."**

---

One line, right at the top.

That was all it took:

```python
import random

ninja = random.choice(["rock", "paper", "scissors"])
```

"`import random`," said the dragon,

"brings the chance-tool onto the deck.

And **`random.choice`** reaches into a hat —

that list of three moves —

and pulls one out.

You never know which.

*Neither does the computer, until it looks.*"

Captain Byte pressed Run.

`scissors`

Again.

`rock`

Again.

`paper`

He laughed out loud.

"It's alive! It's finally *surprising!*"

High on the rail, Ninja Cat's ears twitched.

For the first time, she looked... interested.

---

"Now," said the dragon,

"we throw *our* move,

let the ninja throw hers,

and ask the one question that decides it all:

**are they the same, or not?**"

Captain Byte remembered.

"Doors! `if`, `elif`, `else` — from the Age Machine!"

"And a check we've used before," nodded the dragon.

"`==` — the little twin

that asks *are these two exactly equal?*"

They wrote it together:

```python
import random

moves = ["rock", "paper", "scissors"]

you = input("Rock, paper, or scissors? ")
ninja = random.choice(moves)

print("You chose:", you)
print("Ninja chose:", ninja)

if you == ninja:
    print("A tie! Nobody wins. Go again.")
elif you == "rock" and ninja == "scissors":
    print("You win! Rock smashes scissors.")
elif you == "paper" and ninja == "rock":
    print("You win! Paper wraps rock.")
elif you == "scissors" and ninja == "paper":
    print("You win! Scissors cut paper.")
else:
    print("Ninja wins this round.")
```

---

There's one small new word hiding in there.

Did you spot it?

**`and`.**

It's exactly what it sounds like.

*You win when you threw rock* **and** *the ninja threw scissors.*

**Both** must be true.

If only one is true, the door stays shut.

(You'll meet `and` properly later, in the Safe Password mission.

For now, just read it the way you'd say it out loud.)

---

Captain Byte typed `rock` and pressed Run.

The ship thought.

The ninja reached into her hat.

```
You chose: rock
Ninja chose: scissors
You win! Rock smashes scissors.
```

"YESSS!" The Captain leapt so high he nearly went over the cliff.

The **left door** swung open with a happy *click.*

He played again — and lost.

He played again — a tie.

He played again — won.

And that was the whole point.

Nobody could say what came next.

Not the Captain.

Not the ninja.

Not even the ship.

That's what made it a *game.*

---

From a shadow near the doorway,

a small rubber duck watched the paws blur and the doors swing.

He had, of course, no idea how to play.

He had no hands.

Professor Quackers considered this deeply.

"Quack," he decided.

It meant: *the wisest move is sometimes to simply enjoy the show.*

---

"Builder — your turn," said Dragon Debug,

turning to you.

"Wake up the chance-tool.

Fill the hat with three moves.

Then step up and face the ninja yourself."

So you did.

You typed `import random` at the very top.

You reached into the hat with `random.choice`.

You threw your move.

The ninja threw hers —

and not even *she* knew which

until the paw opened.

Sometimes you won.

Sometimes you didn't.

But every single round was *alive* —

because you'd taught your program

the one thing obedient machines never had before:

**the gift of surprise.**

---

## 🐉 A riddle, before you sail on

Dragon Debug refilled his cup and turned to you.

"One question," he said. "Then we pick a door."

> *I'm the pinch of chaos you keep in a jar.*
> *You must call me by name before I'll appear.*
> *Roll me for dice, or a card, or a coin —*
> *and no two of my answers need ever be near.*
>
> **What am I?**

Say it out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **`random`** — the tool of chance.

And if you got it — Builder, your programs can now *surprise* you.

That's how games are born.

---

## 🧰 Toolbox Card — random & ==

Some tools stay in the hold until you **import** them:

```python
import random
```

Then you can reach into a hat and pull one out:

```python
move = random.choice(["rock", "paper", "scissors"])
```

- `import random` → wakes up the chance-tool. Do it once, at the top.
- `random.choice(a_list)` → picks **one** item, unpredictably.

And the twin that checks *are these exactly the same?*

```python
if you == ninja:
    print("A tie!")
```

- `=` (one) **stores** a value in a box.
- `==` (two) **asks** if two things are equal. Never mix them up.

> New little word: **`and`** — *both* sides must be true.

---

## 🏗️ In the Real World

> A ready-made toolbox you **import** is called a **module** —
> and a whole shelf of them is a **library**.
>
> Real Builders almost never start from nothing.
> They stand on tools other Builders already made —
> and `random` is one every game programmer knows by heart.

---

## 🐉 Dragon Debug's Wisdom

> *"An obedient machine repeats.*
> *A great Builder knows when to hand it a pinch of chance —*
> *and let the program surprise even its maker."*

---

### ⭐ Achievement Unlocked

**Chance Dancer 🎲** — *Your program isn't predictable any more. It can reach into a hat, pull out a surprise, and play a real game. You imported your first tool — and taught a machine how to be unexpected.*

---

### To be continued...

The left door opened onto a narrow stair,

winding down into the dark.

At the bottom sat a chest.

Iron-banded. Enormous. Locked.

No keyhole.

Just a single glowing slot,

and above it, six words:

```
I am thinking of a number.
```

Captain Byte cracked his knuckles.

"A number? I *love* numbers now! I'll just guess it!"

He typed `50`.

The chest rumbled:

```
Too low.
```

He typed `75`.

```
Too high.
```

"...How many guesses do I *get?*" the Captain asked, slowly.

From the shadows, Ninja Cat tilted her head,

as if to say:

*How many can you take?*

Because guessing once is luck.

Guessing *cleverly, again and again* —

that's something a program can do

better than any pirate alive.

→ *Next: The Secret Treasure — and the magic of loops.* 🔁

# Chapter 6 — The Secret Treasure

> *"Guessing once is luck. Guessing again, and again, and again — cleverly — is a program."*

---

The stair wound down into the dark.

Round and round.

Until it stopped at a chest.

Iron-banded.

Enormous.

Locked.

No keyhole.

Just one glowing slot,

and six words carved above it:

```
I am thinking of a number.
```

---

Captain Byte cracked his knuckles.

"A number? Ha! I love numbers now.

Watched me do the maths on the cliffs, didn't you?

I'll just *guess* it."

He typed `50`.

The chest rumbled.

```
Too low.
```

He typed `75`.

```
Too high.
```

He typed `60`.

```
Too high.
```

He typed `55`.

```
Too low.
```

Captain Byte stopped.

His fingers hovered.

"...How long is this going to *take?*"

---

Dragon Debug arrived at the bottom of the stair,

tea somehow still warm.

He watched the Captain type another guess.

And another.

And another.

"Interesting," he said.

Which — you remember — means *lean in.*

"Captain. Look at what your hands are doing."

The Captain looked.

Type a guess. Read the chest. Type a guess. Read the chest.

The *same steps.*

Over.

And over.

"You," said the dragon gently,

"have been doing the computer's favourite chore *by hand.*"

---

"Repeating?" said the Captain.

"Repeating," said the dragon.

"A machine will do the same thing

a hundred times,

a thousand times,

a million times,

and never once get bored,

never once make a typo,

never once ask for a pizza break."

The Captain looked wounded. "I would never ask for—"

His stomach growled.

"...often," he finished.

---

"The tool for *keep doing this* is called a **loop**,"

said the dragon.

"And the loop we want here has a beautiful, honest name.

It's called **`while`**.

You read it exactly how you'd say it out loud:

***while*** *the chest is still locked* —

*keep guessing.*"

---

"But first," said the dragon,

"the chest needs a number to hide.

Remember the chance-tool you woke up on the cliffs?"

The Captain grinned. "`import random`!"

"Its cousin lives right next door.

`random.choice` reached into a hat of *words.*

**`random.randint`** rolls a die between two *numbers.*"

```python
import random

secret = random.randint(1, 100)
```

"`randint(1, 100)`,"

said the dragon,

"picks one whole number

from 1 to 100.

Even the chest doesn't know which,

until it looks."

---

Captain Byte, never one to wait,

dived for the loop.

He typed fast:

```python
guess = int(input("Guess my number (1-100): "))

while guess != secret:
    print("Nope! Keep trying!")
```

"There's a new little sign in there," said the dragon.

"`!=`.

It's the *opposite* of the twin `==`.

`==` asks *are these the same?*

`!=` asks *are these different?*

So this reads:

***while*** *the guess is* ***not*** *the secret — keep going.*"

"PERFECT," roared the Captain,

and slammed Run.

---

```
Guess my number (1-100): 40
Nope! Keep trying!
Nope! Keep trying!
Nope! Keep trying!
Nope! Keep trying!
Nope! Keep trying!
Nope! Keep trying!
Nope! Keep trying!
```

The words kept coming.

Faster.

Filling the screen.

They did not stop.

They were *never* going to stop.

"WHY IS IT DOING THAT?!" the Captain yelped,

stabbing at the keyboard.

Somewhere in the dark, Ninja Cat's ears went flat.

---

Dragon Debug did not panic.

He took a slow sip of tea.

"That hot flash of *why-is-it-doing-that* you just felt?

The stabbing at the keys?

Every Builder feels it," he said.

"I felt it myself, long ago,

over a loop very much like this one.

It isn't a sign that you're *bad* at this.

It's a sign that you're *doing* this.

There's an old Guild saying for a day like today —

*that's not failure. That's called Tuesday.*"

He set his cup down, then picked the thread back up.

"Interesting," he said.

"You have just met one of the most famous bugs in all of programming.

An **infinite loop.**

A loop with no way out."

He set down his cup.

"Look closely, Captain.

You asked for the guess *once* —

up above, before the loop.

Then inside the loop?

Nothing about the guess ever *changes.*

So `guess != secret` stays true forever.

The chest asked a question.

You never let yourself answer it again."

**"Excellent,"** he added,

with the good smile.

**"Now the conversation begins."**

---

Here is the rule the Captain learned that day,

the rule that tames every loop:

> **Every loop needs a way out.**
>
> Something *inside* the loop
> must be able to change —
> so the question can one day answer *"stop."*

The fix was small.

Move the guess *inside* the loop.

Now every turn asks for a **fresh** guess:

```python
import random

secret = random.randint(1, 100)
guess = 0

while guess != secret:
    guess = int(input("Guess my number (1-100): "))
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print("You got it!")
```

---

"One quiet trick," said the dragon,

pointing at the top.

"`guess = 0`.

The secret is somewhere from 1 to 100.

So 0 is a number the answer can *never* be.

We start the guess there on purpose —

so the very first check is always *different,*

and the loop always runs at least once."

The Captain nodded slowly.

He typed `50`.

`Too low.`

`75`.

`Too high.`

`62`.

`Too high.`

`56`.

The chest went still.

Then it *sang.*

```
You got it!
```

Iron bands unlatched, one by one.

---

But Captain Byte wasn't cheering yet.

He was frowning at the screen,

remembering his own question from the top of the stair.

"Dragon... how many guesses did that *take* me?"

"Ah," said the dragon, eyes twinkling.

"Now *that* is a real Builder's question.

And a loop can answer it —

if we give it a **counter.**"

---

"A counter is just a box,"

said the dragon,

"that keeps a tally.

We start it at zero.

Then, every time round the loop,

we bump it up by one."

```python
attempts = 0

# ...inside the loop:
attempts = attempts + 1
```

The Captain squinted.

"Wait. `attempts = attempts + 1`?

That's the same word on *both* sides.

How can a box equal itself... plus one?"

"Read it *right to left,*" said the dragon.

"First, look *inside* the box: `attempts + 1`.

*Then* put that new total *back* in the box.

Take what you had.

Add one.

Store it again.

Every lap, the tally climbs."

---

Put it all together,

and the chest could finally count:

```python
import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess my number (1-100): "))
    attempts = attempts + 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print("You got it in", attempts, "guesses!")
```

The Captain played it once more.

```
You got it in 4 guesses!
```

"FOUR!" he crowed. "I did it in four!"

He puffed up like a very proud, very hungry pigeon.

---

From a ledge in the dark,

a small rubber duck had watched the whole thing —

the endless loop, the panic, the counter, the win.

Professor Quackers had, of course,

said nothing the entire time.

He had simply *watched.*

And somehow, watching him watch

had helped the Captain think.

"Quack," said Professor Quackers.

It meant: *a good Builder counts. A great Builder wonders what the count means.*

---

"Builder — your turn," said Dragon Debug,

turning to you.

"Roll a secret with `random.randint`.

Start your guess at zero.

Loop `while` it isn't the secret.

Nudge higher, nudge lower.

Bump the counter every lap.

And when you win —

see how few guesses it took."

But TommyBot didn't wait to be told twice.

He was already reaching for the keyboard —

already rolling a secret,

already typing the loop from memory,

lips moving as he worked it out.

Dragon Debug watched him go,

and — just for a heartbeat —

didn't need to say a single thing.

He found he rather liked that.

So you did it too.

And the first time your loop ran forever,

you didn't panic.

You smiled the good smile.

You found the way out.

Because now you knew the secret of loops:

**they only run wild when nothing inside them changes.**

---

## 🥋 A door you weren't shown

The iron bands hung loose now.

The lid could be lifted any moment.

But Dragon Debug didn't reach for it.

He turned, instead, toward a stretch of the dark

the torchlight had never quite reached.

"Before we open it," he said,

"there's a room down here I don't show many Builders.

You just earned the way in."

He pressed a claw to the cold stone —

and a low wooden door swung open

onto a warm, quiet hall

that didn't seem to belong to the cave at all.

Lantern light. Worn desks.

And the unmistakable smell of tea.

---

"This," said the dragon,

"is the **Typing Dojo.**

Out there, in the story, I *teach* you things.

In here?

I teach you nothing at all.

In here, you just **type.**

Real code. For the pure joy of it.

Faster. Cleaner. Sharper —

the way a drummer practises rolls.

Not to perform.

Just to keep the hands awake."

TommyBot stepped in, eyes wide.

On the nearest desk, a little program glowed.

He knew it at once.

"Hey — that's the machine we just built!

The guessing game!"

"Mm." The dragon sipped. "Your very first mission.

You already know how to type it.

That's rather the point."

---

High in the rafters, something *shifted.*

Something with a great many tentacles.

Ten, if you cared to count —

and TommyBot suddenly, very much, did.

It uncurled one lazy coil,

sniffed the air for sloppy typing,

and waited.

"Ah," said Dragon Debug,

not bothering to look up.

"That would be **The Tangle.**

A Typo-Squid.

It feeds on messy keys.

Every typo you leave behind

is one more coil around your program."

He waved a claw, vaguely.

"Dreadful nuisance, that squid.

One of these days I really must deal with it."

He did not, in any way,

sound like a dragon who would ever deal with it.

---

"So how do you beat it?" TommyBot whispered.

"You don't out-*run* it," said the dragon.

"Nothing out-runs a squid.

You out-*type* it.

Type clean enough, and something odd happens.

The Tangle doesn't lose, exactly.

It just gets... **bored.**

Bored, and a little impressed.

And off it slinks, to go find a messier Builder."

On his cushion by the door,

Professor Quackers looked at the dragon.

A long look. A knowing one.

The dragon looked very hard at his tea.

Quackers said nothing.

Quackers always knows.

Quackers never tells. 🦆

---

"There are two easy ways in, to begin," said the dragon.

"The first is the simplest thing in the world.

Type the program. Run it. Play.

Slice your caps clean — that's the whole art of it.

The second is sneakier.

I leave a few *typos* in a copy of the code,

and you turn detective.

Nothing broken but the spelling.

Find the slips. Fix them."

TommyBot's eyes drifted past him,

to where the hall ran back into shadow —

more doors, older, stranger,

each one shut.

"And *those?*"

For once, Dragon Debug didn't explain.

He only smiled,

and took a slow sip.

"Those," he said, "are for another day.

Some doors are better left as questions."

---

He nudged the low door shut behind them.

The warm hall dimmed away.

And the chest sat waiting in the dark —

bands loose, lid trembling, ready.

"Now then," said Dragon Debug.

"Where were we?"

---

## 🐉 A riddle, before you sail on

Dragon Debug refilled his cup.

"One question," he said. "Then we open the chest properly."

> *I never grow tired, I never grow bored.*
> *I'll do the same task till you tell me it's done.*
> *But leave me no exit, no door, no way out —*
> *and I'll run till the end of the world, having fun.*
>
> **What am I?**

Say it out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **a loop** — the tool of *keep going.*

And the "way out" it warns you about?

That's the thing every good loop must have.

---

## 🧭 A whisper from the dark (bonus wonder)

Ninja Cat padded out of the shadows

and looked at the Captain's four-guess win.

Then she looked at the chest.

Then back at him.

As if to ask a question without a single word:

*Why did you start at 50?*

Think about it, Builder.

The chest hides a number from 1 to 100.

Guess **50** — the middle —

and whatever the chest says,

you throw away *half* the numbers at once.

Too low? Forget 1–50. Aim for the middle of what's left.

Too high? Forget 50–100. Same trick.

Halve.

Halve again.

Do it cleverly, and you can corner *any* number from 1 to 100

in **seven guesses or fewer.**

Every time.

You don't have a name for that trick yet.

You will.

For now — just notice how good it feels

to guess like a Builder instead of a gambler.

---

## 🧰 Toolbox Card — while, !=, randint & the counter

**The loop** — *keep doing this while something is true:*

```python
while guess != secret:
    guess = int(input("Guess: "))
```

- `while` → repeats the indented block, over and over.
- The block runs **while** the question is true.
- **Every loop needs a way out** — something inside must be able to change.

**The new sign:**

- `==` → *are these the same?*
- `!=` → *are these different?* (the opposite twin)

**Chance's cousin:**

```python
secret = random.randint(1, 100)   # a whole number, 1 to 100
```

**The counter** — *a box that tallies:*

```python
attempts = 0
attempts = attempts + 1   # take it, add one, put it back
```

---

## 🏗️ In the Real World

> Real Builders write **loops** every single day —
> to check every email, every player, every row in a file.
>
> And every Builder alive has made an **infinite loop** by accident.
> The seniors too. It's a rite of passage, not a failure.

---

## 🐉 Dragon Debug's Wisdom

> *"A machine's gift is not that it's clever.*
> *It's that it never tires.*
> *Hand it the boring, endless work —*
> *and save your own mind for the clever part."*

---

### ⭐ Achievement Unlocked

**Loop Weaver 🔁** — *You taught a program to repeat — and, just as importantly, to* ***stop.*** *You rolled a secret, hunted it down with a loop, counted your own guesses, and stared an infinite loop in the eye without blinking. Machines do the tireless work now. You do the thinking.*

---

### To be continued...

The iron bands fell away.

The lid of the chest creaked open.

Captain Byte leaned in, eyes huge,

expecting gold.

There was no gold.

Inside lay a single heavy door —

a door with no handle,

only a glowing keypad

and a message that pulsed in the dark:

```
You found the treasure.
Now prove you can guard it.
Set a password. Make it strong.
```

Captain Byte laughed. "Easy! My password is `pizza`."

The keypad buzzed, unimpressed:

```
Too short. Too simple. Too guessable.
```

"...Rude," said the Captain.

Dragon Debug sipped his tea.

"The chest is right, you know.

Guessing a secret is one skill.

*Guarding* one is another.

A weak password is a door with no lock at all."

High above, Ninja Cat's eyes narrowed —

the look of someone who has picked a great many locks.

*A guard,* the moment seemed to say,

*is only as strong as the questions it asks.*

→ *Next: The Safe Password Checker — and the art of asking many questions at once.* 🔐

---

## 🥋 Typing Dojo

*A small sign hangs by that low wooden door. You don't have to open it. The story's finished — the chest is cracked, the next adventure is already calling. This part is just here, if you want it. Pure play. No story is lost if you walk right past.*

**Guess the Number** — Dragon Debug's very first mission.

You already built this machine.

Now type it clean, from the top, and play it for real.

**Type this. Run it.**

```python
# Guess the Number

import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess my number (1-100): "))
    attempts = attempts + 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print("You got it in", attempts, "guesses!")
```

**Expected output** — *your secret is random, so your numbers won't match this exactly, but it will* ***feel*** *like this:*

```
Guess my number (1-100): 50
Too high.
Guess my number (1-100): 25
Too low.
Guess my number (1-100): 37
Too low.
Guess my number (1-100): 43
Too high.
Guess my number (1-100): 40
Too low.
Guess my number (1-100): 41
Too low.
Guess my number (1-100): 42
You got it in 7 guesses!
```

If your screen looks like that — you did it. 🥋

---

**🕵️ Conan's Challenge** *(optional — only if your eyes are sharp)*

The Guild keeps another copy of this same machine...

except **three typos** slipped into it.

Nothing is broken but the spelling.

Type it, run it — and Python hands you your very first clue:

```
NameError: name 'secrit' is not defined. Did you mean: 'secret'?
```

**Excellent. Now the conversation begins.**

Two more slips are still hiding.

Find them the same way. 🦑

---

🐉 *Dragon Debug sips his tea.* *"Interesting."*

---

## 🎨 Guild Extra — The Chest-Builder

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

# Chapter 3 — The Age Machine

> *"A number just sits there — until you teach it to matter."*

---

Lunch was over.

Six slices, correctly counted.

Captain Byte leaned back, happy, and reached for the wheel.

The ship stopped him.

Not with a hand — it doesn't have one —

but with a question, glowing on the screen:

```
You must be old enough to take the wheel.
How old are you?
```

"Old enough!" said Captain Byte.

He typed a number and pressed Run.

Nothing happened.

The ship just... waited.

---

Dragon Debug looked up from his tea.

"It asked your age," he said.

"You gave it a number. Good.

But knowing a number

and *doing something* with a number

are two different things."

He set the cup down.

"Right now the ship knows you're a number old.

It just doesn't know what that number *means* yet."

Captain Byte frowned.

"So how do I teach it to... decide?"

Dragon Debug smiled the smile he saves for the good part.

"You give it a fork in the road."

---

"Imagine a door," said the dragon.

"On the door is a question.

If the answer is **true**, the ship walks through.

If it's **false**, the ship walks past."

He wrote it out, slow and clear:

```python
age = int(input("How old are you? "))

if age >= 18:
    print("Take the wheel! The ship is yours.")
```

"See the `>=`?" said the dragon.

"It means *this much, or more.*

`age >= 18` asks one simple thing:

*Is your age eighteen or bigger?*

The answer can only ever be **true** or **false**."

> *(Somewhere in the Guild, a tiny knight keeps two flags —*
> *a green one for TRUE, a red one for FALSE.*
> *You'll meet him properly one day. Today, the ship raised them on its own.)*

---

Captain Byte, who has eaten roughly a thousand pizzas

and is therefore *very* much over eighteen,

typed his age and pressed Run.

The ship lit up:

```
Take the wheel! The ship is yours.
```

"YES!" he roared, spinning the wheel like a birthday present.

"Builder — you try!"

TommyBot's hands were already on the keys.

He didn't wait to be shown this time —

he'd watched how the door worked,

and he wanted the latch himself.

So you did.

You typed *your* age.

You pressed Run.

And the ship said...

nothing.

Silence.

The kind Professor Quackers would be proud of.

"It's broken!" said Captain Byte.

---

Dragon Debug took a long, calm sip.

"Interesting," he said.

Which, you'll remember, means:

*you are about to learn something.*

"That little jolt of *it's broken*?

Every Builder feels it.

I felt it too, once —

more times than I've had cups of tea."

"It isn't broken. Look closely.

You wrote what to do when the answer is **true**.

Take the wheel. Lovely.

But you never told it what to do when the answer is **false**."

He shrugged, gently.

"So when your age wasn't eighteen or more,

the ship did the only honest thing it could.

It did *nothing at all*."

Captain Byte opened his mouth to complain.

The dragon held up a finger.

**"Excellent. Now the conversation begins."**

---

"Every door needs a *back* as well as a front," said the dragon.

"The word for 'in every other case' is `else`."

```python
age = int(input("How old are you? "))

if age >= 18:
    print("Take the wheel! The ship is yours.")
else:
    print("Not yet, sailor. Back to training.")
```

"`else` asks no question," said the dragon.

"It's the catch-all.

*If none of the doors above opened — this one always will.*"

You ran it again.

This time the ship answered you.

No more silence.

"Better," said Captain Byte. "But..."

He squinted.

"My little cousin is four.

If *she* types her age, she gets the same message I do?

'Back to training'?

She can barely reach the keyboard!"

---

"Now you're thinking like a Builder," said the dragon, pleased.

"Two doors weren't enough.

Some questions have a *middle*."

"For that," he said,

"we add a door in between.

Its name is `elif` —

short for *else, if.*

It means: *or else, check THIS instead.*"

```python
age = int(input("How old are you? "))

if age >= 18:
    print("Take the wheel! The ship is yours.")
elif age >= 12:
    print("Not the wheel yet — but old enough to start learning!")
else:
    print("Too young to drive. Never too young to build!")
```

Three doors now.

Not one. Not two. Three.

"Python reads them from the top," said the dragon.

"It walks through the **first** door that's true —

and skips all the rest.

Order matters. Always check the biggest gate first."

---

You typed your age one more time.

You pressed Run.

The ship thought for half a heartbeat —

comparing, choosing —

and lit up just for you:

```
Not the wheel yet — but old enough to start learning!
```

Captain Byte gasped.

"It picked the *middle* door!

The ship knew exactly who you were!"

He beamed at you like you'd hung the moon.

"It believes in you, Builder.

It's already saving you a seat at the wheel."

---

On his little shelf, a small rubber duck watched the whole thing.

The silence. The `else`. The three doors.

He said nothing, of course.

Professor Quackers rarely does.

"Quack," he offered, at last.

Somehow, it sounded like *well done.*

---

## 🐉 A riddle, before you sail on

Dragon Debug refilled his cup and turned to you.

"One question," he said. "Then we sail."

> *I stand at a fork where two paths divide.*
> *You hand me a question — I check what is true.*
> *If yes, I go one way. If no, the other.*
> *I never freeze up. I always choose.*
>
> **What am I?**

Say it out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **`if`** — a decision.

And if you got it — Builder, your program can now *make up its own mind.*

---

## 🧰 Toolbox Card — if / elif / else

This is how a program **chooses.**

```python
if age >= 18:
    print("Take the wheel!")
elif age >= 12:
    print("Time to start learning!")
else:
    print("Never too young to build!")
```

- **`if`** — asks a question. If the answer is **true**, run its lines.
- **`elif`** — *"or else, check this instead."* Add as many as you need.
- **`else`** — the catch-all. No question. Runs when nothing above did.

One rule to remember forever:

> Python takes the **first** true door and skips the rest.
> So check the biggest gate first.

Its cousins live here too:

`>=` (this or more) · `<=` (this or less) · `==` (exactly equal) · `>` · `<`

---

## 🏗️ In the Real World

> Every choice a program makes is a **condition** —
> a question that is only ever true or false.
>
> Deciding which lines run, and when, is called **control flow**.
>
> Every menu, every "Are you sure?", every game-over screen
> is just an `if` wearing a costume.

---

## 🐉 Dragon Debug's Wisdom

> *"A program that cannot choose can only obey.*
> *Teach it to ask one true question —*
> *and you've taught it to think."*

---

### ⭐ Achievement Unlocked

**Decision Maker 🧭** — *Your program doesn't just run and talk any more. Now it chooses. Hand it a question, and it will pick the right path — all on its own.*

---

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

### To be continued...

The wheel was the Captain's now.

He spun it once, twice, grinning like a kid on a snow day.

Then the ship beeped —

a new kind of question, harder than the last:

```
To cross the Cliffs of Health, I need more than your age.
I must do maths with your whole body.
```

Captain Byte blinked.

"My... *body?*"

High in the rigging, something moved.

Quiet.

Quick.

Watching.

→ *Next: the Ninja Health Check.* 🥷

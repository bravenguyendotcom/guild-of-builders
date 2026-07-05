# Chapter 2 — The Hungry Pizza Robot

> *"A box remembers what you put in.*
> *A great program lets someone else do the putting."*

---

Captain Byte's stomach growled again.

Louder this time.

Loud enough that a seagull left.

"Right," he announced. "Treasure can wait five minutes.

A captain sails better on a full stomach."

He marched down to the ship's kitchen —

a wonderful, clanking machine of pots and dials —

and slapped a big red button marked **COOK**.

---

The Hungry Pizza Robot whirred to life.

Lights blinked.

Steam hissed.

And then it stopped, and blinked one word at him:

*How many?*

Captain Byte stared.

"How many *what?*"

*How many slices?* blinked the robot.

The Captain threw up his hands.

"How should the ship know? I haven't *told* it yet!"

---

A familiar puff of steam curled across the kitchen.

The smell of tea arrived first, as it always does.

"Interesting," said Dragon Debug.

Captain Byte spun around. "It's *your* fault, isn't it. You taught the ship to be nosy."

"I taught the ship to **ask**," said the dragon, gently.

"Last time, remember, *you* filled the box yourself."

He was right.

Last time, the Captain had typed the number in with his own hands:

```python
pizza_slices = 4
```

A box named `pizza_slices`, with `4` tucked inside.

But a kitchen can't work that way forever.

---

"Think about it," said Dragon Debug, sipping.

"What if it's not you cooking?

What if it's a different sailor, on a different day, who wants a different lunch?

You can't sneak down here and re-type the number for every single person."

Captain Byte frowned. "So the ship has to... find out?"

"The ship has to **ask**," said the dragon.

"And then it has to *listen*."

Captain Byte's eyes went wide.

"The ship can **listen?**"

---

Here is the brand-new trick, Builder.

It has a name: `input`.

```python
name = input("What's your name, Builder? ")
```

Read it the way the dragon does:

> Ship — **ask** the question in the quotes.
> Wait for a person to type an answer.
> Then take whatever they typed
> and drop it into the box called `name`.

The ship prints the question.

It waits.

It listens.

And it remembers.

---

Go on — try it yourself.

Type **your** name when it asks.

Then let the ship say hello back:

```python
name = input("What's your name, Builder? ")
print("Ahoy,", name, "— welcome aboard!")
```

If you typed *Teppy*, the ship answers:

```
Ahoy, Teppy — welcome aboard!
```

The ship just spoke to **you.**

By name.

That box wasn't filled by the Captain this time.

It was filled by *you.*

---

Captain Byte was delighted.

"It knows my name AND it can cook? Best ship ever!"

"So let's feed it," said the dragon. "Ask it your question."

The Captain cracked his knuckles and typed:

```python
slices = input("How many slices, Captain? ")
```

The robot asked.

The Captain answered: **3**.

The robot remembered.

"Three glorious slices," sighed Captain Byte.

Then his eyes lit up with a *dangerous* idea.

---

"Wait," he whispered.

"If the ship can remember 3 slices...

can it give me **double?**"

Before anyone could stop him, he typed:

```python
print("Double that!", slices * 2)
```

He pressed Run.

He held his breath.

The robot beeped, proud as anything, and announced:

```
Double that! 33
```

Silence.

Captain Byte blinked.

"...Thirty. Three. Slices."

A slow grin spread across his face.

"**BEST. SHIP. EVER.**"

---

Dragon Debug did not grin.

He just took a long, calm sip.

"Interesting," he said.

Which, in Guild language, you'll remember means:

*you are about to learn something.*

"Captain. You asked for double 3.

The ship gave you 33.

Does that look like doubling to you?"

Captain Byte's grin wobbled.

"...it looks like the 3 got a friend."

"It did," said the dragon. "And here is why."

---

"When the ship **asks** a question with `input`,

it always hands back **text** —

even when the text *looks* like a number."

He set down his tea.

"You didn't give the ship the number 3.

You gave it the little written symbol `"3"` — like a word.

And doubling a *word* doesn't make it bigger.

It just writes it out twice."

`"3"` doubled becomes `"33"`.

Not maths.

Just... two threes, holding hands.

---

Captain Byte groaned. "So there's no extra pizza?"

"There is no extra pizza," agreed the dragon.

But he was smiling now.

Because this is the good part.

"You found a real bug, Captain.

A famous one. Every Builder meets it."

He paused, and his voice went softer.

"I met it too, once. Long ago.

I was *sure* the computer was broken.

It wasn't. I just hadn't learned to listen yet."

He said it kindly.

No shame in it at all.

"A bug isn't the end of anything."

He looked the Captain in the eye.

**"Excellent. Now the conversation begins."**

---

TommyBot had been quiet in the doorway, working something out.

*(TommyBot is you, remember — the one who learns by asking.)*

"So we have to *tell* it," TommyBot said slowly.

"That the words are really a number."

Dragon Debug turned.

Something in his face changed — the look of a teacher who has just been *met halfway.*

"Now," he said. "You're building."

---

"To fix it," the dragon went on,

"we tell the ship one small, clear thing:

*this text is actually a number.*

We wrap it in `int`."

```python
slices = int(input("How many slices, Captain? "))
print("Double that!", slices * 2)
```

`int` means *integer* — a plain, whole number.

It takes the written `"3"`

and turns it into the true number `3`,

the kind you can actually do maths with.

The Captain typed 3 again.

This time the ship answered:

```
Double that! 6
```

"SIX!" cried Captain Byte. "Now *that's* a lunch."

---

From the corner of the kitchen, on a little shelf beside the flour,

sat a small rubber duck.

He had watched the whole thing.

The double. The 33. The fix.

He said nothing.

Professor Quackers rarely does.

"Quack," he offered, eventually.

Somehow, it settled the matter.

---

## 🐉 A riddle, before you sail on

Dragon Debug refilled his cup and turned to you.

"One question," he said. "Then lunch."

> *I open my mouth and I ask you something.*
> *I wait. I don't rush. I don't guess.*
> *Whatever you type, I hand to your program —*
> *though I always hand it as text, more or less.*
>
> **What am I?**

Say it out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **`input`.**

And if you got it — Builder, your program can now *talk with people.*

That changes everything.

---

## 🧰 Toolbox Card — input

`input` is how your program **asks** — and **listens**.

```python
answer = input("Your question here ")
```

- It shows your question.
- It waits for a person to type.
- It drops their answer into a box (a variable).

One catch, worth remembering forever:

> `input` always gives you **text.**

Need a number to do maths with?

Wrap it: `int(input("How many? "))`

---

## 🏗️ In the Real World

> Anything a program gets from a person is called **input**,
> and the person typing it is the **user**.
>
> You just wrote a program that has a real conversation with a user —
> the same thing every app on your phone is doing all day long.

---

## 🐉 Dragon Debug's Wisdom

> *"Ask clearly. Listen carefully.*
> *And remember — what people type is words, until you tell it to be a number."*

---

### ⭐ Achievement Unlocked

**Conversation Starter 💬** — *Your program can now ask a question, listen to a real person, and answer them back. It doesn't just run any more. It talks.*

---

### To be continued...

Lunch was excellent. (Six slices. Correctly counted.)

But as Captain Byte licked his fingers, the ship blinked a new question:

*You must be old enough to take the wheel. How old are you?*

The Captain answered.

And the ship went quiet for a moment —

thinking, *comparing*, **deciding**.

Because knowing a number is one thing.

*Making a choice* with it is a brand-new kind of magic.

→ *Next: the Age Machine.* ⏳

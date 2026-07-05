# Chapter 1 — Captain Byte Sets Sail

> *"A good pirate remembers where the treasure is.*
> *A great pirate teaches the ship to remember it for him."*

---

The morning smelled like salt, adventure, and — faintly — pizza.

Captain Byte stood at the front of his ship.

One boot on the rail.

Hat crooked.

Grin enormous.

"Today," he announced, to absolutely no one, "we find the treasure!"

He had a map.

He had a ship.

He had four slices of cold pizza in his coat pocket.

He was ready.

...mostly.

---

Here is the thing about Captain Byte.

He *loves* doing things.

Planning things? Less fun.

Remembering things? Almost impossible.

"Right!" he said. "The map says the treasure is buried at exactly—"

He looked at the map.

He looked at the sea.

He looked back at the map.

"...at exactly a number. A *very* important number. I definitely read it a second ago."

But the number was gone.

It had floated right out of his head, the way numbers do.

---

Captain Byte tried shouting it to make it stick.

"TWENTY-SOMETHING!" he yelled at the waves.

The waves did not help.

He tried writing it on his hand.

He got distracted by pizza and smudged it.

"This is hopeless," he groaned. "How is a captain supposed to remember *everything?*"

---

A slow puff of steam curled up from the deck.

The smell of tea arrived before the dragon did.

"Interesting," said Dragon Debug, sipping from a cup that was somehow never empty.

Now — in the Guild, when Dragon Debug says *"Interesting,"* it usually means one thing:

*You are about to learn something.*

"Captain," said the dragon, "you keep losing the number.

So stop trying to hold it in your head.

Give it to the ship. Let the ship remember it *for* you."

Captain Byte blinked. "The ship can *remember* things?"

"Everything can remember things," said Dragon Debug, "if you give the thing a **name**."

---

The dragon set down the teacup.

"Imagine an empty treasure chest," he said.

"You put something inside.

Then you write a name on the lid — big and clear — so you can always find it again."

"That," said Dragon Debug, "is a **variable**.

A box with a name.

The computer holds the box for you, and never forgets what's inside."

TommyBot rolled forward, eyes wide.

*(TommyBot is you, by the way. Curious. Brave. Full of questions. That's exactly how Builders are made.)*

"So," TommyBot asked, "if I want the ship to remember the Captain's name...

I put the name in a box — and I give the box a name too?"

"Now," said the dragon, "you're building."

---

Here is how you tell the ship, in Python:

```python
captain_name = "Byte"
```

Read it out loud, right to left, the way the dragon does:

> Take the name `"Byte"`,
> put it in a box,
> and label that box `captain_name`.

The `=` is not really "equals."

It means: **"put this into that box."**

Now the ship remembers.

Ask it any time you like:

```python
print("Ahoy! Captain", captain_name, "is ready to sail!")
```

And the ship answers:

```
Ahoy! Captain Byte is ready to sail!
```

Captain Byte gasped.

"It remembered my name! I've been trying to do that for *years!*"

---

"Now," said Dragon Debug, "the important number."

Captain Byte squinted at the map.

This time, the moment he read it, he *stored* it:

```python
treasure_depth = 27
```

A box named `treasure_depth`, with `27` safely inside.

Stored.

Named.

Never floating out of anyone's head again.

"Twenty-seven paces down!" cried the Captain.

"I'll never lose it now — the *ship* is holding it for me!"

---

Captain Byte was so pleased he made one more box on the spot:

```python
pizza_slices = 4
```

"Now the ship will *always* know how much pizza I have!"

Then he ate a slice.

He asked the ship. The ship said `4`.

Captain Byte frowned. "...it's lying to me."

"No," said Dragon Debug, hiding a smile behind his tea.

"You changed the pizza. You didn't tell the box.

A box holds exactly what you put in it — no more, no less."

The Captain looked at his three real slices.

Then at the box, still proudly insisting there were `4`.

"Best kind of pizza," he decided. "The kind that comes back."

*(One day we'll teach a box how to change its mind. For now, a promise: a box remembers exactly what you gave it. Nothing sneaks in or out on its own.)*

---

Then, being Captain Byte, he got excited and typed too fast:

```python
print("The treasure is at", tresure_depth, "paces down.")
```

The ship went quiet.

Then it said something red and grumpy:

```
NameError: name 'tresure_depth' is not defined
```

Captain Byte's face fell.

"It's broken! I broke the ship!"

"You didn't break anything," said Dragon Debug, calmly refilling his tea.

"The ship is *talking to you*. Read what it said."

Captain Byte read it again.

*tresure_depth.*

Then he read his box.

*treasure_depth.*

"...I spelled it wrong," he whispered.

"There's no second *a*. The ship went looking for that box — and that box doesn't exist."

Dragon Debug smiled.

**"Excellent. Now the conversation begins."**

One fixed letter later, the ship answered perfectly:

```
The treasure is at 27 paces down.
```

---

From the corner of the deck, a small rubber duck had watched the whole thing.

He said nothing.

He is **Professor Quackers**, and saying nothing is his entire method.

*(You'll understand later. Everyone does.)*

"Quack," said Professor Quackers.

Somehow, it felt like wisdom.

---

## 🐛 Debug Log

Real Builders keep a little record of the bugs they beat.

It turns a frustrating moment into something to be proud of.

Here's your very first one:

| My bug | What caused it? | How did I fix it? |
|--------|-----------------|-------------------|
| The ship said `NameError`. | I spelled the box's name wrong — `tresure_depth` instead of `treasure_depth`. | Fixed the spelling so both names matched. The ship found the box. |

One missing letter.

That's all a bug often is.

---

## 🐉 A riddle, before you sail on

Dragon Debug set down his tea and looked right at you.

"You learned something real today," he said.

"Let's see if it stuck."

> *I am a box you'll never see.*
> *Put something in — it stays with me.*
> *Give me a name, just one that's true,*
> *and I'll remember it... long after you forget to.*
>
> **What am I?**

Say your answer out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **a variable.**

And if you knew that — Builder, you just spoke your first word of Python.

---

## 🧰 Toolbox Card — Variables

A **variable** is a box with a name.

- You **put** something in it: `gold = 3`
- The computer **remembers** it for you.
- You **look inside** any time by using its name.

Give your boxes clear names.

`treasure_depth` tells you what's inside.

`x` tells you nothing.

Clear names are a gift to the next Builder — and the next Builder is usually *you*, next week.

---

## 🏗️ In the Real World

> Every app you've ever used remembers things with **variables** —
> your game's score, your health bar, your username.
>
> Grown-up Builders call everything a program remembers its **state**.
>
> You just met the idea humming behind every screen you tap.

---

## 🐉 Dragon Debug's Wisdom

> *"Don't keep it in your head.*
> *Give it a name, and let the computer hold it for you."*

---

### ⭐ Achievement Unlocked

**Rookie Python 🐍** — *You wrote your first real Python, and taught a computer to remember something for you. That is the very first power every Builder learns.*

---

### To be continued...

Captain Byte's stomach growled.

Loudly.

"Before *any* treasure," he declared, "a captain must eat."

But the ship's kitchen had a question of its own:

*How many slices?*

And to answer that, the ship would have to learn a brand-new trick —

how to **ask**.

→ *Next: the Hungry Pizza Robot.* 🍕

# Chapter 7 — The Safe Password Checker

> *"A weak password is a door with no lock. A strong one is a door that asks good questions."*

---

The keypad glowed in the dark.

```
Too short. Too simple. Too guessable.
```

"...Rude," said Captain Byte again,

still a little hurt.

"It's a *great* password. Pizza is my whole personality."

Dragon Debug said nothing.

He just sipped his tea

and looked at a spot near the Captain's boots.

Something small was standing there.

---

It was a knight.

A *very* small knight.

Barely taller than a teacup,

polished head to toe,

and carrying two flags —

one **green**, one **red** —

as if they were the most important things in the world.

To him, they were.

The little knight bowed, low and serious.

"Who," said the Captain, "are you?"

The knight thought about it.

Hard.

Then he lifted the **green** flag. 🟢

---

"...Is that a yes?" said the Captain.

The knight lifted **green** again.

"Can you say anything *else?*"

The knight froze.

His tiny face wrestled with something enormous.

Then, slowly, almost apologetically,

he raised the **red** flag. 🔴

The Captain turned to Dragon Debug.

"Is he broken too?"

---

"He isn't broken," said the dragon,

and for once he was smiling before the lesson,

not during it.

"This is **Sir Boolean.**

And he is the most honest knight in the Guild."

"He only owns two answers.

Green for **true.**

Red for **false.**

Ask him anything —

*anything* —

and he will give you one flag or the other.

Never a maybe. Never a shrug.

Just... true, or false."

Sir Boolean nodded so hard his helmet wobbled.

> *(He's named after a real person, they say —*
> *someone who loved true-and-false so much*
> *he built a whole kind of maths out of just those two words.*
> *A story for another day.)*

---

"A question with only two answers,"

said the dragon,

"has a name in Python.

We call it a **boolean.**

Sir Boolean *is* one.

Is it raining? Are you eight or older?

Is this password long enough?

Every one of those is a tiny question

that can only ever come back **true** or **false.**

Green flag.

Or red flag."

The Captain looked at the sulking keypad.

"So... the door is just asking me questions?"

"Now you see it," said the dragon.

---

"It asked the first one already," he went on.

"*Is this password long enough?*

Watch."

He held up the word `pizza`

and counted on his claws.

"p—i—z—z—a. Five letters.

Python has a tool that counts for you.

It's called **`len`** — short for *length.*"

```python
len("pizza")
```

"That gives back `5`.

The vault wants **8 or more.**

So the real question is:"

```python
len(password) >= 8
```

"And look —

that little line, all on its own,

*is a flag.*

Hand it `pizza`, and it comes back **false.**"

Sir Boolean looked at `pizza`,

counted quietly,

and raised the **red** flag. 🔴

---

Captain Byte, of course, could not wait.

He never can.

"I've *got* this," he said,

cracking his knuckles.

"I'll ask all the questions at once."

He typed fast:

```python
password = input("Set your password: ")

if len(password) >= 8 and password != "pizza":
    print("Password accepted!")
else:
    print("WRONG!")
```

"Long **and** not-pizza," he said proudly.

"If it passes — accepted. If not — WRONG. Simple!"

He typed `pizza`.

```
WRONG!
```

"HA! Caught it!"

Then, just to show off, he typed `password`.

```
Password accepted!
```

The Captain's grin fell off his face.

---

"...*What?*" he whispered.

"My vault just accepted the word `password`.

The worst password in the *history of passwords.*"

That sinking feeling — the one where you were *sure* you'd built it right —

is allowed, Captain.

Even dragons have shipped a guard that let the wrong thing through.

Dragon Debug set down his cup.

"Interesting," he said.

Which — you know by now — means *lean in.*

"Two things went wrong here, Captain.

And both of them are the same mistake."

He held up one claw.

"First — when it said **WRONG!**,

did it tell you *which* rule you broke?

Too short? Too obvious? A bit of both?

No. It just shouted.

A guard that yells 'WRONG!' and nothing else

is a guard nobody can learn from."

He held up a second claw.

"Second — you *mashed all your questions into one.*

`long AND not-pizza`.

But `password` is eight letters,

and it isn't `pizza`,

so your big clumsy rule waved it right through.

You asked one blurry question

and missed the danger completely."

**"Excellent,"** he said.

**"Now the conversation begins."**

---

Sir Boolean stepped forward.

This was his moment.

He set his two flags down, side by side,

and picked them up one at a time,

to show the Captain how flags *combine.*

---

**First — the word `and`.** 🟢🟢

"`and` is greedy," said the dragon.

"It only shows green

when **both** flags are green.

Long *and* not-pizza?

Both must be true, or the whole thing is false."

```python
len(password) >= 8 and password != "pizza"
```

Sir Boolean raised green in his left hand,

green in his right,

and — only then — nodded. ✅

---

**Next — the word `or`.** 🟢🔴

"`or` is generous," said the dragon.

"It shows green if **either** flag is green.

We can use it to sniff out silly passwords —

the ones everyone tries first."

```python
password == "pizza" or password == "password"
```

"*Is it pizza, or is it 'password'?*

If **either** is true — red alert.

We caught the sneaky one."

Sir Boolean raised one red, one green,

and still nodded — because *one* was enough.

---

**Last — the word `not`.** 🔴➡️🟢

"`not` is a mirror," said the dragon.

"It flips a flag.

Green becomes red. Red becomes green."

```python
not password == "pizza"
```

"That says: *true, as long as it is NOT pizza.*"

Then the dragon's eyes twinkled.

"But Captain —

you already learned this flip.

Back at the chest, remember?"

```python
password != "pizza"
```

"`!=` and `not ... ==` say the very same thing.

You've been flipping flags since Chapter 6.

You just didn't know the knight's name for it."

The Captain blinked.

"I already knew a spell... and didn't know I knew it?"

"That," said the dragon, "happens to Builders all the time."

---

"Now," said the dragon, "the real fix.

Don't ask one blurry question.

Ask each one *on its own* —

and give each red flag its *own honest answer.*"

```python
password = input("Set your password: ")

if len(password) < 8:
    print("Too short. I need at least 8 letters.")
elif password == "pizza":
    print("Too obvious. Everyone knows you love pizza.")
elif password == "password":
    print("Really? 'password' is the first thing a thief tries.")
else:
    print("Strong! The vault is yours.")
```

The Captain typed `pizza`.

```
Too short. I need at least 8 letters.
```

"It *told* me why!"

He typed `password`.

```
Really? 'password' is the first thing a thief tries.
```

"It caught it! It actually *caught* it!"

He typed `seadragon42`.

```
Strong! The vault is yours.
```

The keypad glowed warm and green.

Deep in the door, a lock turned —

a real one, this time.

---

"See the difference?" said the dragon quietly.

"The blurry guard shouted 'WRONG'

and let the thief walk in.

The clear guard asked one honest question at a time —

and told you exactly how to do better.

That is the whole art of a good gate."

Sir Boolean, overcome,

raised **both** flags at once.

Then remembered he can't do that,

and settled, proudly, on green. 🟢

---

"Builder — your turn," said the dragon.

"Guard your own vault.

Ask if it's long enough.

Ask if it's one of the silly ones.

And when a rule fails,

don't shout 'WRONG.'

*Tell the truth about which flag went red.*"

But TommyBot was already typing —

`elif` after `elif`, one honest question at a time,

as if the fix had been obvious for pages.

So you did.

You typed a weak one first —

on purpose —

just to watch the vault explain itself.

Then you fixed it,

one honest question at a time,

until the lock turned for you too.

---

On his shelf, the small rubber duck

had watched every flag go up and down.

Green. Red. Green.

Professor Quackers said nothing,

as is his way.

"Quack," he offered, at the end.

It meant:

*A good guard says no. A great guard says why.*

---

## 🐉 A riddle, before you sail on

Dragon Debug refilled his cup.

"One question," he said. "Then we open the door."

> *I own just two words in the whole wide world.*
> *One means "yes," and one means "no."*
> *I never say maybe, I never say "sort of" —*
> *I raise one flag, and away we go.*
>
> **What am I?**

Say it out loud.

Tell the duck, if you like. 🦆

.

.

.

Ready?

The answer is: **a boolean** — true or false, and nothing in between.

And if you got it —

Builder, your programs can now *judge.*

They can look at a thing

and say, honestly, *yes* or *no.*

---

## 🧰 Toolbox Card — booleans & the three flag-words

A **boolean** is a question with only two answers: **`True`** or **`False`**.

Every comparison you write *is* a boolean:

```python
len(password) >= 8      # True or False, on its own
password != "pizza"     # True or False, on its own
```

**Count the letters** with `len`:

```python
len("pizza")   # 5
```

**Combine flags** with three little words:

- **`and`** — greedy. True only if **both** sides are true.
- **`or`** — generous. True if **either** side is true.
- **`not`** — a mirror. Flips true ↔ false. *(`not x == y` is the same as `x != y`.)*

**The golden rule of a good guard:**

> Don't ask one blurry question and shout "WRONG."
> Ask each question on its own —
> and tell the truth about *which* one failed.

---

## 🏗️ In the Real World

> Every "Are you sure?", every login, every form that says
> *"password too short"* is doing one job: **validation** —
> checking that what you typed follows the rules.
>
> And those true/false questions? Real Builders call them **booleans**,
> after a mathematician named George Boole. You just used his idea.

---

## 🐉 Dragon Debug's Wisdom

> *"Anyone can build a door that says no.*
> *A Builder builds a door that says no —*
> *and then, kindly, says why."*

---

### ⭐ Achievement Unlocked

**Flag Bearer 🚩** — *You met Sir Boolean and learned his honest little language: true and false. You can weigh a thing with `and`, `or`, and `not`, catch the sneaky answers a blurry rule would miss, and build a guard that doesn't just say no — it says exactly why. Your programs can judge now. Use it kindly.*

---

### To be continued...

The great door swung open at last.

Captain Byte rushed in, arms wide,

ready — *finally* — for gold.

There was no gold.

There was a **mountain.**

A towering, tumbling heap of salvage —

bottles and bolts and cracked circuit boards,

tin cans and copper wire and one very confused boot,

all the loot a hundred shipwrecks leave behind.

A sign leaned against the pile:

```
The treasure is here — buried in the mess.
Sort it. Count it. Only then is it yours.
```

Captain Byte stared up at the heap.

"There must be a *thousand* things in there."

High on a beam, Ninja Cat licked a paw,

pretended she hadn't just tried the new lock,

and watched to see what the Builder would do

with a pile far too big to count by hand.

→ *Next: the Recycling Robot — counting a mountain, one thing at a time.* ♻️

---

## 😄 Guild Extra — Sir Boolean's One Joke

Sir Boolean only ever carries two flags.

A green one that means **TRUE**.

A red one that means **FALSE**.

Someone once asked him for a third flag. Just in case.

He looked at them for a long moment.

Then raised the red one.

That's the whole joke.

Sir Boolean doesn't do maybe.

---

## 🥋 Typing Dojo — Mission 002: The Bouncer

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

The Guild door has a new bouncer, and he takes his job *seriously.*

To get in, your password must clear **two** rules — long enough,

and not one of the passwords every burglar tries first.

Fail, and the bouncer tells you **exactly** which rule you broke.

**🥋 Tier I — Keyboard Ninja.** *("Slice your caps.")*

Type this. Run it.

```python
password = input("Password, please: ")

if len(password) < 8:
    print("Too short. I need at least 8 characters.")
elif password == "password" or password == "12345678":
    print("Nice try. That one is on every burglar's first-guess list.")
else:
    print("Welcome in, Builder.")
```

Expected output:

```
Password, please: abc
Too short. I need at least 8 characters.
```

```
Password, please: password
Nice try. That one is on every burglar's first-guess list.
```

```
Password, please: dragon-tea-42
Welcome in, Builder.
```

*(Notice: `password` is eight letters long — it passes the first rule,*

*then gets caught by the second. Two separate checks, so the bouncer*

*always knows which door you tripped.)*

**🕵️ Conan's Challenge (optional):** the Guild's copy has three typos. Can you find them?

```python
password = inupt("Password, please: ")

if lem(password) < 8:
    print("Too short. I need at least 8 characters.")
elif password == "password" or password == "12345678":
    prnt("Nice try. That one is on every burglar's first-guess list.")
else:
    print("Welcome in, Builder.")
```

Run it once, and Python hands you your first clue:

```
NameError: name 'inupt' is not defined. Did you mean: 'input'?
```

Two more are hiding on the lines below. Find them the same way. 🦑

🐉 Dragon Debug sips his tea. "Interesting."

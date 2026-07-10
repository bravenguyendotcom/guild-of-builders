# Chapter 10 — The Caesar Messenger

> *"Every letter has a secret number. Slide the numbers, and the message hides itself."*

---

Captain Byte held the note up to the light.

```
Kw hud ixmttih.
```

He turned it sideways. Upside down. Sideways again.

"Nope. Still nonsense," he admitted. "But I'm *close.* I can feel it."

He squinted harder, as if squinting were a Python skill.

"...breakfast. It says breakfast."

"It does not say breakfast," said Dragon Debug, not even looking up from his tea.

---

TommyBot was already turning the note over, comparing letters to letters.

"It's not backwards," TommyBot said slowly. "I'd know backwards — that was the Mirror.

This is something else. The letters aren't rearranged. They're just... wrong.

Like every letter got bumped to a different one."

Dragon Debug set his cup down, and for the first time all morning, he looked genuinely pleased.

"Now *that,*" he said, "is exactly the right word. *Bumped.*"

---

"Here's a secret every Builder learns eventually," said the dragon.

"To a computer, a letter was never really a letter.

It's a **number**, wearing a letter's costume."

He tapped the console, and a small chart appeared:

```
'a' = 97
'b' = 98
'c' = 99
   ...and so on, all the way down the alphabet.
```

"Python has two little spells for crossing that bridge," Dragon Debug went on.

"`ord()` takes a letter and hands you back its number.

`chr()` takes a number and hands you back its letter.

They're opposites. A door that swings both ways."

TommyBot's eyes lit up. "So if I *bump* the number — just add to it —

then turn it back into a letter with `chr()`..."

"...you've built the oldest secret code in the world," said Dragon Debug.

"Generals used it before computers existed. Before *electricity* existed.

They just didn't have `ord()` to do the counting for them."

---

"I want to build one," Captain Byte announced. "Right now. For the crew.

Real pirate business needs a *secret* channel."

"Real pirate business," Dragon Debug repeated, sipping his tea, "usually just needs

fewer people shouting the treasure's location across an open deck. But — sure. Let's build it."

---

TommyBot was already at the console. This part felt familiar —

ask for a message, walk it letter by letter, build something new as you go.

The exact same shape as the Mirror, just yesterday.

"A message," TommyBot murmured, typing. "And a shift — how far to bump each letter.

Then walk the message, letter by letter, bumping as I go."

```python
message = input("Message to encode: ")
shift = input("Shift by how many? ")

secret = ""
for letter in message:
    code = ord(letter)
    secret = secret + chr(code + shift)

print("Encoded:", secret)
```

TommyBot hit Run without a second thought, already reaching for the next idea.

---

The ship did not print a secret message.

The ship printed this:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

---

TommyBot stared at it. Then laughed — a short, surprised laugh, not a defeated one.

"Wait. I *know* this one," TommyBot said. "This is the pizza-robot bug.

Chapter 2. `input()` always hands back text, even when it looks like a number.

I forgot again — just... in a new place this time."

"So?" said Dragon Debug, not offering the answer. Just the question.

"What does a Builder do, when a bug turns out to be an old friend?"

---

TommyBot thought about it for a second — really thought, not just reached for the fix.

"...Doesn't fix it and feel dumb," TommyBot said. "Fixes it, and feels like — like proof.

Proof that I actually learned it the first time. It's just showing up somewhere new."

Dragon Debug's tea had gone still in his hand.

"That," he said quietly, "is a truer sentence than most Builders manage on their *tenth* bug.

You didn't just fix it, TommyBot. You recognized it — and you weren't ashamed of it.

That's the harder skill. Most people never learn that part at all."

---

**"Excellent. Now the conversation begins."**

TommyBot wrapped the shift in `int()`, same trick as always —

*tell* Python the text is really a number, before asking it to do number things.

```python
message = input("Message to encode: ")
shift = int(input("Shift by how many? "))

secret = ""
for letter in message:
    code = ord(letter)
    secret = secret + chr(code + shift)

print("Encoded:", secret)
```

One word, then a shift of `3`:

```
Message to encode: pizza
Shift by how many? 3
Encoded: sl}}d
```

Captain Byte peered at it. "That's — that's not even *readable.* You broke my pizza."

"I hid your pizza," TommyBot corrected. "Bump it back the other way, and it comes home."

A shift of `-3` on `sl}}d`, and the console answered:

```
Message to encode: sl}}d
Shift by how many? -3
Encoded: pizza
```

Captain Byte's whole face changed. "It came BACK. My pizza came BACK.

TommyBot. TommyBot, we have to send *everything* like this now."

---

## 🧪 Testing Table

TommyBot ran it twice more, just to be sure `pizza` wasn't a lucky one.

| Input (message, shift) | Expected | Actual |
|---|---|---|
| `pizza`, `3` | `sl}}d` | `sl}}d` ✅ |
| `sl}}d`, `-3` | `pizza` | `pizza` ✅ |
| `Byte`, `5` | `G~yj` | `G~yj` ✅ |
| `G~yj`, `-5` | `Byte` | `Byte` ✅ |

Same shift forward, same shift back, every single time.

That's not luck. That's a Builder who understood the machine underneath.

---

## 🐛 Debug Log

| My bug | What caused it? | How did I fix it? |
|---|---|---|
| The ship said `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. | I asked for the shift with `input()` and used it right away — but `input()` always hands back text, even when it looks like a number, so Python couldn't add it to `code`. | Wrapped it in `int()`: `shift = int(input(...))` — the same fix from Chapter 2, showing up in a brand-new place. |

Some bugs only visit once.

This one's an old friend — and old friends are the easiest to recognize.

---

## 🧰 Toolbox Card — `ord()`, `chr()`, and character math

Every letter is secretly a number. Python keeps the lookup table so you don't have to.

```python
ord("a")   # 97  -- letter to number
chr(97)    # "a" -- number back to letter
```

**`ord()`** and **`chr()`** are opposites — a door that swings both ways.

Add to the number, and you've *bumped* the letter along the alphabet:

```python
code = ord(letter)
new_letter = chr(code + shift)
```

Bump every letter in a message the same amount, and you've built a cipher.

Bump back by the same amount, the other direction, and the message comes home.

*(No wraparound yet — bump too far past `z`, and you land on stranger symbols,*
*not back at `a`. That's a trick for a future chapter.)*

---

## 🏗️ In the Real World

> Turning meaning into numbers, shifting the numbers, and turning them back —
> that's the great-great-grandparent of every **encryption** protecting your
> passwords, your messages, and your bank card right now.
>
> Real encryption is *far* more complex than one shift repeated down a line.
> But the core idea — hide meaning inside numbers, and hold the key that
> undoes it — is exactly the one you just built.

---

## 🐉 Dragon Debug's Wisdom

> *"A secret isn't magic.*
> *It's just a number, wearing a costume —*
> *and knowing which costume is the whole trick."*

---

### ⭐ Achievement Unlocked

**Cipher Smith 🗝️** — *You learned that letters are secretly numbers, built a working cipher with `ord()` and `chr()`, met an old bug wearing a new costume — and this time, you recognized it before it could shake you.*

---

### To be continued...

"Okay," said Captain Byte, cracking his knuckles. "NOW we read the note."

TommyBot ran the note through the cipher, shift `1`. Gibberish.

Shift `2`. Gibberish.

Shift `3`... `4`... `5`...

Twenty-five shifts, tried one by one, patient as a tide.

Not one of them turned `Kw hud ixmttih.` into real words. Not a single one.

"That doesn't make sense," said TommyBot, sitting back. "The shift trick

*works.* We just proved it works. Why doesn't it work on *this?*"

Dragon Debug studied the note for a long moment, tea forgotten in his hand.

"Because," he said slowly, "whoever wrote this didn't shift every letter

the *same* amount." He looked up. "Which means someone out there

already knows a trick we haven't learned yet."

---

From somewhere ahead, past the tree line, came a sound none of them expected —

a drumroll. Then applause. Then a booming, delighted voice asking a riddle

to an audience of absolutely no one.

Ninja Cat was already trotting toward it, tail flicking with interest,

the note's mystery forgotten for now — but only for now.

"Someone up ahead," she seemed to say, without saying anything at all,

"loves puzzles even more than you two do."

→ *Next: The Riddle Theatre — where the road is blocked by wordplay.* 🎭

---

## 😄🧩🎨 Guild Extra

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

## 🥋 Typing Dojo — Mission 005: Secret Cipher

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

Every letter has a secret number. `a` is one number, `b` is the next, and so on

down the line. Slide every number along by the same amount, turn them back into

letters, and your message turns to nonsense that only the Guild can read.

Slide it back the other way, and the secret returns.

**🥋 Tier I — Keyboard Ninja.** *("Slice your caps.")*

Type this. Run it.

```python
message = input("Message to encode: ")
shift = int(input("Shift by how many? "))

secret = ""
for letter in message:
    code = ord(letter)
    secret = secret + chr(code + shift)

print("Encoded:", secret)
```

Expected output:

```
Message to encode: hello
Shift by how many? 3
Encoded: khoor
```

```
Message to encode: dragon
Shift by how many? 3
Encoded: gudjrq
```

To *decode*, run it again on the secret with a **negative** shift:

```
Message to encode: khoor
Shift by how many? -3
Encoded: hello
```

*(`ord()` turns a letter into its number; `chr()` turns a number back into a letter.*
*The whole cipher is just counting — no magic, no shortcut.)*

**🕵️ Tier II — Conan's Challenge.** *("Do you have any clue?")*

Same cipher — but **three typos** slipped in. No logic is broken. Only fingers.

```python
message = input("Message to encode: ")
shift = int(input("Shift by how many? "))

secret = ""
for letter in message:
    code = odr(letter)
    secret = secret + crh(code + shift)

 print("Encoded:", secret)
```

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 13
    print("Encoded:", secret)
                             ^
IndentationError: unindent does not match any outer indentation level
```

**Excellent. Now the conversation begins.**

Straighten that line up, run again, and the next two clues are waiting — both hiding

in the Mirror's new trick, the little spells that turn letters into numbers and back. 🦑

🐉 Dragon Debug sips his tea. *"Interesting."*

Captain Byte insists he can read any code by eye. *(He read `gudjrq` as "breakfast.")*

Professor Quackers says nothing. Professor Quackers never does. 🦆

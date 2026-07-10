# Chapter 9 — The Palindrome Mirror

> *"Some things can't be flipped by asking. You build the reflection yourself."*

---

The mirrored plate sat heavy in Captain Byte's hands.

One word, engraved deep.

Read left to right: one thing.

Read right to left: the *exact same thing.*

"Ninja Cat," the Captain called up, "did you know about this?"

Ninja Cat said nothing.

Ninja Cat rarely explains a mystery when watching you find it is more fun.

---

The plate was warm. Warmer than metal should be.

And beneath it, set into the deck, was a slot —

shaped exactly like the plate, with six words etched above it:

```
Only a true mirror-word may pass.
```

Captain Byte slid the plate toward the slot, then stopped.

"Wait. How do I know if a word is a — a mirror-word?

Some are easy. `level`. Anyone can see that one's the same backwards."

He frowned. "But what about a *long* one? A weird one?

I can't just... stare at it and hope."

---

Dragon Debug climbed up, tea in hand, and looked at the slot with interest.

"You don't stare," he said. "You *check.*

And a Builder never checks by hoping. A Builder checks by building."

"So I need... a mirror-checker," said the Captain slowly.

"That's the job, yes," said the dragon.

---

TommyBot was already crouched by the ship's console, fingers moving.

The reset-inside-the-loop bug from the salvage pile was still fresh —

close enough to still sting a little, far enough to feel like a lesson learned.

This time, TommyBot wanted to get there *first.*

"I've got an idea," TommyBot said. "A word is just letters, right?

Like the pile was just items. And yesterday, we walked a whole pile

with a `for` loop. A word should work the same way."

"Good instinct," said Dragon Debug. "Keep pulling that thread."

---

TommyBot typed fast, chasing the idea before it could slip away.

"If lists have a `.reverse()` tool... strings probably do too, right?

Same family. Should work the same way."

```python
word = "level"
word.reverse()
print(word)
```

TommyBot pressed Run, already smiling.

The ship did not print a reversed word.

The ship printed this:

```
AttributeError: 'str' object has no attribute 'reverse'
```

---

TommyBot stared at the words. Read them again. They didn't get friendlier.

"...I don't understand," TommyBot said. "It worked for the pile.

Why doesn't it work for a word?"

That hot, small itch of *I followed the pattern and it still broke* —

the same one from yesterday — crept back in, quieter this time,

but not gone.

"That feeling again," TommyBot admitted. "I thought I was past it."

"You're never past it," said Dragon Debug, gently.

"You just get faster at recognizing it — and faster at *not* running from it.

That's not a step backward, Builder. That's the whole climb."

---

**"Excellent. Now the conversation begins."**

Dragon Debug set down his tea and knelt by the console.

"Here's what the ship is actually telling you," he said.

"A **string** — a word — is *close cousins* with a list. Both hold things in order.

But a string is special: once it's written, it can't be rearranged in place.

Not shuffled. Not reversed. Not edited letter-by-letter, mid-word.

It's *fixed*, the moment it's made."

TommyBot blinked. "So... it really can't flip itself?"

"It can't," said the dragon. "But *you* can build a new one, letter by letter,

that happens to be its mirror. The string won't change.

You'll just make a second one, right beside it, facing the other way."

---

"Same trick as the pile," Dragon Debug went on. "You already know the move —

walk it, one thing at a time. Only this time, instead of counting,

you're going to *stack.*"

```python
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
```

"Start with an empty box," said the dragon. "Then, for every letter you visit —

put it in *front* of whatever's already there. Not behind. In front."

TommyBot squinted at it. "So the first letter you see... ends up last?"

"Watch," said the dragon.

---

TommyBot ran it, this time tracing each letter out loud, exactly as Dragon Debug taught.

`l` goes in: `reversed_word` is `"l"`.

`e` goes in *front*: `reversed_word` is `"el"`.

`v` goes in front: `"vel"`.

`e` goes in front: `"evel"`.

`l` goes in front: `"level"`... backwards.

"Wait," said TommyBot, sitting up straighter. "That's — that's the *same word.*

`level` reversed is still `level`."

"That's what makes it a mirror-word," said Dragon Debug. "A palindrome.

And now you have the last piece — how do you *check* it, without a person staring?"

TommyBot didn't hesitate this time. "Compare them. `==`. Same as always."

```python
if word == reversed_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
```

The Recycling Robot, still nearby, made a small approving click.

Even it agreed: that was the honest way to check.

---

## 🧪 Testing Table

TommyBot ran the checker on a few words, just to be sure it wasn't a fluke.

| Input | Expected | Actual |
|-------|----------|--------|
| `level` | is a palindrome | is a palindrome ✅ |
| `dragon` | is not a palindrome | is not a palindrome ✅ |
| `kayak` | is a palindrome | is a palindrome ✅ |

Three for three. The Mirror had a new, honest judge.

---

## 🐛 Debug Log

| My bug | What caused it? | How did I fix it? |
|--------|-----------------|--------------------|
| The ship said `AttributeError: 'str' object has no attribute 'reverse'`. | I assumed strings could reverse themselves in place, like I'd hoped lists could — but strings can't be rearranged once they're made. | Built a *new* word by walking the old one letter by letter, stacking each new letter in front, then compared the two with `==`. |

An error that stops you cold isn't a wall.

It's the ship telling you exactly which assumption to let go of.

---

## 🧰 Toolbox Card — Strings, one letter at a time

A **string** holds its letters in order, just like a list holds its items —

but once it's written, it's **fixed.** You can walk it. You can't rearrange it.

```python
for letter in word:
    print(letter)
```

To build something new *from* a string — like its mirror — start with an

empty box, then add to it as you walk:

```python
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
```

Adding a letter to the **front** each time is what flips the order.

Then check your work the plain way: `word == reversed_word`.

A **palindrome** is any word where that comparison comes back `True`.

---

## 🏗️ In the Real World

> Walking through text one character at a time, and building something new
> from it, is called **string processing.**
>
> Every spell-checker, every search bar, every autocomplete you've ever used
> is doing exactly this — reading letters, one at a time, and deciding
> what to do next.
>
> You just wrote your first real string-processing program.

---

## 🐉 Dragon Debug's Wisdom

> *"Some things can't be flipped by asking.*
> *You don't force them to change.*
> *You build the reflection yourself — one true piece at a time."*

---

### ⭐ Achievement Unlocked

**Mirror Walker 🪞** — *You met your first string bug, learned that words can't rearrange themselves, and built a mirror-checker from scratch — one letter, stacked in front of the last, until the reflection was complete. The Mirror has never met a truer judge.*

---

### To be continued...

The plate slid home with a click like a held breath finally let out.

The deck shuddered. A hidden drawer creaked open at Captain Byte's feet.

Inside: no gold. Just a single folded note, its message scrawled in letters

that made no sense at all.

```
Kw hud ixmttih.
```

Captain Byte turned it over, upside down, sideways. Nothing helped.

"That's not backwards," he said slowly. "I'd know backwards now.

This is something else."

Dragon Debug leaned in, and for the first time all day, he didn't answer right away.

"Someone didn't hide this treasure," he said at last. "Someone *wrote* to it.

And whoever they were... they didn't want just anyone reading it."

High above, Ninja Cat's ears twitched once, toward the horizon,

as if she already knew exactly who had.

→ *Next: the Caesar Messenger — a message hiding in plain sight.* 🗝️

---

## 🎨 Guild Extra — The Mirror Cat        (Art)

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

## 🥋 Typing Dojo — Mission 004: Mirror, Mirror

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

The Mirror only opens for one kind of word — one that reads exactly

the same, forwards and backwards. No shortcut tool. No `.reverse()` —

strings don't carry one. You build the reflection yourself, one letter

at a time, and let the Mirror judge what you made.

**🥋 Tier I — Keyboard Ninja.** *("Slice your caps.")*

Type this. Run it.

```python
word = input("Say a word for the Mirror: ")

reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    print(word, "is a palindrome. The Mirror agrees with itself.")
else:
    print(word, "is not a palindrome.")
```

Expected output:

```
Say a word for the Mirror: level
level is a palindrome. The Mirror agrees with itself.
```

```
Say a word for the Mirror: dragon
dragon is not a palindrome.
```

```
Say a word for the Mirror: kayak
kayak is a palindrome. The Mirror agrees with itself.
```

*(Watch `reversed_word` build itself backwards, one letter stacked in*
*front of the last — the same walk-the-thing move as Chapter 8's pile,*
*only now it's walking letters instead of items.)*

**🕵️ Tier II — Conan's Challenge.** *("Do you have any clue?")*

Same Mirror — but **three typos** slipped in. No logic is broken. Only fingers.

Two of them will stop the program cold, and Python will point right at them.

The third won't. It runs just fine and still isn't how this chapter spelled things.

```python
word = input("Say a word for the Mirror: ")

reversd_word = ""
fro letter in word:
    reversd_word = letter + reversd_word

if word = reversd_word:
    print(word, "is a palindrome. The Mirror agrees with itself.")
else:
    print(word, "is not a palindrome.")
```

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 8
    fro letter in word:
        ^^^^^^
SyntaxError: invalid syntax
```

**Excellent. Now the conversation begins.**

Two more are hiding — don't stop at the first one you fix. 🦑

🐉 Dragon Debug sips his tea. *"Interesting."*

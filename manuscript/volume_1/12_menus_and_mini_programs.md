# Chapter 12 — Menus & Mini-Programs

> *"A menu is just a promise: ask me again, as many times as you like —*
> *until you say stop."*

---

Sir Quizzalot cleared his throat with tremendous ceremony.

"By the authority vested in me — which is considerable — I hereby name

TommyBot **Keeper of the Guild Joke Board.**"

"Is that a real title?" asked TommyBot.

"It is now," said Maestro Monty, already hanging a small wooden sign

over the theatre's side door: **JOKE BOARD — SUBMISSIONS WELCOME.**

Captain Byte peered at the empty board. "So... what does a Keeper actually *do*?"

Dragon Debug set down his tea.

"Ask the board a question," he said. "Any question at all. Then ask it again.

And again. For as long as jokes keep arriving — which, with this crowd,

will be forever."

TommyBot frowned. "So it just... keeps asking? Over and over?"

"Every time," said the dragon. "Until someone tells it to stop."

Nobody had said the word *menu* out loud yet.

But TommyBot was already reaching for the keyboard, turning the idea over.

*Ask. Wait. Remember. Ask again.*

---

## The Task

A Joke Board needs three things, and the crew worked them out together,

right there on the theatre steps.

**One.** Show the options: add a joke, read the jokes, or close the board.

**Two.** Whatever the Builder picks, do that thing — and then show the options *again.*

**Three.** Every joke added has to still be there the next time someone asks —

not just for one turn, but for the whole session.

"That third one," said Dragon Debug, "is the interesting part. We need

something that *remembers.* We call that **state.**"

TommyBot had an idea already forming. "Like... a list. That just sits there,

outside the loop, and we add to it every time?"

Dragon Debug allowed himself the smallest smile. "Go on, then."

TommyBot built it, piece by piece, narrating along the way:

```python
jokes = []

while True:
    print()
    print("GUILD JOKE BOARD")
    print("1) Add a joke")
    print("2) Read all jokes")
    print("3) Close the board")
    choice = input("Choose: ")

    if choice == "1":
        joke = input("New joke: ")
        jokes.append(joke)
        print("Added:", joke)
    elif choice == "2":
        print("You have", len(jokes), "jokes:")
        for joke in jokes:
            print("-", joke)
```

"`while True`," Dragon Debug explained, "means *keep going, no matter what* —

a loop with no built-in reason to stop. And `.append()` is how a list

grows: it doesn't replace what's inside, it just adds one more thing

onto the end, quietly, every time you ask."

Captain Byte added a joke of his own the moment it ran.

*"Why don't pirates share pizza? Because they always split the deck."*

Nobody laughed. Captain Byte considered this a personal failing of the audience.

---

## The Honest Bug

Everything worked beautifully — right up until Captain Byte tried to leave.

"Alright," he said. "I'm done. Board says option three closes it. Watch this."

He typed `3`.

```
GUILD JOKE BOARD
1) Add a joke
2) Read all jokes
3) Close the board
Choose: 3
The board closes. Fair winds, Builder.

GUILD JOKE BOARD
1) Add a joke
2) Read all jokes
3) Close the board
Choose: 
```

The board did not close.

It said its goodbye — warmly, sincerely — and then cheerfully asked

the exact same question again.

"IT'S STILL HERE," bellowed Captain Byte, jabbing `3` a second time,

then a third, with rising fury. Each time, the board bid him a lovely

farewell. Each time, it reopened instantly, as if nothing had happened.

"I SAID close! I SAID fair winds! Why does it keep — is it *haunted?*"

Dragon Debug did not laugh, though it clearly cost him something.

"That growl is a familiar one, Captain. Every Builder has met a loop

that simply would not let them leave. It isn't haunted. It's honest —

it's doing *exactly* what you told it to do. We just haven't told it

the one thing it actually needs to hear."

"Excellent," he added, settling in. "Now the conversation begins."

TommyBot was already scrolling back through the code, and stopped

on the `elif choice == "3":` block.

"Wait," said TommyBot slowly. "We print the goodbye message... but we

never actually tell the loop to *stop.* We just fall right back to the

top and ask again. Saying goodbye isn't the same as leaving."

"Say more," said Dragon Debug — which, from him, was practically applause.

"We need the word for *leave this loop right now.* Is there one?"

There was.

```python
    elif choice == "3":
        print("The board closes. Fair winds, Builder.")
        break
```

One word. `break`. Said once, meant once.

Captain Byte typed `3` again, braced for another cheerful betrayal.

```
GUILD JOKE BOARD
1) Add a joke
2) Read all jokes
3) Close the board
Choose: 3
The board closes. Fair winds, Builder.
```

And it stopped.

Captain Byte stared at the quiet terminal for a long moment.

"...That's it? One word?"

"One word," said Dragon Debug, "in exactly the right place. That's most

of programming, Captain. Not more words. The *right* ones."

---

## 🧪 Testing Table

| Input | Expected | Actual (before fix) | Actual (after `break`) |
|---|---|---|---|
| Choose: 1, then a joke | Joke added, menu returns | ✅ worked | ✅ worked |
| Choose: 2 | Lists all jokes so far | ✅ worked | ✅ worked |
| Choose: 3 | Says goodbye, program ends | ❌ says goodbye, loops again | ✅ says goodbye, ends |

---

## 🐛 Debug Log

**My bug:** Choosing "Close the board" printed a goodbye — and then asked the question again anyway.

**What caused it?** The `elif choice == "3":` block *said* goodbye, but never told the `while True:` loop to actually stop. With nothing telling it otherwise, the loop just did what loops always do: went back to the top and asked again.

**How did I fix it?** Added `break` right after the goodbye message — the one word that means *leave this loop, right now.*

---

## 🧰 Toolbox Card

> *A `while True` loop has no built-in reason to stop. Saying goodbye out loud isn't the same*
> *as telling the loop to leave. If you want a door to actually close, you have to say `break` —*
> *clearly, and in the right place.*

---

## 🏗️ In the Real World

> The Joke Board's three moves — **add something, look at everything, close it down** — are

> two-thirds of a pattern real Builders use every single day. Grown-ups call it **CRUD**:

> **C**reate, **R**ead, **U**pdate, **D**elete. You just built Create and Read. Update (fixing

> a joke that fell flat) and Delete (retiring one that's overplayed) are coming later, when

> the story needs them — same board, same list, a couple more menu options.
>
> And that quiet little `while True` loop? It's the same shape behind a bank's ATM menu,

> a phone's customer-service line, and nearly every command-line tool a professional

> Builder touches before lunch. *Ask. Wait. Remember. Ask again — until someone says stop.*

---

## 🐉 Dragon Debug's Wisdom

> *"A loop with no exit isn't broken. It's just waiting for you*
> *to tell it, plainly, where the door is."*

---

### ⭐ Achievement Unlocked

**List Keeper 📋** — *You built a program that remembers — a list that grows every time you ask it to, and a menu that asks, and asks again, exactly as many times as it's needed. You met a loop that wouldn't leave, found the missing word, and said it. The Joke Board is officially open.*

---

### To be continued...

The board worked now. Truly, properly worked — open it, add a joke, read them back,

close it clean.

Captain Byte leaned back, admiring it. "It's perfect."

"It's *plain,*" said a new voice, faintly wounded, from somewhere in the rafters above the stage.

Nobody had noticed the figure up there — sketching, it seemed, on nothing at all,

with a paintbrush that left no visible mark.

"A board with no color," the voice went on, "is just a board. A **canvas**, painted well,

is a *welcome.*"

Dragon Debug looked up, entirely unsurprised, the way he always was.

"Later," he said, not unkindly. "One thing at a time."

From TommyBot's pocket, forgotten again in the excitement of the working menu,

the encoded note gave the faintest papery rustle.

Some mysteries wait for their moment.

This wasn't it. Not yet.

→ *Next: The Painter's Deck — where the board finally gets its colors.* 🎨

---

## 😄🧩🎨 Guild Extra

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

## 🥋 Typing Dojo — Mission 007: The Quest Log

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

Every Builder needs a place to keep their quests.

Not on a scrap of paper that blows away — in a program that *remembers.*

Show a menu. Wait for a choice. Add a quest, or list them all, or close the book.

Then loop back and do it again, for as long as you like.

This little shape — *menu, choice, remember, repeat* — is almost every program ever written.

**🥋 Tier I — Keyboard Ninja.** *("Slice your caps.")*

Type this. Run it. Add a few quests of your own, then list them.

```python
quests = []

while True:
    print()
    print("QUEST LOG")
    print("1) Add a quest")
    print("2) Show all quests")
    print("3) Close the log")
    choice = input("Choose: ")

    if choice == "1":
        quest = input("New quest: ")
        quests.append(quest)
        print("Added:", quest)
    elif choice == "2":
        print("You have", len(quests), "quests:")
        for quest in quests:
            print("-", quest)
    elif choice == "3":
        print("The log closes. Fair winds, Builder.")
        break
    else:
        print("That's not on the menu.")
```

Expected output:

```
QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 1
New quest: Find the Sunstone
Added: Find the Sunstone

QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 2
You have 1 quests:
- Find the Sunstone

QUEST LOG
1) Add a quest
2) Show all quests
3) Close the log
Choose: 3
The log closes. Fair winds, Builder.
```

*(Notice the shape — it's the Joke Board's twin. Same pattern, new skin.*

*You didn't just meet this idea once today. You built it, broke it, and fixed it —*

*and now you're typing it again on purpose. That's how it sticks.)*

**🕵️ Tier II — Conan's Challenge.** *("Do you have any clue?")*

Same log — but **three typos** slipped in. No logic is broken. Only fingers.

```python
# The Quest Log
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

quests = []

while True
    print()
    print("QUEST LOG")
    print("1) Add a quest")
    print("2) Show all quests")
    print("3) Close the log")
    choice = input("Choose: ")

    if choice == "1":
        quest = input("New quest: ")
        quests.apend(quest)
            print("Added:", quest)
    elif choice == "2":
        print("You have", len(quests), "quests:")
        for quest in quests:
            print("-", quest)
    elif choice == "3":
        print("The log closes. Fair winds, Builder.")
        break
    else:
        print("That's not on the menu.")
```

Retype it, run it, and fix each slip until it runs clean. Fix one, and the next clue steps forward.

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 7
    while True
              ^
SyntaxError: expected ':'
```

**Excellent. Now the conversation begins.** 🦑

Fix that one, run again, and two more clues are waiting — one in how a quest

gets added, one in how far a line leans.

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Captain Byte adds three quests to his log. All three just say *"eat pizza."*

Professor Quackers says nothing. Professor Quackers never does. 🦆

# 🏴‍☠️ Captain Byte's Treasure Quest — v1

Your first complete game, Builder. This is the Volume I deliverable of
**The Guild of Builders** — a playable command-line adventure, built entirely
from the mini-games you made across the volume.

## How to play

You need Python 3. Then, from inside this folder:

```
python3 main.py
```

The ship's console gives you a menu. Clear all five trials, then claim the treasure:

- 🔒 **The Chest** — guess the number (from Chapter 6)
- 🚪 **The Gate** — set a safe password (from Chapter 7)
- 🪞 **The Mirror** — speak a palindrome (from Chapter 9)
- 🗝️ **The Coded Message** — decode the cipher (from Chapter 10)
- 🎭 **The Riddle** — outwit Monty & Quizzalot (from Chapter 11)

Then pick **6) Claim the Treasure**. Play again as often as you like.

## What's inside

```
treasure_quest/
├── main.py        # the ship's console — the menu loop that runs the game
├── story.py       # all the words: title, intro, endings
├── minigames.py   # the five trials, each a mini-game you already built
└── README.md      # this file
```

## Why it's built this way

Each trial is a mini-game you wrote earlier in Volume I, wrapped as a function
the console can call. The game didn't need a *new* idea — it needed the ones you
already had, standing together on deck. That's the whole lesson of the capstone.

Uses only Volume I skills: `input`, loops, `if`/`elif`/`else`, `random`, and strings.
No installs, no external libraries.

## What's next

Right now this is a **menu** of adventures. In Volume II, you'll learn to weave them
into one journey — where the number you crack from the chest becomes the key you carry
to the gate. Same game. Bigger. 🐉

---

🍩 *You didn't just play a game. You built one. Say it out loud: **I built this.***

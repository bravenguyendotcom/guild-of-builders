# 🎮 GAME_DESIGN.md

### *Captain Byte's Treasure Quest* — the one game, four generations

> **Status:** v1 spec is **DRAFT-ready to build**. v2–v4 are **DRAFT direction**.
> **The rule that makes this project special:** the game is **never restarted**. Each
> volume evolves the *same* game. This is where the child *feels* iterative development,
> versioning, and Kaizen — because they live it.

---

## Design pillars (apply to every version)

1. **Playable & shareable from v1.** Even the first CLI version should be fun enough that
   the child proudly runs it for a friend.
2. **Story-driven.** Captain Byte, Dragon Debug, Professor Quackers, and the Bug Monster
   appear in the game itself, not only in the book.
3. **Uses exactly what the volume taught** — no more, no less. The game is the proof of
   the curriculum.
4. **Every version is a real deliverable** (the Donut Law 🍩).
5. **Progressive & never lost.** A Builder finishing any volume can answer: *"What did I
   just achieve? What's coming next?"* We never let them feel lost.

---

# Version 1 — CLI Adventure (Volume I deliverable)

**Platform:** command line (pure Python, no external libraries).
**Goal:** a short, funny, complete text adventure.

### The v1 shape: a **menu of adventures**, wrapped in one story

Treasure Quest v1 is a **menu-driven adventure**, not a single tightly-woven storyline. The
game's main console (the menu loop from Ch 12 / Mission 007 / 010) offers the player a short
sequence of **story stops**, each of which *is* a mini-game the Builder already built earlier
in the volume:

- 🔒 **The Chest** — guess-the-number to crack it open (Ch 6 / Mission 001).
- 🚪 **The Gate** — a password/logic check to pass (Ch 7 / Mission 002).
- 🪞 **The Mirror** — a palindrome puzzle (Ch 9 / Mission 004).
- 🗝️ **The Coded Message** — decode a Caesar cipher (Ch 10 / Mission 005).
- 🎭 **The Riddle** — a riddle gate from Monty & Quizzalot (Ch 11).
- 🏴‍☠️ **The Treasure** — reached when the stops are cleared; win/lose + achievements.

A light story wraps the menu so it feels like *a voyage with meaningful plot*, not a quiz: the
Captain sails, the console is the ship's wheel, each choice is a place on the map, and the
treasure is the payoff. **The recognition is the magic** — a Builder plays it and thinks *"hey,
that's MY guess-the-number game… and MY password checker… all in one place."*

**Why menu-of-adventures for v1 (and not tight-woven):** it's honest to Volume I skills (no data
structures or state machines yet), it's genuinely playable and complete, and assembling
already-built pieces is exactly the capstone's lesson — *you already have everything; now make it
stand together* (D-23, Mission 010 is an Echo). Tight-woven integration (one seamless branching
story where the pieces interlock) needs Vol II tools (inventory, state, save/load) — so it's a
**Volume II** evolution, not a v1 requirement.

> **🌱 Plant the seed (in the Ch 15 capstone).** The game ends by *inviting the next ambition*:
> "This is a menu of adventures. But what if they weren't a menu — what if it were **one woven
> journey**, where the chest you crack drops a key you carry to the gate? Hold that thought. That's
> Volume II thinking." The capstone doesn't just ship a game; it makes the Builder *itch to make it
> more.* (North Star: curiosity pulling toward the next volume.)

### Required features
- An **intro story** (Captain Byte sets sail for treasure) + a **coloured title screen** (Ch 13).
- A **main menu / console** that loops (Ch 12 / Missions 007, 010) — the ship's wheel.
- **Choices** that branch the path (`if`/`elif`/`else`).
- **The reused mini-games** as story stops (chest, gate, mirror, cipher, riddle — above).
- **Random events** (`random`) — a storm, a lucky coin, a Bug Monster ambush.
- **Win / Lose** endings.
- **Achievements** printed at the end (e.g. "Bug Hunter", "Treasure Finder").
- **Replay** ("Play again? y/n").
- Code **organized into functions**, with clear names and comments.

### Structure target (teaches clean code without saying "clean code")
```
treasure_quest/
├── main.py            # the game loop + menu (the console)
├── story.py           # text and narration (intro, transitions, endings)
├── minigames.py       # the reused mini-games: chest, gate, mirror, cipher, riddle
└── README.md          # how to run it
```

### Definition of "done" for v1
- Runs start-to-finish with no crashes on expected input.
- A 12-year-old who didn't write it can play it and smile.
- Uses only Volume I skills.
- Each mini-game is recognizably one the Builder built earlier (the "that's MINE!" moment).
- The child can say, honestly: **"I built this."**

---

# Version 2 — Growing the Adventure (Volume II)

Same game, evolved. Adds: **inventory**, **NPCs & shops**, **save/load to a file**,
**multiple maps**, better monsters and dialogue. Introduces dictionaries in depth, files,
modules, and error handling — *because the bigger game needs them.*

**This is where the menu-of-adventures becomes tight-woven** (the seed planted in v1): with
inventory and state, the chest can drop a key the player *carries* to the gate; choices start to
*matter* across stops; the world connects into one journey instead of a list. That evolution is
the whole point of Volume II — *"I made it bigger,"* and *"the pieces now talk to each other."*

Target feeling: *"Wow, this already feels like a real indie game."*

---

# Version 3 — The Living World (Volume III)

Same game, rebuilt on solid architecture. Adds a real **UI** (web-first if feasible),
**images, sound, animation**, via **OOP** and **event-driven** design. Packaged and
**published** so the child can share a URL.

Target feeling: *"People I don't know can play my game."*

---

# Version 4 — The Infinite Guild (Volume IV)

Same game, now intelligent. Adds **AI NPCs**, **AI-generated quests / maps / dialogue**,
**AI hints**, an **AI companion** — plus real **deployment** and **GitHub collaboration**.

Target realization: *"I can build applications **with** AI — not just use AI."*

---

## The consistency check (run before shipping any version)

- Is it the **same game**, evolved — not a new one? ✅ required
- Do the **canonical characters** appear and behave per `CHARACTERS.md`? ✅
- Does it use **only** the skills taught up to this volume? ✅
- Can the child clearly say what they achieved and what's next? ✅
- Is it a **real, runnable donut**? 🍩 ✅

---

🏴‍☠️ *One game. Four generations. The Builder grows with the game; the game grows with the Builder.*

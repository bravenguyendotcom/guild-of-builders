# 🥋 The Typing Dojo

### An arcade inside the Guild — where Builders train by typing real code

> **Status:** v1.0 (frozen system spec — the *format*, not the content).
> **What this is:** the **place**. Inside it live the **canonical engines** (`coding_gold_mine/`)
> and the **mission skins** (`missions/`).
> **What this is NOT:** a classroom, a workbook, or another lesson. The teaching lives in the
> main story (*Captain Byte's Treasure Quest*). The Dojo only lets fast Builders **linger,
> train, and get quietly hooked.**

---

## The one-line soul

> **Type. Run. Smile. Learning Computer Science is a wonderful side effect.**

A Builder thinks they're practicing typing.
Actually, they're building Python fluency — and meeting beautiful ideas so many times, in so
many disguises, that one day those ideas feel like old friends.

*The Art of Teaching Without Any Teaching.*

---

## Why the Dojo exists (its only jobs)

- Practice typing (precision at the keyboard).
- Reward quick learners so they're never bored (the Fast Track, see `BUILDERS_LOGBOOK.md`).
- Keep them inside the Guild universe.
- Quietly expose them to cool ideas.
- **Success test:** if one kid goes home and Googles *"what is A*?"* because of a side-quest,
  the Dojo has done its job.

It never competes with the story. It's the arcade room Captain Byte would lose hours in. 🕹️

---

## The big idea: Engine + Skin (this is what makes it scale)

We do **not** write missions from scratch. We **assemble** them.

```
Mission  =  Engine (the Python program)
          + Skin   (the story hook + Guild flavor)
          + Challenge I  (Passive Memory)
          + Challenge II (Detective Mode)
```

One canonical `bfs.py` can wear many skins — Maze Escape, Robot Vacuum, Fire Rescue, Treasure
Map, Alien Cave. Same code, different imagination. (Nintendo has done this for decades.)

**So the durable asset is not the missions. It's the library of canonical programs.**
Everything else is a creative wrapper around it.

### Three layers (keep them DRY)

- **Layer 1 — Canonical Program** (`coding_gold_mine/`): written **once**, the source of truth
  (e.g. `bfs.py`). Improve it once, every mission using it improves.
- **Layer 2 — Mission** (`missions/`): a lightweight **skin** over an engine (many per engine).
- **Layer 3 — Main Story** (`manuscript/`): if/when the concept deserves *real* teaching, the
  main adventure does it properly — at the right time. The Dojo never pre-teaches.

---

## Folder structure

```text
typing_dojo/
├── README.md                 ← this spec
├── coding_gold_mine/         ← Layer 1: canonical engines (the real treasure)
│   ├── 001_guess_the_number.py
│   ├── 002_hangman.py
│   └── ...
└── missions/                 ← Layer 2: skins over the engines
    ├── 001_guess_the_number/
    │   ├── README.md          ← the mission (one screen)
    │   ├── challenge_1.py     ← the clean program to type
    │   └── challenge_2.py     ← same program, seeded with typos
    └── ...
```

Nothing fancy. Git-friendly. One screen per mission.

---

## The four tiers (a mastery ladder — each trains a different faculty)

The Dojo grows with the Builder. Each tier **unlocks by skill** (per `DECISIONS.md` D-16 logic),
so later tiers naturally arrive in later volumes.

| Tier | The question it asks | You train your... | Earliest |
|------|----------------------|-------------------|----------|
| 🥋 **Typing Dojo** | Can your *fingers* be precise? | fingers | Volume I |
| 🕵️ **Detective Mode** | Can your *eyes* spot mistakes? | eyes | Volume I |
| 🐉 **Dragon Debug's Den** | Can your *mind* find logic bugs? | reasoning | ~Volume II–III |
| ☁️ **The Lost Heaven** | Can you understand a whole *system* you've never seen? | systems thinking | ~Volume III–IV |

> **v1 builds only the first two tiers.** Dragon Debug's Den and The Lost Heaven are **design
> seeds only** — parked, not authored, because they need debugging/OOP/multi-file skills the
> Builder doesn't have yet. (They also carry a wink: in the Lost Heaven, *"find an AI companion"*
> — which loops straight into `HUMAN_AI_MANIFESTO.md`.)

---

## The mission format (frozen — one screen, nothing more)

```
Mission ####  —  Title

Story Hook          (2–5 lines, funny, in-world)

Challenge I         Passive Memory
Challenge II        Detective Mode

CS Seeds            (3–8 tags)

Guild Flavor        (1–3 lines — atmosphere, never a lesson)

Related Missions
```

No worksheets. No "Think First." No reflection. No explanation. **That belongs to the main
story, not here.**

### Challenge I — Passive Memory
Type the whole program. Run it. Any error is *probably your own typo* — hunt it, fix it, smile.
No need to analyze or understand it. If curiosity strikes, study it — but that's a bonus.

### Challenge II — Detective Mode
Same program, seeded with **typing mistakes only** — *never* logic or algorithm bugs. Retype it,
spot each typo, fix it as you go until it runs clean.
*"Excellent. Now the conversation begins."*

**Detective bug categories (typos only):** missing punctuation · wrong indentation · wrong
variable/function name · missing quote · wrong bracket · wrong keyword case · missing underscore
· wrong operator · small spelling slip. **Never an algorithm bug.**

---

## Rules for every canonical program

- ✅ executable · ✅ self-contained · ✅ terminal-based · ✅ readable · ✅ canonical
- ✅ beautiful output whenever possible · ✅ under ~250 lines
- ❌ no external dependencies unless truly necessary

---

## Guild Flavor (keep it to 3 lines, never a lesson)

Just atmosphere that reminds the Builder they're still in the Guild:

- 🏴‍☠️ *Captain Byte:* "I'm sure I can sort these faster." *(He couldn't.)*
- 🐉 *Dragon Debug:* "When the answer hides — don't search everywhere."
- 🦆 *Professor Quackers:* Quack.
- 🎨 *Professor Pycasso* types ASCII art just because it's beautiful.

Wonder first, explanation later. End each mission with **one** 3-line teaser that plants
curiosity — never a paragraph.

---

## Strategic repetition (intentional, not accidental)

Normal software says *"Don't repeat yourself."* The Dojo whispers the opposite to the *learner*:

> **Meet the same beautiful idea hundreds of times, in hundreds of adventures, until your
> fingers know it before your brain does.**

- The same engine returns under new skins (Binary Search as *Guess the Number*, then *Dragon
  searches a spellbook*, then *Search a billion stars*).
- **Echo Missions:** a later mission is secretly an earlier one in a new costume. The flash of
  *"wait — I've done this before!"* is the reward. That recognition **is** computer science.
- Internal author tags (never shown to kids): 🌱 Seed (first meeting) · 🌿 Sprout (repeat) ·
  🌳 Tree (fluent) · 🌲 Forest (everywhere).

---

## v1.0 scope — freeze it here

- **Build the format, not the mountain.** v1 = **10 missions** (Batch 01), Tiers 1–2 only.
- **Mission 001 is the template.** Build it fully, get it right, then produce the next nine
  fast and consistent.
- **Minimal metadata for v1** (authors/teachers only, never shown to kids):
  `ID · Title · CS Seeds · Prerequisites · Related`. Everything richer (Fun Factor, Visual
  Reward, Concept Density…) is parked until it earns its place.

### Batch 01 — the first ten (order = when they naturally fit Volume I)

| # | Mission | Why it's satisfying to type | CS Seed |
|---|---------|------------------------------|---------|
| 001 | Guess the Number | interactive, instant success | randomness, loops |
| 002 | Hangman | a real game | strings, lists |
| 003 | Caesar Cipher | secret messages | cryptography |
| 004 | Bubble Sort Race | ASCII animation | sorting |
| 005 | Binary Search | "magic" guessing | divide & conquer |
| 006 | Maze Escape | beautiful terminal output | BFS |
| 007 | Conway's Game of Life | mesmerizing patterns | emergence |
| 008 | Markov Story Generator | funny text | probability, "AI" |
| 009 | A* Pathfinder | smart pathfinding | heuristic search |
| 010 | Tiny Chatbot | feels like "AI" | rules, pattern matching |

Sweet spot: **90% typing practice · 10% Guild flavor · 100% authentic Computer Science.**
The first seven are simply *fun programs*; only the last three are "classic algorithms" —
right for a reader still in Volume I.

---

## What the Dojo must never become

- ❌ a classroom, a lecture, or another workbook
- ❌ required (skipping every mission still reaches 🏛️ Guild Builder)
- ❌ a leaderboard against other kids (race yourself — `DECISIONS.md` D-15)
- ❌ borrowed IP (original creatures & skins only — D-19)
- ❌ the 300-mission mountain *today* (that's the multi-year dream; v1 is ten)

---

🥋 *Keep typing. Keep smiling. One day you'll look back and realize you accidentally became a Builder.* 🏴‍☠️🐉🍩

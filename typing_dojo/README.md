# 🥋 The Typing Dojo

### An arcade inside the Guild — where Builders train by typing real code

> **Status:** v1.1 (system spec). Updated for `DECISIONS.md` **D-27–D-30**: finalized tier
> names, the owner/guardian, the honor rule, and the in-book vs. URL gate.
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

*The Art of Teaching Without Any Teaching* (`docs/PHILOSOPHY.md`).

---

## Who runs it — Dragon Debug & The Tangle (D-27)

The Dojo has an **owner** and a **guardian**, and they're a double-act:

- 🐉 **Dragon Debug — the owner.** He built the Dojo as a calm training hall. He sips his tea,
  watches you type, and says *"Interesting."*
- 🦑 **The Tangle — the guardian.** A ten-tentacled Typo-Squid (an original creature, D-19) that
  feeds on sloppy typing.

The running secret: Dragon Debug *pretends* the squid is a nuisance he "hasn't gotten around to
removing" (*"one day I'll deal with that squid…"*) — but he keeps it **on purpose.** A Dojo with
nothing to push against teaches nothing. Type cleanly enough and The Tangle isn't *defeated* —
it gets **bored and impressed**, and wanders off to find a sloppier Builder. Dragon Debug never
admits he planned it. **Quackers knows. Quackers says nothing.** 🦆

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

## The big idea: Engine + Skin (D-21 — this is what makes it scale)

We do **not** write missions from scratch. We **assemble** them.

```
Mission  =  Engine (the Python program)
          + Skin   (the story hook + Guild flavor)
          + the challenge tiers the topic deserves (see below)
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

## The four tiers (D-28 — a mastery ladder; each trains a different faculty)

Finalized names and taglines — **these are canon.** No sub-levels.

| Tier | Name & tagline | Trains your... | The challenge |
|------|----------------|----------------|---------------|
| 🥋 **I** | **Keyboard Ninja** — *"Slice your caps."* | **fingers** | Passive Memory: type the canonical program, run it, smile. Any error is probably your own typo. |
| 🕵️ **II** | **Conan's Challenge** — *"Do you have any clue?"* | **eyes** | Detective Mode: the code has **typos only — never logic bugs.** Find & fix them. |
| 🐉 **III** | **Dragon Debug's Den** — *"Welcome to the kingdom of bugs."* | **mind** | **Logic bugs allowed.** The observable input→output must match the canonical mission, but the *implementation may be twisted.* |
| ☁️ **IV** | **The Lost Heaven** — *"You may feel lost; befriend AI for help."* | **systems thinking** | Not a single file and **not typing**: a whole project folder to understand and fix to meet requirements. |

**On "Hell":** *Hell I–V* is only a **difficulty rating** of how brutal a Den (Tier III) mission
is — **not** a level name. A single Den mission is rated somewhere on that scale.

**Tiers = repetition, on purpose (D-23, D-28).** A mission carries **only the tiers its topic
deserves**: introductory topics ship **Tier I only**; important CS ideas earn more tiers —
*because more tiers = more times the idea is carved into memory.* A topic's tier-siblings may
publish as **separate mission IDs**, so a learner never knows they're the same idea in a new
costume.

### 🔒 The honor rule (D-28 — stated, and enforced culturally)

In **Tier III (Den)** and **Tier IV (Lost Heaven)**, you **must not open the Tier I / II
canonical source.** No peeking. That refusal is what makes the challenge real — it turns typing
practice into genuine code review and systems reasoning. Play fair, Builder.

---

## Where the tiers live — in the book vs. outside (D-29)

The gate is **always open — in and out of the book.** But *what appears where* differs:

- **Openly offered (no self-select needed):** **Tier I & II** appear at the **end of chapters
  from Chapter 6 onward**, freely repeating. This is the osmosis engine — it must be frequent
  and casual, so it's never hidden (this is the exception to D-24's "don't advertise").
- **Self-select only (quiet in-world sign, never a banner — D-24):** **Tier III & IV.**
- **In the book (gentle end only):** Tiers I–II freely; **Tier III only rarely, and only at
  Hell I–II** — so an "optional" chapter-end never sandbags a kid.
- **Outside the book (the wider Dojo, reachable by URL):** **Hell III–V** Den missions and
  **all of Tier IV** live here — for quick learners and contributors.

---

## The mission format (frozen — one screen, nothing more)

```
Mission ####  —  Title

Story Hook          (2–5 lines, funny, in-world)

Challenge(s)        the tier(s) this topic deserves (Keyboard Ninja / Conan's Challenge / …)

CS Seeds            (3–8 tags)

Guild Flavor        (1–3 lines — atmosphere, never a lesson)

Related Missions
```

No worksheets. No "Think First." No reflection. No explanation. **That belongs to the main
story, not here.**

### Tier I — Keyboard Ninja (Passive Memory)
Type the whole program. Run it. Any error is *probably your own typo* — hunt it, fix it, smile.
No need to analyze or understand it. If curiosity strikes, study it — but that's a bonus.

### Tier II — Conan's Challenge (Detective Mode)
Same program, seeded with **typing mistakes only** — *never* logic or algorithm bugs. Retype it,
spot each typo, fix it as you go until it runs clean.
*"Excellent. Now the conversation begins."*

**Detective bug categories (typos only):** missing punctuation · wrong indentation · wrong
variable/function name · missing quote · wrong bracket · wrong keyword case · missing underscore
· wrong operator · small spelling slip. **Never an algorithm bug.**

### Tier III — Dragon Debug's Den (logic bugs allowed)
The code runs, but the output may be wrong. Read, think, debug. **Fairness rule:** the
input→output must still match the canonical mission; the implementation may be twisted
(for↔while, recursion↔iteration, dict↔list, built-in↔hand-rolled). Reward:
*"Dragon Debug smiles. 'You fixed more than the code. You fixed the idea.'"*

### Tier IV — The Lost Heaven (systems, not typing)
A whole project folder. Understand it, then fix it to meet the requirements. Patterns and design.
The tip is honest: *find an AI companion* — which loops straight into `HUMAN_AI_MANIFESTO.md`.

---

## Rules for every canonical program

- ✅ executable · ✅ self-contained · ✅ terminal-based · ✅ readable · ✅ canonical
- ✅ beautiful output whenever possible · ✅ under ~250 lines
- ✅ **include the expected output** (so a Builder typing along in IDLE/an IDE can confirm success)
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

## Strategic repetition (intentional, not accidental — D-23)

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

## Scope — the book vs. the growing library (D-30)

- **In the book:** roughly **one Dojo mission per chapter (~50 across the series)** — topics
  chosen carefully, multiplied by tier-variants and skins.
- **Outside the book:** the wider library grows over time, built by curious Builders and
  contributors, reachable by URL. **We build the framework to practice and to inspire** — the
  library scales through contribution, not by authoring hundreds up front.
- **We record the *system* as canon; we do NOT commit to 300–500 programs** — that's the
  long-term dream, parked, not a promise. *v1 > perfection.*

### v1.0 build order (unchanged)

- **Build the format, not the mountain.** Start with **Batch 01** (~10 missions), Tiers I–II.
- **Mission 001 is the template.** Build it fully, get it right, then produce the rest fast and
  consistent.
- **Minimal metadata for v1** (authors/teachers only, never shown to kids):
  `ID · Title · CS Seeds · Prerequisites · Related`. Everything richer (Fun Factor, Visual
  Reward, Concept Density…) is parked until it earns its place.

---

## What the Dojo must never become

- ❌ a classroom, a lecture, or another workbook
- ❌ required (skipping every mission still reaches 🏛️ Guild Builder)
- ❌ a leaderboard against other kids (race yourself — `DECISIONS.md` D-15)
- ❌ borrowed IP (original creatures & skins only — D-19)
- ❌ the 300-mission mountain *today* (that's the long-term dream; v1 is a small batch)

---

🥋 *Keep typing. Keep smiling. One day you'll look back and realize you accidentally became a Builder.* 🏴‍☠️🐉🍩

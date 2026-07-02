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

### Required features
- An **intro story** (Captain Byte sets sail for treasure).
- **Choices** that branch the path (`if`/`elif`/`else`).
- At least one **mini-game** reused from the missions (e.g. guess-the-number to open a chest,
  or a password/riddle gate).
- **Random events** (`random`) — a storm, a lucky coin, a Bug Monster ambush.
- **Win / Lose** endings.
- **Achievements** printed at the end (e.g. "Bug Hunter", "Treasure Finder").
- **Replay** ("Play again? y/n").
- Code **organized into functions**, with clear names and comments.

### Structure target (teaches clean code without saying "clean code")
```
treasure_quest/
├── main.py            # the game loop + menu
├── story.py           # text and narration
├── minigames.py       # guess-the-number, riddle gate, etc.
└── README.md          # how to run it
```

### Definition of "done" for v1
- Runs start-to-finish with no crashes on expected input.
- A 12-year-old who didn't write it can play it and smile.
- Uses only Volume I skills.
- The child can say, honestly: **"I built this."**

---

# Version 2 — Growing the Adventure (Volume II)

Same game, evolved. Adds: **inventory**, **NPCs & shops**, **save/load to a file**,
**multiple maps**, better monsters and dialogue. Introduces dictionaries in depth, files,
modules, and error handling — *because the bigger game needs them.*

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

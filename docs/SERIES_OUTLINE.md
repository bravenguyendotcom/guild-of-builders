# 🗺️ SERIES_OUTLINE.md

### The whole series from 30,000 feet — every volume, every chapter

> **Status:** Volume I is **near-canon** (maps to the existing mission ladder). Volumes II–IV
> are a **compass, not a contract** — directional outlines, revised as each volume's real game
> state comes to exist. (Per canon: we don't fully draft a volume before the previous game
> is built.)
>
> **This file is the map. The detail lives elsewhere:** skills → `CURRICULUM.md`; game
> evolution → `GAME_DESIGN.md`; how chapters read → `STYLE_GUIDE.md`; who appears → `CHARACTERS.md`.
>
> **Chapter entries are compact on purpose:** Story (the beat) · Learn (Python/CS) ·
> Game (how the Quest evolves) · Real World 🏗️ (the professionalism rung) · Cast.

---

## The spine of the whole journey

One game. Four generations. The Builder grows with the game.

| Vol | Role | The child can say... | Pro-ladder rung 🏗️ |
|-----|------|----------------------|---------------------|
| **I** | The First Voyage | "I built a game." | **Vocabulary** — the trade has names |
| **II** | Growing the Adventure | "I made it bigger." | **Rituals** — plan, standup, iterate |
| **III** | The Living World | "People can play my game." | **Artifacts** — README, demo, present |
| **IV** | The Infinite Guild | "I build *with* AI." | **The room** — propose, collaborate, belong |

The ultimate goal lands in **Volume IV, Chapter 11**: the Builder proposes and ships a
solution to a *real* problem, with confidence. Everything before it is the climb to that rung.

---

# 📘 VOLUME I — The First Voyage
**Python:** basics (CLI). **Deliverable:** *Treasure Quest v1* — a playable, shareable text game.
**Rung:** vocabulary — every skill quietly gets its real-world name.
*(Chapters map to the 20-mission ladder in `CURRICULUM.md`.)*

**Ch 0 — Welcome: The Ship That Needs You** *(shipped)*
- Story: Captain Byte, alone in a storm on a leaking ship, needs a Builder.
- Learn: the Builder's mindset — *"Version 1 beats a blank page."*
- Game: you join the Guild and set sail.
- 🏗️: *source code* — the words a Builder types are called this.

**Ch 1 — The First Line** *(shipped)*
- Story: the first thing you ever tell the computer.
- Learn: `print` / `input`; name your captain.
- Game: the game greets *you* by name.
- 🏗️: *program* · Cast: Dragon Debug arrives (the tea 🐉☕).

**Ch 2 — The Hungry Robot** 🍕
- Story: the ship's cook can't count the provisions.
- Learn: variables, string formatting (Mission 1).
- Game: track supplies for the voyage.
- 🏗️: *variable*.

**Ch 3 — The Fork in the Tide**
- Story: two channels, one ship — how does a program *choose*?
- Learn: booleans + `if`/`elif`/`else` (Mission 2).
- Game: your first branching choice.
- 🏗️: *conditional* · Cast: **Sir Boolean** debuts (green TRUE / red FALSE).

**Ch 4 — Numbers of the Sea** 🪙
- Story: trading gold at a pirate port.
- Learn: arithmetic, integer division & modulo (Missions 3–4).
- Game: the treasure/gold currency is born.
- 🏗️: *operator*.

**Ch 5 — The Forest of Loops** 🌲
- Story: the same path, again and again, until you learn to repeat *on purpose*.
- Learn: `while`/`for`, `range`, `break`/`continue`.
- Game: repeating encounters and turns.
- 🏗️: *loop / iteration* · Cast: **Professor Loop**.

**Ch 6 — The Guessing Cave** 🕯️
- Story: a locked chest that answers "higher" or "lower."
- Learn: guess-the-number logic (Mission 6).
- Game: the chest-opening mini-game (reused in the capstone).
- 🏗️: *algorithm*.

**Ch 7 — The Locked Gate** 🔐
- Story: only the right words open the inner island.
- Learn: `and`/`or`/`not`, precise checks (Mission 7).
- Game: a gate guarding the next area.
- 🏗️: *validation*.

**Ch 8 — The Riddle Theatre** 🎭
- Story: two ridiculous hosts block the road with wordplay.
- Learn: strings — palindromes, Caesar cipher (Missions 9–10).
- Game: a riddle-gate mini-game.
- 🏗️: *string* · Cast: **Maestro Monty & Sir Quizzalot** debut 🤡🥁.

**Ch 9 — The Grand Library** 📚
- Story: shelves of monsters, heroes, and junk to sort.
- Learn: lists & dictionaries (Missions 8, 12, 14).
- Game: a simple inventory and monster stats.
- 🏗️: *data structure*.

**Ch 10 — The Bug Monster's Lair** 👾
- Story: everything breaks. Good. *"Excellent. Now the conversation begins."*
- Learn: reading errors, Rubber Duck debugging.
- Game: a bug-hunt sequence.
- 🏗️: *bug / stack trace* · Cast: **Bug Monster**, **Professor Quackers** 🦆.

**Ch 11 — The Workshop of Tools** 🛠️
- Story: you keep rebuilding the same thing — until you forge a reusable tool.
- Learn: functions; Don't Repeat Yourself.
- Game: refactor repeated code into clean functions.
- 🏗️: *function / DRY* · Cast: Dragon Debug (*"make it clear"*).

**Ch 12 — The Painter's Deck** 🎨
- Story: a game can be *beautiful*, not just correct.
- Learn: ASCII art, formatted & colored output.
- Game: a title screen and prettier text.
- 🏗️: *user experience* · Cast: **Professor Pycasso** (*"every program is a canvas"*).

**Ch 13 — The Escape Room** 🚪
- Story: one door, guarded by everything you've learned.
- Learn: combine guessing + strings + logic + math (Mission 19).
- Game: the pre-capstone integration puzzle.
- 🏗️: *integration*.

**Ch 14 — Captain Byte's Treasure Quest v1** 🏴‍☠️ *(capstone / donut)*
- Story: the full voyage, start to treasure.
- Learn: assemble it all into one clean, organized program (Mission 20).
- Game: **the complete CLI game — shipped.**
- 🏗️: *definition of done / shipping v1* · Achievement: **CLI Builder** 💻.

---

# 📗 VOLUME II — Growing the Adventure
**Python:** data structures in depth, files, modules, `try`/`except`. **Deliverable:** *Treasure Quest v2* (same game, evolved).
**Rung:** rituals — plan before you build; iterate in small steps.

**Ch 1 — The Map Grows** — Story: the crew dreams bigger; Dragon Debug says *plan first.*
Learn: writing a tiny spec. Game: the v2 wishlist. 🏗️: *spec / requirements.*

**Ch 2 — The Knapsack** — Story: too much loot, no pockets. Learn: lists & dicts in depth.
Game: a real inventory system. 🏗️: *state.*

**Ch 3 — The Merchant's Wharf** — Story: a shopkeeper who haggles. Learn: functions that
return values, nested data. Game: buying & selling; first true NPC. 🏗️: *interface.*

**Ch 4 — When Things Go Wrong** — Story: Captain Byte feeds the ship nonsense and it sinks.
Learn: `try`/`except`, graceful failure. Game: the game stops crashing on bad input. 🏗️: *exception / edge case.*

**Ch 5 — The Memory Stone** — Story: a stone that remembers your journey. Learn: reading &
writing files (save/load). Game: **save and continue.** 🏗️: *persistence.* Cast: Quackers (check it saved).

**Ch 6 — The Cartographer** — Story: a world with many rooms. Learn: data-driven maps
(dicts of rooms). Game: a multi-location world. 🏗️: *data-driven design.* Cast: **Ninja Cat** (navigation).

**Ch 7 — The Toolmakers' Guild** — Story: one giant scroll is impossible to carry. Learn:
modules & `import`; split the code. Game: the game becomes many tidy files. 🏗️: *modules / codebase.*

**Ch 8 — The Bestiary** — Story: monsters with real personalities. Learn: weighted randomness,
data-driven creatures. Game: richer, fairer encounters. 🏗️: *configuration.* Cast: Bug Monster evolves.

**Ch 9 — The Riddle Theatre Returns** 🎭 — Story: Monty & Quizzalot upgrade their act. Learn:
dictionaries of riddles/dialogue. Game: puzzle NPCs. Cast: **Monty & Quizzalot.**

**Ch 10 — The Standup** — Story: a daily two-minute check-in with the Captain. Learn: tracking
a tiny backlog, working in iterations. 🏗️: *standup / backlog / iteration.*

**Ch 11 — Pycasso's Palette** 🎨 — Story: color comes to the terminal. Learn: ANSI color,
formatted tables, simple art. Game: a handsome text UI. Cast: **Pycasso.**

**Ch 12 — Treasure Quest v2** *(capstone / donut)* — the **same** game, grown up. Achievement: **World Builder** 🗺️.

---

# 📙 VOLUME III — The Living World
**Python:** OOP, architecture, event-driven UI, assets, packaging, publishing (web-first).
**Deliverable:** *Treasure Quest v3* — a **published** game with a shareable URL.
**Rung:** artifacts — a README strangers can use; a demo you present with confidence.

**Ch 1 — The Blueprint** — Story: the ship's too big to hold in your head. Learn: thinking in
objects (nouns of the game). 🏗️: *architecture.*

**Ch 2 — Meet the Class** — Story: Player, Monster, Item become *things* with their own powers.
Learn: classes & objects. Game: entities refactored into classes. 🏗️: *class / object.* Cast: Dragon Debug (design).

**Ch 3 — Inheritance Island** — Story: a family of monsters. Learn: inheritance & polymorphism.
Game: a monster hierarchy. 🏗️: *reuse.*

**Ch 4 — The Stage Appears** — Story: the game gets a *screen.* Learn: GUI/web, event-driven
programming (clicks, input). Game: the first real window. 🏗️: *event loop / UI.*

**Ch 5 — Pycasso's Canvas** 🎨 — Story: pixels, sprites, real color. Learn: graphics, images,
layout. Game: a visual game board. Cast: **Pycasso** (headline role).

**Ch 6 — The Sound of Adventure** — Story: the world makes noise and moves. Learn: audio,
animation, feedback. Game: sound & motion. 🏗️: *assets.*

**Ch 7 — The State Machine** — Story: menu → play → win/lose, cleanly. Learn: managing game
state. 🏗️: *state management.*

**Ch 8 — Packing the Ship** — Story: getting the game ready to leave home. Learn: packaging,
dependencies. 🏗️: *dependencies / build.*

**Ch 9 — The Lighthouse** — Story: a light others can find. Learn: deployment, hosting.
Game: **a shareable URL.** 🏗️: *deployment.*

**Ch 10 — The README for Strangers** — Story: someone you'll never meet wants to play. Learn:
writing docs a stranger can follow. 🏗️: *documentation.*

**Ch 11 — Demo Night** — Story: you show the family what you built. Learn: presenting with
confidence. 🏗️: *demo / presentation.*

**Ch 12 — Treasure Quest v3** *(capstone / donut)* — the **published** game. Achievement: **Game Publisher** 🌍.

---

# 📕 VOLUME IV — The Infinite Guild
**Python:** AI APIs, prompt engineering, agents, automation, Git/GitHub, collaboration, ethics.
**Deliverable:** *Treasure Quest AI* — **plus the confidence to build original things.**
**Rung:** the room — propose solutions, collaborate, belong among real Builders.

**Ch 1 — A New Kind of Crew** — Story: a strange new mate joins — brilliant, but not always
right. Learn: what AI is and isn't; teammate, not oracle. 🏗️: *AI as a tool; responsibility first.*

**Ch 2 — The Talking Parrot** 🦜 — Story: an NPC that truly talks. Learn: your first AI API
call; prompt basics. Game: an AI-powered character. 🏗️: *API / prompt.*

**Ch 3 — The Art of Asking** — Story: ask badly, get nonsense; ask well, get magic. Learn:
prompt engineering — clarity, examples, verification. 🏗️: *prompt engineering.*

**Ch 4 — The AI Quartermaster** — Story: endless quests, maps, and dialogue. Learn: injecting
AI-generated content into the game. Game: **infinite quests.** Cast: Captain Byte over-trusts the AI...

**Ch 5 — The Honest Duck** 🦆 — Story: ...and it makes something up. Learn: hallucination &
verification — never trust blindly. 🏗️: *testing AI output.* Cast: **Professor Quackers** (check your work).

**Ch 6 — The Companion** — Story: a helper that gives hints, not answers. Learn: build an AI
hint/companion system. Game: an in-game AI guide. 🏗️: *human-in-the-loop.*

**Ch 7 — Agents & Automation** — Story: teaching the crew to do chores themselves. Learn:
chaining steps; simple agents/automation. 🏗️: *agent / automation.*

**Ch 8 — The Guild Repository** — Story: the whole Guild works on one codebase. Learn: Git &
GitHub for real — branches, commits, pull requests. 🏗️: *version control / pull request* (the Vol I word *code review*, now lived).

**Ch 9 — Working With Others** — Story: two Builders, one game, zero chaos. Learn: issues,
reviews, teamwork; speaking like an engineer/PM. 🏗️: *collaboration.*

**Ch 10 — Ethics of the Builder** — Story: with power comes *"make it kind."* Learn:
responsibility, bias, privacy, safety. 🏗️: *responsible AI.* Cast: Dragon Debug (the creed completes).

**Ch 11 — The Real Problem** ⭐ — Story: a real need — at home, at school, in the world. Learn:
propose and build a genuine solution; pitch it with confidence. 🏗️: **proposing a solution / the pitch.**
*(This is the series' ultimate goal, realized.)*

**Ch 12 — Treasure Quest AI & The Infinite Guild** *(capstone / donut)* — the AI-powered game
ships, and the Builder is ready to build things no book planned. Achievement: **Guild Builder** 🏛️ — *you belong in the room.*

---

## Notes for authors

- **Chapter counts are provisional** (currently ~14 / 12 / 12 / 12). Ship v1 of the outline;
  refine per volume. Kaizen.
- **Every chapter must feed the Quest.** If a chapter doesn't evolve the game or the Builder,
  question it (North Star).
- **Volumes II–IV will shift** once each prior game state exists. Treat them as direction.
- Detailed skills stay in `CURRICULUM.md`; this file is the bird's-eye map only.

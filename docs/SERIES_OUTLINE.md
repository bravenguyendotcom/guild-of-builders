# 🗺️ SERIES_OUTLINE.md

### The whole series from 30,000 feet — every volume, every chapter

> **Status:** Volume I is **in production** (chapters 0–7 shipped; 8–15 planned). Volumes II–IV
> are a **compass, not a contract** — directional outlines, revised as each volume's real game
> state comes to exist. (Per canon: we don't fully draft a volume before the previous game
> is built.)
>
> **This file is the map. The detail lives elsewhere:** skills → `CURRICULUM.md`; game
> evolution → `GAME_DESIGN.md`; how chapters read → `STYLE_GUIDE.md`; who appears → `CHARACTERS.md`;
> side-quests → `SIDE_QUESTS.md` + `typing_dojo/`.
>
> **Chapter entries are compact on purpose.**
> **Core fields (most chapters):** Story (the beat) · Learn (Python/CS) · Game (how the Quest
> evolves) · 🏗️ Real World (the professionalism rung) · Cast · Achievement (badge earned).
> **Optional threads (shown only when a chapter has one):**
> 🥋 **Dojo** — a Typing Dojo mission unlocks here (by skill; see `typing_dojo/`) ·
> 🎭 **Riddle/Joke** — a riddle or joke beat (Monty & Quizzalot / the Joke Board) ·
> 🎨 **Art** — a "make it beautiful" beat (Pycasso) ·
> 🖼️ **Advanced Gallery** — a 3D/motion CLI art showpiece (skill-gated; `PYCASSO_GALLERY_ADVANCED.md`) ·
> 🌫️ **Fog Creature** — the inner enemy this chapter quietly helps a Builder face.

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
*(**Volume I is complete — Chapters 0–15 all shipped**, and every Dojo mission (001–010) built.
The capstone game ships in `source_code/volume_1/treasure_quest/`. Skill detail lives in
`CURRICULUM.md`.)*

**Ch 0 — Welcome: The Ship That Needs You** *(shipped)*
- Story: Captain Byte, alone in a storm on a leaking ship, needs a Builder.
- Learn: the Builder's mindset — *"Version 1 beats a blank page."* (story only, no syntax)
- Game: you join the Guild and set sail.
- 🏗️: *source code*.
- 🌫️ Fog Creature: the Fog of "I Can't" (the first, gentlest meeting).

**Ch 1 — Captain Byte Sets Sail** *(shipped)*
- Story: the Captain keeps losing the treasure number — so the ship remembers it for him.
- Learn: **variables** (a box with a name); the first `NameError` as a conversation.
- Game: the ship remembers and greets by name.
- 🏗️: *state* · Cast: Dragon Debug arrives (tea 🐉☕), Professor Quackers 🦆, TommyBot (*"is you"*).
- Achievement: **Rookie Python** 🐍.

**Ch 2 — The Hungry Pizza Robot** 🍕 *(shipped)*
- Story: the ship's kitchen must ask how many slices — and listen.
- Learn: **`input`** (ask + listen); the classic *"input is always text"* bug (`"3" * 2 == "33"`),
  fixed with **`int`**.
- Game: the ship holds a real conversation with the user.
- 🏗️: *input / user* · Achievement: **Conversation Starter** 💬.

**Ch 3 — The Age Machine** ⏳ *(shipped)*
- Story: the ship won't hand over the wheel until it *decides* you're old enough.
- Learn: **`if` / `elif` / `else`** and comparisons (`>=`, `<=`, `==`, `>`, `<`).
- Game: the ship makes its first decision.
- 🏗️: *conditional*.

**Ch 4 — The Ninja Health Check** 🥷 *(shipped)*
- Story: the Cliffs of Health demand a *calculated* readiness score.
- Learn: **`float`** (numbers with a dot), operators `*` `/` with bracket precedence, **`round()`**;
  the `int("1.5")` **ValueError** as a conversation.
- Game: the ship computes, not just remembers.
- 🏗️: *operator* · Cast: **Ninja Cat** debuts 🐱.

**Ch 5 — Rock, Paper, Scissors** ✊ *(shipped)*
- Story: Captain Byte faces Ninja Cat and teaches the ship to be unpredictable.
- Learn: **`import`**, **`random.choice()`**, `=` vs `==`, the word **`and`**.
- Game: the game can surprise you — how games are born.
- 🏗️: *module / library* · Achievement: **Chance Dancer** 🎲.

**Ch 6 — The Secret Treasure** 🔁 *(shipped)*
- Story: a locked chest hides a number; guess it, cleverly, again and again.
- Learn: **`while`** loops, **`!=`**, **`random.randint()`**, the **infinite loop** (rite of passage),
  the **counter** pattern (`attempts = attempts + 1`). *(Seeds binary search via Ninja Cat's hint.)*
- Game: the chest-opening mini-game (reused later).
- 🏗️: *loop / iteration* · Achievement: **Loop Weaver** 🔁.
- 🥋 Dojo: **unlocks here** — Mission 001 *Guess the Number* becomes typeable (first `while` + `random`).
  *(Introduced by a quiet sign, not a banner — D-24.)*

**Ch 7 — The Safe Password Checker** 🔐 *(shipped)*
- Story: guard the treasure — one blurry `and`-guard lets `"password"` slip through.
- Learn: **booleans**, **`len()`**, the flag-words **`and` / `or` / `not`**; separate `if`/`elif`
  questions that explain *which* rule failed.
- Game: a gate guarding the next area.
- 🏗️: *validation* · Cast: **Sir Boolean** debuts 🛡️ · Achievement: **Flag Bearer** 🚩.
- 🥋 Dojo: Mission **002 The Bouncer** (a rules-checker: length + forbidden word). See `typing_dojo/MISSIONS_PLAN.md`.

---

**Ch 8 — The Recycling Robot** ♻️ *(shipped)*
- Story: a mountain of salvage to sort and count.
- Learn: counting a list *without* `.count()` (Mission 8).
- Game: sort/count the treasure pile.
- 🏗️: *iteration / accumulation*.
- 🥋 Dojo: Mission **003 Tally Machine** (count items in a list, no `.count()`). See `typing_dojo/MISSIONS_PLAN.md`.

**Ch 9 — The Palindrome Mirror** 🪞 *(shipped)*
- Learn: strings — reverse/compare *without* `reverse()` (Mission 9). 🏗️: *string*.
- Game: a mirror-word puzzle the game can use as a gate.
- 🥋 Dojo: Mission **004 Mirror, Mirror** (reverse & compare a string). See `typing_dojo/MISSIONS_PLAN.md`.

**Ch 10 — The Caesar Messenger** 🗝️ *(shipped)*
- Learn: character math, a simple cipher (Mission 10). 🏗️: *encoding*.
- Game: a secret coded message the player must decode to advance.
- 🥋 Dojo: Mission **005 Secret Cipher** (shift letters — Caesar; echoes this chapter). See `typing_dojo/MISSIONS_PLAN.md`.

**Ch 11 — The Riddle Theatre** 🎭 *(shipped)*
- Story: two ridiculous hosts block the road with wordplay.
- Cast: **Maestro Monty & Sir Quizzalot** debut 🤡🥁. 🏗️: *the show*.
- Game: riddle-asking characters who guard a path in the game.
- 🎭 Riddle/Joke: the Riddle Theatre & Guild Joke Board open (write-your-own invited).
- 🥋 Dojo: Mission **006 The Guessing Cave** 🔁 (an Echo of 001 — same engine, new skin, D-23). See `typing_dojo/MISSIONS_PLAN.md`.

**Ch 12 — Menus & Mini-Programs** ✅ *(shipped)*
- Learn: menu loops, list state — To-Do / Contact Book / shop (Missions 16–18). 🏗️: *state / CRUD*.
- Game: **the menu loop that becomes the game's main console** (the spine of the capstone).
- 🥋 Dojo: Mission **007 The Quest Log** (a menu loop over a list). See `typing_dojo/MISSIONS_PLAN.md`.

**Ch 13 — The Painter's Deck** 🎨 *(shipped)*
- Learn: ASCII art, formatted & colored output. Cast: **Professor Pycasso** (debut show). 🏗️: *user experience*.
- 🎨 Art: the "make it beautiful" thread opens (title screens, ASCII, colour).
- Game: a coloured title screen and prettier output for the game.
- 🥋 Dojo: Mission **008 The Sign Painter** (build ASCII art with loops). See `typing_dojo/MISSIONS_PLAN.md`.
- 🖼️ Advanced Gallery: **Matrix Rain** 🟢 — Pycasso's debut showpiece; the green code waterfall
  (lists + random + colour = motion). **Shown *and runnable* here** — the child runs it and watches
  it fall; the full build waits for Vol II. Built: `pycasso_gallery/matrix_rain.py`. See
  `PYCASSO_GALLERY_ADVANCED.md`.

**Ch 14 — The Escape Room** 🚪 *(shipped — pre-capstone)*
- Learn: combine guessing + strings + logic + math (Mission 19). 🏗️: *integration*.
- Game: the first time several mini-games join into one gated sequence — a dry run for the capstone.
- 🥋 Dojo: Mission **009 The Vault** 🔁 (Echo — combines guess + check, echoes 001/002). See `typing_dojo/MISSIONS_PLAN.md`.

**Ch 15 — Captain Byte's Treasure Quest v1** 🏴‍☠️ *(shipped — capstone / the volume's donut)*
- Learn: assemble it all into one clean, organized program (Mission 20).
- Game: **the complete CLI game — shipped.**
- 🏗️: *definition of done / shipping v1* · Achievement: **CLI Builder** 💻.
- 🥋 Dojo: Mission **010 The Ship's Console** 🔁 (Echo of 007 — a tiny menu tying it together). See `typing_dojo/MISSIONS_PLAN.md`.

> **Note:** chapter *count* is provisional — the shipped chapters reordered and expanded the
> original 14-chapter sketch (e.g. Sir Boolean now debuts at Ch 7, not Ch 3). The map follows
> the territory. `CURRICULUM.md`'s mission ladder remains the skill source of truth.

---

# 📗 VOLUME II — Growing the Adventure
**Python:** data structures in depth, files, modules, `try`/`except`. **Deliverable:** *Treasure Quest v2* (same game, evolved).
**Rung:** rituals — plan before you build; iterate in small steps.
**New this volume:** 🧭 **Lady-O-Query** joins the main cast (Ch 1). The **Fog Creatures** deepen
(Shortcut Serpent, Ego Gremlin), and the antagonist ladder begins its climb toward the visioned
Final Boss (see `VILLAINS.md`, D-37). *Soul: "it's alive" (the world grows into a place) → "my
family plays it" (the Widening Circle homecoming) — dare boldly, come home warmly.*

**Ch 1 — The Map Grows** — Story: the crew dreams bigger; Dragon Debug says *plan first* — and
**🧭 Lady-O-Query, the Navigator, joins the crew** (her entrance *is* the volume's opening note;
she owns Big-O / planning — see `CHARACTERS.md`, D-36). Cast: **Lady-O-Query debuts.**
Learn: writing a tiny spec. Game: the v2 wishlist. 🏗️: *spec / requirements.*
🖼️ Advanced Gallery: **Rocket Launch** 🚀 — *"let your dreams lift off!"* a rising rocket on a
growing exhaust trail (a moving sprite over time). See `PYCASSO_GALLERY_ADVANCED.md`.

**Ch 2 — The Knapsack** — Story: too much loot, no pockets. Learn: lists & dicts in depth.
Game: a real inventory system. 🏗️: *state.*

**Ch 3 — The Merchant's Wharf** — Story: a shopkeeper who haggles. Learn: functions that
return values, nested data. Game: buying & selling; first true NPC. 🏗️: *interface.*

**Ch 4 — When Things Go Wrong** — Story: Captain Byte feeds the ship nonsense and it sinks.
Learn: `try`/`except`, graceful failure. Game: the game stops crashing on bad input. 🏗️: *exception / edge case.*
🛡️ **Shield beat (D-39):** *never trust what a user types* — validation as a safety reflex, voiced by Lady-O.

**Ch 5 — The Memory Stone** — Story: a stone that remembers your journey. Learn: reading &
writing files (save/load). Game: **save and continue.** 🏗️: *persistence.* Cast: Quackers (check it saved).
🛡️ **Shield beat:** the first privacy touch — *what's safe to store, and what isn't?*

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
🖼️ Advanced Gallery: **Moon Landing** 🌙 — *"the eagle has landed"*; a lander descending with a
slowing (easing) touchdown. See `PYCASSO_GALLERY_ADVANCED.md`.

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
💾 **Cloud persistence (D-40):** the file→cloud upgrade — a **multiplayer high-score table**
("save it so your friend can see your score"). Concept-first (*shared data lives in a database, not
a file*), with a simple hosted database (e.g. Supabase) as the example; needs an account
(parent-aware). 🛡️ **Shield beat:** *data minimization* — store only a name and a score, never more.

**Ch 10 — The README for Strangers** — Story: someone you'll never meet wants to play. Learn:
writing docs a stranger can follow. 🏗️: *documentation.*

**Ch 11 — Demo Night** — Story: you show the family what you built. Learn: presenting with
confidence. 🏗️: *demo / presentation.*
🖼️ Advanced Gallery: **Starfield** ✨ — *"to infinity and beyond!"* flying forward through stars
(perspective by division — the first taste of 3D). See `PYCASSO_GALLERY_ADVANCED.md`.

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
🖼️ Advanced Gallery: **Rotating Sphere / Globe** 🌍 — a shaded planet spinning in text (3D→2D
projection + light shading). See `PYCASSO_GALLERY_ADVANCED.md`.

**Ch 5 — The Honest Duck** 🦆 — Story: ...and it makes something up. Learn: hallucination &
verification — never trust blindly. 🏗️: *testing AI output.* Cast: **Professor Quackers** (check your work).
🌫️ Fog Creature: the **Shortcut Serpent** — *"let the AI do it all."*

**Ch 6 — The Companion** — Story: a helper that gives hints, not answers. Learn: build an AI
hint/companion system. Game: an in-game AI guide. 🏗️: *human-in-the-loop.*

**Ch 7 — Agents & Automation** — Story: teaching the crew to do chores themselves. Learn:
chaining steps; simple agents/automation. 🏗️: *agent / automation.*

**Ch 8 — The Guild Repository** — Story: the whole Guild works on one codebase. Learn: Git &
GitHub for real — branches, commits, pull requests. 🏗️: *version control / pull request* (the Vol I word *code review*, now lived).
🖼️ Advanced Gallery: **The Spinning Donut** 🍩 — *the Gallery capstone.* The legendary a1k0n 3D
ASCII torus (trig + two-axis rotation + z-buffer + luminance shading), built from math you now
understand. See `PYCASSO_GALLERY_ADVANCED.md`.
  *(Lore: this is the Guild's own emblem. Early on, Dad joked that "**.md**" didn't mean Markdown
  — it meant **"Mommy's Donuts,"** the file he kept *promising* but never delivered. So the
  Guild's iron law became: never promise a donut you don't ship. That's why donuts sit beside
  the pizzas all through the book — and why the final showpiece is a donut you make **real**,
  spinning in 3D, right where Builders learn to ship for real.)*

**Ch 9 — Working With Others** — Story: two Builders, one game, zero chaos. Learn: issues,
reviews, teamwork; speaking like an engineer/PM. 🏗️: *collaboration.*

**Ch 10 — Ethics of the Builder** — Story: with power comes *"make it kind."* Learn:
responsibility, bias, privacy, safety. 🏗️: *responsible AI.* Cast: Dragon Debug (the creed completes).
🌫️ Fog Creature: the **Ego Gremlin** — *"you don't need reviews or teammates."*

**Ch 11 — The Real Problem** ⭐ — Story: a real need — at home, at school, in the world. Learn:
propose and build a genuine solution; pitch it with confidence. 🏗️: **proposing a solution / the pitch.**
*(This is the series' ultimate goal, realized.)*

**Ch 12 — Treasure Quest AI & The Infinite Guild** *(capstone / donut)* — the AI-powered game
ships, and the Builder is ready to build things no book planned. Achievement: **Guild Builder** 🏛️ — *you belong in the room.*

---

## Notes for authors

- **Chapter counts are provisional** (Vol I now ~15 shipped+planned; II–IV ~12 each). Ship v1
  of the outline; refine per volume. Kaizen.
- **Every chapter must feed the Quest.** If a chapter doesn't evolve the game or the Builder,
  question it (North Star).
- **Optional threads are optional.** Only tag 🥋 Dojo / 🎭 Riddle / 🎨 Art / 🌫️ Fog Creature on a
  chapter that genuinely carries that beat — don't force one onto every chapter. The map stays
  compact.
- **Dojo unlocks are by skill, quietly.** A 🥋 tag marks where a Typing Dojo mission first
  becomes *typeable*; the child meets it via a small sign, never a banner (D-24).
- **Volumes II–IV will shift** once each prior game state exists. Treat them as direction.
- **Volume I now follows the shipped manuscript** (chapters 0–7 real; 8–15 planned).
- Detailed skills stay in `CURRICULUM.md`; this file is the bird's-eye map only.

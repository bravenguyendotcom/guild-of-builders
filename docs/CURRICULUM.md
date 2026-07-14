# 🎓 CURRICULUM.md

### What your child actually learns — and why it's built this way

> **For parents, teachers, and authors.** This is the honest map of the computer science inside
> *The Guild of Builders*. If you know CS, read the pedagogy notes — they explain the *method*,
> not just the topics. If you don't, read the plain-language skills: your child is learning real
> programming, in the order a child actually absorbs it.
> **The promise:** no skill appears because "it's next in a textbook." Every skill appears because
> a story needs it, and a game the child is building needs it. Motivation first, syntax second.

---

## The method, in one minute (why a CS-literate parent can trust this)

Most beginner courses teach *topics* in a logical order: variables, then types, then loops, then
functions. Logical for the teacher — but a child doesn't wake up wanting to learn "loops." So we
invert it. We give the child a **problem they care about** (a locked chest, a coded message, a
guard at a gate), and the Python concept arrives as *the tool that solves it.* The concept is the
answer to a question the child is already asking.

Three principles a CS parent will recognize:

- **Concepts are introduced at the point of need, not the point of convenience.** Booleans arrive
  when a password guard has to be *exactly* right — not in a "data types" chapter. The need makes
  the concept stick.
- **Bugs are taught on purpose.** Every chapter contains a real, run-it-yourself bug (an infinite
  loop, a `ValueError`, an off-by-one). The child learns to *read an error message and reason* —
  the single most transferable skill in software, and the one most courses skip.
- **The whole volume builds one shippable thing.** Every mini-game the child writes is a piece of
  the final game. Learning accumulates into a deliverable, not a pile of exercises. The child ends
  able to say, honestly: *"I built this."*

This is *computational thinking* taught by osmosis: decomposition, pattern-recognition,
abstraction, and debugging, absorbed through story rather than lecture.

---

## Three threads that run through every volume (the Builder, not just the Python)

The Python is the vehicle. Three things ride alongside it, volume to volume:

- 🌱 **Builder's Heart** — emotional resilience: frustration, the stuck bug, the Debug Break,
  *"real developers have broken keyboards too."* Named and normalized, never shamed. The #1 reason
  a young learner quits isn't difficulty — it's discouragement, so we teach the heart to persevere.
- 🦸 **The Inverting Mentor** — across the four volumes the child shifts from *asking* to
  *answering*. By the final volume, the mentor asks *them* the questions. The curriculum isn't
  "more Python each year" — it's a child *becoming* a Builder.
- 🛡️ **The Builder's Shield** — security & privacy *awareness and good practice*, built as a habit:
  *"a real Builder makes it work — and thinks about who it protects."* Emerges in Volume II (voiced
  by Lady-O-Query) when the game first handles real data for real people. It teaches the **WHATs** —
  strong passwords, store only what you need, never trust input blindly, guard your keys — as
  reflexes, through light story-natural beats. **It never teaches the HOWs** (hacking, malware,
  social engineering) or heavy theory: *the Shield protects, it never arms* (D-39). A book that
  raises Builders teaches them to build things that protect people.

---

# Volume I — The First Voyage (Python basics → a real CLI game)

**Prerequisite:** none. **Deliverable:** *Captain Byte's Treasure Quest v1* — a playable,
shareable command-line game the child builds from the pieces they make along the way.

### What your child learns, chapter by chapter (the shipped order)

This is the real running order of the book — each skill tied to the story beat that motivates it.

| Ch | Story | Python concept (the tool the story needed) |
|----|-------|--------------------------------------------|
| 0 | The ship that needs a Builder | the Builder's mindset — *"Version 1 beats a blank page"* (no syntax yet) |
| 1 | The Captain keeps losing the treasure number | **variables**; reading a first `NameError` calmly |
| 2 | The kitchen must ask and listen | **`input`**; *"input is always text"* (`"3"*2 == "33"`), fixed with **`int`** |
| 3 | The ship won't hand over the wheel until you're old enough | **`if` / `elif` / `else`**, comparisons |
| 4 | The Cliffs of Health demand a readiness score | **`float`**, `*` `/`, bracket precedence, **`round()`**; a `ValueError` |
| 5 | Teach the ship to be unpredictable | **`import`**, **`random`**, `=` vs `==`, **`and`** |
| 6 | A locked chest hides a number — guess it | **`while`** loops, **`!=`**, `random.randint`, the **infinite loop**, the **counter** |
| 7 | Guard the treasure; a blurry guard lets `"password"` slip | **booleans**, **`len()`**, **`and`/`or`/`not`**, precise validation |
| 8 | A mountain of salvage to sort and count | **iteration over a list**, counting *without* `.count()` |
| 9 | A mirror that only lets a palindrome pass | **strings** — reversing/comparing *without* `reverse()` |
| 10 | A coded parchment points the way | **character math**, a simple **Caesar cipher** |
| 11 | Two hosts block the road with wordplay | putting logic + strings to work; write-your-own riddles |
| 12 | Little programs that remember | **menu loops** + **list state** (the console that will run the game) |
| 13 | Make it beautiful | **ASCII art**, formatted & **coloured output** (and the on/off nature of colour codes) |
| 14 | The Escape Room — every trick at once | **integration**: several mini-games joined into one gated sequence |
| 15 | **Assemble the whole game and ship it** | **functions (`def`)** — organizing it all into one clean, runnable program |

> **On functions:** they arrive *last*, at the capstone — on purpose. Functions answer a question
> the child has genuinely felt by Chapter 15: *"my code is sprawling and repeated — how do I give
> each piece a name and call it?"* Teaching `def` as the tool that turns five loose mini-games into
> one organized game is far stickier than teaching it abstractly in week two. (A light tease can
> appear earlier where menus make code repetitive.) This is the leap from *"I can write code"* to
> *"I can organize software"* — the most grown-up idea in the volume.

### Computational thinking woven throughout
Decomposition (break the treasure hunt into trials), pattern-recognition (the counter pattern
recurs), abstraction (a function hides messy detail behind a name), and dry-running/edge-cases
(what if the user types letters?). These are never lectured — they're practiced.

### The deliverable
*Captain Byte's Treasure Quest v1* — a menu-driven adventure where each trial is a mini-game the
child built earlier (the chest, the gate, the mirror, the cipher, the riddle), assembled with
functions into one game that runs start-to-finish, with win/lose, achievements, and replay. Uses
only Volume I skills, standard library only. **A friend or parent can actually play it.**

---

# Volume II — Growing the Adventure

**Prerequisite:** Volume I. **Deliverable:** *Treasure Quest v2* — the **same** game, evolved.
**Rung** 🏗️: *rituals* — plan before you build; iterate in small steps. **Circle:** for the people I love.

> *(Volumes II–IV below are the **planned** skill arc — they firm up chapter-by-chapter as each
> volume is written and shipped. The skills and order are real; the exact chapter details evolve.)*

**What your child learns (the skill arc):**

| Skill area | The tool the story needs |
|---|---|
| Data structures in depth | **lists, dicts, tuples, sets** — a real inventory, a world of rooms, a bestiary |
| Functions that give back | **`return` values, nested data** — a shopkeeper who haggles, a first true NPC |
| Graceful failure | **`try` / `except`** — the game stops crashing when fed nonsense |
| Persistence | **files (read/write)** — *save and continue*; the game finally *remembers* |
| Bigger codebases | **modules & `import`** — one giant scroll becomes many tidy files |
| Richer randomness | **weighted choices** — monsters with fairer, more interesting behaviour |
| The efficiency lens | **Big-O intuition** — Lady-O-Query joins and teaches you to *see* cost |

**The game grows:** inventory, NPCs, shops, save/load, multiple rooms, a bestiary. **This is where
the menu of adventures becomes one woven journey** — with state and memory, the number you crack
from the chest can become the key you carry to the gate. The child's own v1 ending planted this
itch; Volume II is the answer.

**New this volume — 🧭 Lady-O-Query joins**, the Navigator who teaches planning and thinks in Big-O.
And **🛡️ the Builder's Shield emerges** through her: *"never trust what a user types"* (input
validation as a safety reflex, not just a crash-fix), and the first privacy beat when the game
saves data — *"what's safe to store, and what isn't?"*

**What your child can now build:** programs that **remember** across runs (save files), handle bad
input without crashing, are organised across multiple files, and manage real state (inventories,
maps, records). This is the jump from *toy scripts* to *programs that do real work* — roughly a
solid first-year programming course.

---

# Volume III — The Living World

**Prerequisite:** Volume II. **Deliverable:** *Treasure Quest v3* — a **published** game with a shareable URL.
**Rung** 🏗️: *artifacts* — a README strangers can use; a demo you present with confidence. **Circle:** for my community.

**What your child learns (the skill arc):**

| Skill area | The tool the story needs |
|---|---|
| Object-oriented thinking | **classes & objects** — Player, Monster, Item become *things* with their own powers |
| Reuse | **inheritance & polymorphism** — a whole family of monsters from one blueprint |
| A real screen | **GUI / web, event-driven programming** — clicks and input, the first true window |
| Graphics & assets | **images, sprites, sound, animation** — a visual, noisy, moving world |
| Clean state | **state machines** — menu → play → win/lose, managed cleanly |
| Shipping | **packaging, dependencies, deployment** — the game leaves home and gets a **URL** |
| **Cloud persistence (D-40)** | **a real database, tasted** — a **multiplayer high-score table** / cloud save |

**The game grows:** a real UI, animation, sound, images — and a **URL** the child can send to a
friend. *"People I don't know can play my game."*

**The database moment (D-40):** the natural upgrade from Vol II's local save-file to *shared* cloud
data — *"save your high score to the cloud so your friend can see it."* Taught **concept-first**:
the durable lesson is *shared, persistent data lives in a database, not a file*, using a simple
modern hosted database (e.g. **Supabase** — a few lines, no SQL or servers required) as the
example. Needs an account (parent-aware), like the Vol IV AI service. It's also a prime
**🛡️ Builder's Shield** beat: *data minimization* — store only a name and a score, **never more than
you need.**

**What your child can now build:** real applications with a graphical interface, published to a URL
that anyone can visit, backed by a real cloud database. This is where *hobbyist* becomes *capable of
real projects* — past most bootcamp fundamentals.

---

# Volume IV — The Infinite Guild

**Prerequisite:** Volume III. **Deliverable:** *Treasure Quest AI* — **plus the confidence to build original things.**
**Rung** 🏗️: *the room* — propose solutions, collaborate, belong among real Builders. **Circle:** for the world.

**What your child learns (the skill arc):**

| Skill area | The tool the story needs |
|---|---|
| Building *with* AI | **AI APIs** — an NPC that truly talks; AI-generated quests and dialogue |
| Talking to AI well | **prompt engineering** — clear instructions, structured requests |
| Automation | **agents & scripts** — the game does things on its own |
| Collaboration | **Git & GitHub** — versioning, working with others, contributing |
| Shipping for real | **deployment, keys, accounts** — a real service in the real world |
| Guarding secrets | **🛡️ the Shield matures** — *guard your API keys like house keys; never paste secrets into a prompt* |
| Ethics & responsibility | the **AI Friendship Rules** & the Human & AI Manifesto |

**The game grows:** AI NPCs, AI-generated quests and dialogue, an AI companion.

**The AI thread is a *values* thread, not just a skills thread.** Volume IV teaches working *with*
AI through five kid-facing **AI Friendship Rules** — think first / ask AI second; ask AI to help
*find* the bug, not hand you the answer; never copy what you can't explain; AI is a teammate, not a
servant. It's also where the child becomes the one proposing the solutions. The realization we're
building toward: *"I can build things **with** AI — not just use it."*

**What your child can now build:** real, **AI-powered applications** — a chatbot, an AI-assisted
tool, an app that calls an LLM to do something genuinely useful — deployed for real, versioned on
GitHub, built with the judgment to guard secrets and respect the people who use it. This is *current
2026 developer workflow* — the same skills working developers are learning right now.

---

# What this series does — and doesn't — make your child *(for parents & educators)*

Honesty is a feature. Here is the truthful ceiling, so you can trust the floor.

**By the end of Volume IV, your child can — fluently:**
build and ship real applications (CLI tools, small web/GUI apps, automation scripts), publish them
to a URL backed by a cloud database, and build **AI-powered apps** with modern tools — with the
confidence, the debugging instinct, and the Builder's mindset to *learn anything next.*

**What this series deliberately does *not* do (and where those roads begin):**

- **It does not make a Machine Learning engineer.** Vol IV teaches building *with* AI (calling it,
  prompting it, coworking with it) — the modern, valuable skill — not building AI *itself* (no
  model training, no neural-net math, no numpy/pandas/PyTorch depth). *That road is recommended
  from high-school level and up.*
- **It does not drill Data Structures & Algorithms** the way a coding interview demands (sorting,
  recursion, trees, graphs, design patterns, system design). Lady-O-Query *seeds curiosity* about
  this world — she gestures at it, sometimes gently mocks it, to inspire — but the book doesn't
  teach it. *That road — plus advanced Python, full-stack frameworks (Django, FastAPI), and libraries
  like PyTorch — is where a Builder heads to earn real money; it challenges adults, and it's worth
  digging into deeply when the time comes.*
- **It does not cover** deep testing theory, raw SQL/database administration, concurrency, or type
  systems. (Debugging — practised *constantly* throughout — is the honest foundation testing grows
  from.)

The graduate this series makes, on purpose: **a confident, kind generalist Builder** who has *built
real things they love* and knows how to keep learning — not a specialist in any one field yet, but
ready to become one. In 2026, that may be the more valuable outcome.

---

# 🧭 Where to go from here — a Builder's next horizons *(the goodbye, after Volume IV)*

To every Builder who reaches the end: you didn't just learn Python. You became someone who can
*build.* Here is the sea beyond the map — go when you're ready, at your own pace.

1. **Machine Learning** — how AI actually *learns.* A deep, beautiful field (numpy, pandas,
   PyTorch, the math underneath). *Recommended from high-school level and up.* You've already built
   *with* AI; this is learning to build *the AI itself.*
2. **Data Structures, Algorithms & the road to a real job** — sorting, recursion, trees, graphs,
   design patterns, system design; advanced Python; full-stack frameworks (Django, FastAPI). This is
   the road to employment and real money. It's *hard* — it challenges adults — but you have the one
   thing that matters most: you're not afraid of hard, and you know how to debug your way through.
3. **Deeper databases & the back-end** — you tasted the cloud (high scores in Vol III). Real
   databases (PostgreSQL, Supabase and beyond), SQL, and back-end engineering are how big
   applications remember millions of people. A natural next step from what you've already touched.

And whatever you build next — remember the Shield 🛡️: *make it work, and think about who it
protects.* Fair winds, Builder. The Guild is proud of you. 🏴‍☠️🐉🍩

---

## For authors (the build-side notes)

- **Skill-gating is real:** a chapter (and its Typing Dojo mission) uses only skills the child
  already has by that point. The detailed mission backlog lives in `typing_dojo/MISSIONS_PLAN.md`;
  the chapter map lives in `SERIES_OUTLINE.md`. This file is the *why*; those are the *what/where*.
- **The map follows the territory.** Volume I above reflects the **shipped** chapter order. Where
  the original sketch differed (an early "gold exchange / ATM / superhero roster" ladder), the
  shipped stories replaced it — every skill still lands only where a story needs it.
- **Volumes II–IV are direction, not contract** — they firm up as each prior game state ships.

---

🎓 *We don't teach children computer science. We let them behave like computer scientists — and
one day they notice they've become one.*

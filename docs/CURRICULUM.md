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

## Two threads that run through every volume (the Builder, not just the Python)

The Python is the vehicle. Two things ride alongside it, volume to volume:

- 🌱 **Builder's Heart** — emotional resilience: frustration, the stuck bug, the Debug Break,
  *"real developers have broken keyboards too."* Named and normalized, never shamed. The #1 reason
  a young learner quits isn't difficulty — it's discouragement, so we teach the heart to persevere.
- 🦸 **The Inverting Mentor** — across the four volumes the child shifts from *asking* to
  *answering*. By the final volume, the mentor asks *them* the questions. The curriculum isn't
  "more Python each year" — it's a child *becoming* a Builder.

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

**Python focus:** dictionaries/tuples/sets in depth, **files** (save/load), **modules**, stronger
functions, **error handling** (`try`/`except`), richer randomness.

**The game grows:** inventory, NPCs, shops, save/load, multiple rooms, better dialogue. **This is
where the menu of adventures becomes one woven journey** — with state and memory, the number you
crack from the chest can become the key you carry to the gate. The child's own v1 ending planted
this itch; Volume II is the answer.

---

# Volume III — The Living World

**Prerequisite:** Volume II. **Deliverable:** *Treasure Quest v3* — a **published** game (web-first).

**Python focus:** **OOP** (classes), game architecture, event-driven design, assets, packaging,
publishing. **The game grows:** a real UI, animation, sound, images — and a **URL** the child can
send to a friend. *"People I don't know can play my game."*

---

# Volume IV — The Infinite Guild

**Prerequisite:** Volume III. **Deliverable:** *Treasure Quest AI* + the confidence to build
original things.

**Python focus:** AI APIs, prompt engineering, agents, automation, deployment, GitHub
collaboration, and ethics. **The game grows:** AI NPCs, AI-generated quests and dialogue, an AI
companion.

**The AI thread is a *values* thread, not just a skills thread.** Volume IV teaches working *with*
AI through five kid-facing **AI Friendship Rules** — think first / ask AI second; ask AI to help
*find* the bug, not hand you the answer; never copy what you can't explain; AI is a teammate, not
a servant. It's also where the child becomes the one proposing the solutions. The realization we're
building toward: *"I can build things **with** AI — not just use it."*

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

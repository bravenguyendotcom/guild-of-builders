# 🎓 CURRICULUM.md

### The Python learning path, mapped to the story

> **Status:** Volume I is **in production** (chapters 0–7 shipped). Volumes II–IV are **DRAFT outlines**.
> **Principle:** No skill appears because "it's next in the textbook." Every skill appears
> because a mission in *Captain Byte's Treasure Quest* needs it.

---

## The shape of the whole journey

| Volume | Python focus | The game becomes... |
|--------|--------------|---------------------|
| **I — The First Voyage** | Basics | a playable CLI adventure |
| **II — Growing the Adventure** | Data structures, files, modules | a bigger game with inventory, save/load, NPCs |
| **III — The Living World** | OOP, GUI/web, architecture | a real published game (desktop or web) |
| **IV — The Infinite Guild** | AI APIs, agents, deployment | an AI-powered game + real-world apps |

---

## Two threads that run through *every* volume (not Python skills — the Builder)

The Python skills below are the *vehicle*. Two things ride quietly alongside them, from
Volume I to IV, and every author should keep them in view:

- 🌱 **Builder's Heart** (`DECISIONS.md` D-32) — the emotional-resilience thread: frustration,
  the stuck bug, comparing yourself, the Debug Break. Named and normalized as the volumes go,
  never shamed. The skills are how a Builder *acts*; Builder's Heart is how a Builder *keeps going*.
- 🦸 **The Inverting Mentor** (`DECISIONS.md` D-31) — across the four volumes, TommyBot shifts
  from *asking* to *answering*, until by Volume IV Dragon Debug is the one asking questions.
  The curriculum isn't just "more Python each volume" — it's a child *becoming* a Builder.

These aren't lessons with their own chapters; they're the growth the Python skills serve.

---

# Volume I — The First Voyage (Python Basics)

**Prerequisite:** none.
**Deliverable:** `Captain Byte's Treasure Quest v1` (CLI, playable, shareable).

### Skills covered (in story order)

*(This list reflects the **shipped** chapter order 0–7, then the planned remainder. The
mission ladder below is the skill source of truth; this is the running order.)*

**Shipped so far (Ch 1–7):**
- variables, `input` / `print` (Ch 1–2)
- text vs. numbers: `int()`, and the *"input is always text"* bug `"3" * 2 == "33"` (Ch 2)
- `if` / `elif` / `else`, comparisons `>= <= == > <` (Ch 3)
- `float`, operators `*` `/`, bracket precedence, `round()`, the `ValueError` on `int("1.5")` (Ch 4)
- `import`, `random.choice()`, `=` vs `==`, the word `and` (Ch 5)
- `while` loops, `!=`, `random.randint()`, the infinite loop (rite of passage), the counter pattern (Ch 6)
- booleans (`True`/`False`), `len()`, the flag-words `and` / `or` / `not`, precise `if`/`elif` validation (Ch 7)

**Still ahead (planned):**
- `for` loops, `range`, `break` / `continue`
- integer division `//` & modulo `%`  *(not yet introduced — planned around the gold/ATM missions)*
- strings in depth: reversing, palindromes, character math / a simple cipher
- lists, tuples, dictionaries (introductory)
- menu loops & list/dict state (mini-programs)
- basic functions
- reading error messages & Rubber Duck debugging (deepened)
- computational thinking throughout: decomposition, pattern recognition, abstraction, dry-running, edge cases

> **Note:** the shipped chapters reordered the original sketch — conditionals and `float`
> arrived before `//`/`%`, and booleans/logical operators landed at **Ch 7** (Sir Boolean's
> debut), not early. That's fine: every skill still appears only when a chapter's story needs
> it (the Principle above). The map follows the territory.

### Ladder ↔ shipped chapters (reconciliation)

The numbered **mission ladder** below is the *skill* source of truth. The **shipped chapter
order** expanded and resequenced it. Quick map of what's real so far:

| Mission (ladder) | Shipped as | Skill actually taught |
|---|---|---|
| 1 Hungry Pizza Robot | Ch 2 | `input`, `int`, the `"3"*2` bug |
| 2 Age Machine | Ch 3 | `if`/`elif`/`else` |
| 3 Ninja Health Check | Ch 4 | `float`, `*` `/`, `round()` |
| 4 Pirate Gold Exchange | *(not yet — `//`/`%` still ahead)* | integer division & modulo |
| 5 Rock, Paper, Scissors | Ch 5 | `import`, `random.choice`, `and` |
| 6 The Secret Treasure | Ch 6 | `while`, `!=`, `random.randint`, counter |
| 7 Safe Password Checker | Ch 7 | booleans, `len()`, `and`/`or`/`not` |

*(Ch 0 Welcome and Ch 1 Sets Sail precede the ladder: mindset, then variables + `NameError`.
Mission 4's modulo hasn't shipped yet — it's planned, not skipped.)*

### The mission ladder (foundation exercises → the game)

These story-driven missions build the *skills*; the volume's capstone assembles them into
the game. (Titles are the working canon from the founding sessions.)

**Level 1 — Warm-up (mechanics of input/output & variables)**
1. Hungry Pizza Robot 🍕 — variables, string formatting, input
2. The Age Machine ⏳ — if/elif/else ("...old enough to learn driving!")
3. Ninja Health Check 🥷 — arithmetic, BMI, conditionals
4. Pirate Gold Exchange 🪙 — integer division & modulo
5. Rock, Paper, Scissors ✊ — `random`, comparison

**Level 2 — Computational thinking (conditions, loops, strings)**
6. The Secret Treasure (guess 1–100) — loops, comparison, counting attempts
7. Safe Password Checker 🔐 — multiple conditions, precise error messages
8. Recycling Robot ♻️ — counting a list *without* `.count()`
9. The Palindrome Mirror 🪞 — strings *without* `reverse()`
10. Caesar Messenger 🗝️ — character math, simple cipher

**Level 3 — Algorithms & data (think before you code)**
11. The ATM 🏧 — validation (enough funds? divisible by 50,000?)
12. Superhero Roster 🦸 — menu-driven list CRUD
13. Exam Scores 📊 — max/min/average *without* `max()`, `min()`, `sum()`
14. Monster Classifier 👾 — dictionaries + thresholds
15. Treasure Code Decoder 🧩 — parsing `A1B3C2` → sums

**Level 4 — Mini programs (writing *software*, not just answers)**
16. To-Do List CLI ✅ — menu loop, list state
17. Contact Book 📇 — dictionaries, add/edit/find/delete
18. LEGO Store 🧱 — inventory that changes on each purchase

**Level 5 — The Capstone**
19. Escape Room 🚪 — combine guessing, palindrome, password, math into one gated puzzle
20. **Captain Byte's Treasure Quest v1** 🏴‍☠️ — the full CLI adventure: story, choices,
    treasure, random events, win/lose, achievements, replay. Split into functions,
    organized cleanly. *This is the volume's real deliverable.*

> Missions 1–19 are the *training*. Mission 20 is the *ship*. The child ends Volume I
> saying **"I built my first game"** — something to show Dad, Mum, teachers, and friends.

---

# Volume II — Growing the Adventure (DRAFT outline)

**Prerequisite:** Volume I.
**Deliverable:** `Treasure Quest v2` — the *same* game, evolved.

Python focus: dictionaries/tuples/sets in depth, files (save/load), modules, better
functions, error handling (`try`/`except`), richer randomness.

Game gains: inventory, NPCs, shops, save/load, multiple maps, better monsters & dialogue.

---

# Volume III — The Living World (DRAFT outline)

**Prerequisite:** Volume II.
**Deliverable:** `Treasure Quest v3` — a *published* game (web-first, ideally).

Python focus: OOP (classes), game architecture, event-driven programming, assets,
packaging, publishing.

Game gains: real UI, animations, sound, images. The child can send a friend a **URL**.

---

# Volume IV — The Infinite Guild (DRAFT outline)

**Prerequisite:** Volume III.
**Deliverable:** `Treasure Quest AI` + the confidence to build original things.

Python focus: AI APIs, prompt engineering, agents, automation, deployment, GitHub,
collaboration, ethics.

Game gains: AI NPCs, AI-generated quests/maps/dialogue, AI hints, an AI companion.

Beyond the game, the Builder can now: make useful AI apps, contribute tools to their class
or school, or even try real freelance/collaborative work. **They build *with* AI, not merely consume it.**

> **The AI thread is a *values* thread, not just a skills thread.** Volume IV teaches working
> *with* AI through the **AI Friendship Rules** (`DECISIONS.md` D-33) — think first / ask AI
> second, ask AI to help *find* the bug (not hand the answer), never copy what you can't
> explain, AI is a teammate not a servant — the concrete, kid-facing companion to
> `HUMAN_AI_MANIFESTO.md`. This is also where the Inverting Mentor (D-31) pays off: the Builder
> is now the one proposing solutions.

---

## Mapping rule (for authors)

When adding any exercise, fill this in:

```
Mission #:
Story hook:
Skill(s) taught:
Computational-thinking skill:
Feeds which part of the game?:
Difficulty (⭐–⭐⭐⭐⭐⭐):
```

If "feeds which part of the game?" is blank — reconsider. Everything should serve the Quest.

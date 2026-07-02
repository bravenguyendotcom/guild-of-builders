# 🎓 CURRICULUM.md

### The Python learning path, mapped to the story

> **Status:** Volume I is **DRAFT-ready to build**. Volumes II–IV are **DRAFT outlines**.
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

# Volume I — The First Voyage (Python Basics)

**Prerequisite:** none.
**Deliverable:** `Captain Byte's Treasure Quest v1` (CLI, playable, shareable).

### Skills covered (in story order)
- variables, `input` / `print`
- strings & string formatting
- numbers, operators, integer division & modulo
- booleans, comparison, logical operators
- `if` / `elif` / `else`
- `while` and `for` loops, `range`, `break` / `continue`
- `random`
- lists, tuples, dictionaries (introductory)
- basic functions
- reading error messages & basic debugging (Rubber Duck method)
- computational thinking: decomposition, pattern recognition, abstraction, dry-running, edge cases

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

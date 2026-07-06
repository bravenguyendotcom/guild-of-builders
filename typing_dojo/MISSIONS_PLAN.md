# 🥋 typing_dojo/MISSIONS_PLAN.md

### The living mission backlog — one place, so no chapter is left without its Dojo beat

> **Status:** LIVING backlog (a plan, not the code). The built missions live in
> `coding_gold_mine/` (engines) + `missions/` (skins); this file tracks **what's planned, where
> it lands, and what's done.**
> **Why this exists:** the ~50-mission / ~1-per-chapter plan (D-30) had no single home, so the
> 🥋 tags in `SERIES_OUTLINE.md` were incomplete (only Ch 6/9/10). This backlog is the source of
> truth the outline's 🥋 tags point at.
> **The rule (D-29):** from **Chapter 6 onward, every chapter ends with an optional 🥋 Dojo
> block** (Tiers I–II). This backlog assigns each chapter a mission — **new** when the chapter
> introduces a fresh idea, or an **Echo** (a familiar engine in a new skin, D-23) when it doesn't.
> Repetition is the point: *"until your fingers know it before your brain does."*

---

## How to read this

- **New** = a fresh canonical engine (goes in `coding_gold_mine/`).
- **Echo** 🔁 = reuses an existing engine under a new skin (D-23) — no chapter after Ch 6 is ever
  "empty"; if it has no new algorithm, it echoes a beautiful old one.
- **Tiers** = which tiers this mission ships with (a topic earns only the tiers it deserves, D-28).
  In-book blocks are **Tier I–II**; harder tiers live outside the book (D-29).
- **Status:** ✅ built · 🔨 next · 📋 planned.
- **Skill gate:** a mission only uses skills the child *already has* by that chapter.

---

## Volume I — the in-book backlog (Ch 6 onward)

| Ch | Chapter | Mission | New/Echo | Engine | Tiers | Status |
|----|---------|---------|----------|--------|-------|--------|
| 6 | The Secret Treasure | **001 Guess the Number** | New | `001_guess_the_number.py` | I–II | ✅ built |
| 7 | Safe Password Checker | **002 The Bouncer** (a rules-checker: length + forbidden word) | New | `002_bouncer.py` | I–II | 🔨 next |
| 8 | The Recycling Robot | **003 Tally Machine** (count items in a list, no `.count()`) | New | `003_tally.py` | I–II | 📋 |
| 9 | The Palindrome Mirror | **004 Mirror, Mirror** (reverse & compare a string) | New | `004_palindrome.py` | I–II | 📋 |
| 10 | The Caesar Messenger | **005 Secret Cipher** (shift letters — Caesar) | New | `005_caesar.py` | I–II | 📋 |
| 11 | The Riddle Theatre | **006 The Guessing Cave** 🔁 | Echo of 001 | `001` (new skin) | I–II | 📋 |
| 12 | Menus & Mini-Programs | **007 The Quest Log** (menu loop over a list) | New | `007_menu.py` | I–II | 📋 |
| 13 | The Painter's Deck | **008 The Sign Painter** (build ASCII art with loops) | New | `008_ascii_sign.py` | I–II | 📋 |
| 14 | The Escape Room | **009 The Vault** 🔁 (combine guess + check — echoes 001/002) | Echo | `001`+`002` skin | I–II | 📋 |
| 15 | Treasure Quest v1 (capstone) | **010 The Ship's Console** 🔁 (a tiny menu tying it together) | Echo of 007 | `007` (new skin) | I–II | 📋 |

*Volume I total: 10 missions (5 new engines + echoes) — the "Batch 01" scope, now chapter-mapped.*

---

## Volume II — planned backlog (data structures, files, modules)

*Skills unlock: dicts/tuples/sets in depth, files (save/load), `try`/`except`, functions.*

| Ch | Chapter | Mission idea | New/Echo | Tiers | Status |
|----|---------|--------------|----------|-------|--------|
| 1 | The Map Grows | **011 The Blueprint** (read a tiny spec → checklist) | New | I–II | 📋 |
| 2 | The Knapsack | **012 The Inventory** (add/remove from a list) | New | I–II | 📋 |
| 3 | The Merchant's Wharf | **013 The Haggler** (functions that return a price) | New | I–II | 📋 |
| 4 | When Things Go Wrong | **014 The Safety Net** (`try`/`except` a bad input) | New | I–II | 📋 |
| 5 | The Memory Stone | **015 The Save Stone** (write/read a file) | New | I–II | 📋 |
| 6 | The Cartographer | **016 The Room Map** (dict of rooms) | New | I–III | 📋 |
| 7 | The Toolmakers' Guild | **017 The Toolbox** 🔁 (split a program into functions) | Echo | I–II | 📋 |
| 8 | The Bestiary | **018 The Monster Roll** (weighted random) | New | I–II | 📋 |
| 9 | The Riddle Theatre Returns | **019 The Riddle Bank** 🔁 (dict of Q&A — echoes 016) | Echo | I–II | 📋 |
| 10 | The Standup | **020 The Backlog** 🔁 (menu over a list — echoes 007/012) | Echo | I–II | 📋 |
| 11 | Pycasso's Palette | **021 The Colour Box** (formatted/coloured output) | New | I–II | 📋 |
| 12 | Treasure Quest v2 (capstone) | **022 The Grown Game** 🔁 (integration echo) | Echo | I–II | 📋 |

---

## Volume III — planned backlog (OOP, architecture)

*Skills unlock: classes/objects, inheritance, state, packaging. Tier III (Den) becomes common.*

| Ch | Chapter | Mission idea | Tiers | Status |
|----|---------|--------------|-------|--------|
| 1–2 | Blueprint / Meet the Class | **023 The Class Factory** (a simple class) | I–III | 📋 |
| 3 | Inheritance Island | **024 The Family Tree** (inheritance) | I–III | 📋 |
| 4 | The Stage Appears | **025 The Event Loop** 🔁 | I–III | 📋 |
| 5 | Pycasso's Canvas | **026 The Sprite Board** (2D grid) | II–III | 📋 |
| 6 | The Sound of Adventure | **027 The Frame Beat** 🔁 (loop timing echo) | II–III | 📋 |
| 7 | The State Machine | **028 The Mode Switch** (state machine) | I–III | 📋 |
| 8–10 | Packing / Lighthouse / README | **029 The Packager** 🔁 | I–II | 📋 |
| 11 | Demo Night | **030 The Showcase** 🔁 (integration echo) | I–II | 📋 |

---

## Volume IV — planned backlog (AI, agents, collaboration)

*Skills unlock: APIs, prompts, Git, agents. Tier III–IV and the outside-the-book URL missions.*

| Ch | Chapter | Mission idea | Tiers | Status |
|----|---------|--------------|-------|--------|
| 1–2 | New Crew / Talking Parrot | **031 The First API Call** | I–II | 📋 |
| 3 | The Art of Asking | **032 The Prompt Lab** | I–II | 📋 |
| 4 | The AI Quartermaster | **033 The Content Injector** 🔁 | I–III | 📋 |
| 5 | The Honest Duck | **034 The Fact-Checker** (verify AI output) | I–III | 📋 |
| 6–7 | Companion / Agents | **035 The Helper Chain** | II–IV | 📋 |
| 8 | The Guild Repository | **036 The Merge** 🔁 (Git-flavoured logic puzzle) | I–III | 📋 |
| 9–10 | Working With Others / Ethics | **037 The Reviewer** 🔁 | II–III | 📋 |
| 11 | The Real Problem | **038 The Solver** 🔁 (Tier IV seed — systems) | III–IV | 📋 |

---

## Distribution principles (so this stays honest)

- **No chapter Ch 6+ is ever empty.** New idea → new mission; no new idea → an **Echo** (D-23).
- **Skill-gated.** A mission uses only what the child has learned by that chapter (D-20).
- **Tiers earned, not forced.** Most in-book missions are Tier I–II; Tier III appears only when
  the skills support it (Vol II+), and only at gentle difficulty in-book (D-29).
- **The mountain grows outside.** This backlog is the *in-book* ~1-per-chapter set (~38 here +
  echoes). The wider library (harder tiers, more skins) grows in the open-source gallery (D-30).
- **`SERIES_OUTLINE.md`'s 🥋 tags point here.** When a mission's chapter/target changes, update
  this backlog first, then the outline's one-line 🥋 tag.

---

## Build order (next up)

1. ✅ **001 Guess the Number** — built (the template).
2. 🔨 **002 The Bouncer** (Ch 7) — the next engine to author.
3. 📋 Then 003–005 (the new Vol I engines), then the echoes.

> Build the format, not the mountain. Ship missions as chapters need them — never all at once.
> *v1 > perfection.*

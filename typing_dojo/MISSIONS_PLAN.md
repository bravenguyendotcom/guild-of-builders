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
| 7 | Safe Password Checker | **002 The Bouncer** (a rules-checker: length + forbidden word) | New | `002_bouncer.py` | I–II | ✅ built |
| 8 | The Recycling Robot | **003 Tally Machine** (count items in a list, no `.count()`) | New | `003_tally.py` | I–II | ✅ built |
| 9 | The Palindrome Mirror | **004 Mirror, Mirror** (reverse & compare a string) | New | `004_palindrome.py` | I–II | ✅ built |
| 10 | The Caesar Messenger | **005 Secret Cipher** (shift letters — Caesar) | New | `005_caesar.py` | I–II | ✅ built |
| 11 | The Riddle Theatre | **006 The Guessing Cave** 🔁 | Echo of 001 | `001` (new skin) | I–II | ✅ built |
| 12 | Menus & Mini-Programs | **007 The Quest Log** (menu loop over a list) | New | `007_menu.py` | I–II | ✅ built |
| 13 | The Painter's Deck | **008 The Sign Painter** (build ASCII art with loops) | New | `008_ascii_sign.py` | I–II | ✅ built |
| 14 | The Escape Room | **009 The Vault** 🔁 (combine guess + check — echoes 001/002) | Echo | `001`+`002` skin | I–II | ✅ built |
| 15 | Treasure Quest v1 (capstone) | **010 The Ship's Console** 🔁 (a tiny menu tying it together) | Echo of 007 | `007` (new skin) | I–II | ✅ built |

*Volume I total: 10 missions (5 new engines + echoes) — the "Batch 01" scope, now chapter-mapped.*

---

## Volume II — planned backlog (data structures, files, modules)

*Skills unlock: dicts/tuples/sets in depth, files (save/load), `try`/`except`, functions.*

| Ch | Chapter | Mission idea | New/Echo | Tiers | Status |
|----|---------|--------------|----------|-------|--------|
| 1 | The Map Grows | **011 The Blueprint** (read a tiny spec → checklist) | New | I–II | ✅ built |
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

## 🎲 Tier II typo rotation — keep the *shape* fresh, not just the categories

> **The audit that produced this (Missions 004–011).** The Typo Palette (D-28) fixed *which
> categories* the typos come from — and the predictability quietly moved up a level:
> - **The shape alternated** — three-throwers, two-and-a-ghost, three-throwers, two-and-a-ghost —
>   for seven missions straight.
> - **Every silent typo was a consistent variable rename** — five for five. A Builder learns by
>   mission three that *"the sneaky one is always a misspelled variable"* and stops reading the code.
> - **The README telegraphed the shape** in the same words each time (*"two will stop the program
>   cold; the third won't"*) — the mission handed over the answer's shape for free.
>
> The palette cured stale *categories*; this cures stale *shapes*. Same disease, one level up.

### The three shapes (how loud the three typos are)

- **Shape A — the cascade:** all three throw. Fix one, the next traceback appears. Pure ladder.
- **Shape B — two and a ghost:** two throw; one is **silent** (the program runs, the output is wrong).
- **Shape C — the quiet room:** one throws; **two are silent**. The traceback is the easy part;
  the real hunt is reading output against expectation.

### The three silent devices (how a typo hides)

- **S1 — consistent variable rename.** Declared and used the same wrong way everywhere: runs clean,
  nothing to see, only a careful read finds it. *(The classic — now rationed.)*
- **S2 — silent over-indent.** A line nudged one level in: legal Python, different meaning
  (runs inside the loop instead of after it). Output is subtly wrong.
- **S3 — string-literal slip.** A typo inside a quoted string: the program runs *perfectly* and
  prints something misspelled. Caught **only** by reading your own output against the
  README's **Expected output** — the Donut Law in miniature.
  > ⚠️ **Guard:** never use a string-literal slip where the misspelled text is *itself* the lesson
  > (a prompt the Builder types back, a password, a cipher input). That turns a ghost into a
  > logic bug and breaks the Tier II contract.

### The two rules (non-negotiable, from here on)

1. **No shape three times running.** A · A · B is fine; A · A · A is not.
2. **Never the same silent device twice running.** If the last ghost was S1, the next is S2 or S3.

### The one habit (kill the leak at its source)

**Stop telegraphing the shape in the README.** Never write *"two will stop the program; the third
won't."* Say what Conan would say — *"Three slips are in here. Do you have any clue?"* — and let
the Builder discover the shape by hunting. The mission must never hand over the answer's outline.

### Volume II typo schedule (planned — adjust as chapters ship)

| Mission | Shape | Silent device | Note |
|---|---|---|---|
| **012** The Inventory | B | **S2** (over-indent) | breaks the five-in-a-row variable-rename tell |
| **013** The Haggler | A | — | pure cascade; no ghost at all |
| **014** The Safety Net | C | **S1** + **S2** | the quiet room; `try`/`except` is a natural fit |
| **015** The Save Stone | B | **S3** (string literal) | *(if S3 is in play — else S2)* |
| **016** The Room Map | A | — | |
| **017** The Toolbox 🔁 | B | **S1** | S1 has rested three missions; it's fresh again |
| **018** The Monster Roll | C | **S2** + **S3** | |
| **019** The Riddle Bank 🔁 | A | — | |
| **020** The Backlog 🔁 | B | **S1** | |
| **021** The Colour Box | C | **S3** + **S2** | S3's best home: colour output *is* the read-it-yourself lesson |
| **022** The Grown Game 🔁 | B | **S2** | capstone echo |

> Shapes and devices are **scheduled in advance on purpose** — a rotation you can *see* is a
> rotation you can *keep*. Improvising per mission is exactly how the last pattern went stale.

---

## Build order (next up)

1. ✅ **Volume I complete** — Missions 001–010 all built and bash-verified (engines in
   `coding_gold_mine/`, skins in `missions/`). The full Vol I Dojo ladder is shipped.
2. ✅ **011 The Blueprint** — built & bash-verified (Vol II Ch 1's ritual mission: scoping a
   wishlist into v1/later, zero new syntax on purpose — see D-28a).
3. 🔨 **012 The Inventory** (Ch 2) — the next engine to author. First mission under the new typo
   rotation: **Shape B · silent device S2** (over-indent) — it breaks the five-in-a-row
   variable-rename tell. Build to the chapter's skills; don't run ahead of the manuscript.

> Build the format, not the mountain. Ship missions as chapters need them — never all at once.
> *v1 > perfection.*

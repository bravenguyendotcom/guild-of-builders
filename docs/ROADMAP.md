# 🗺️ ROADMAP.md

### Where we are, and where we're sailing

> **Status:** LIVING. Update this at the end of every work session.
> This is the one file that answers *"What do I do next?"*

---

## Current position

**Phase 0 — Foundation.** ✅ *In progress → nearly complete.*

We have laid the constitutional skeleton of the project:
`MASTER_BOOT`, `PROJECT_BIBLE`, `CHARACTERS`, `STYLE_GUIDE`, `CURRICULUM`, `GAME_DESIGN`,
`DECISIONS`, `CONTRIBUTING`, plus the repository structure and license.

We deliberately **stopped before writing Volume II of anything** — because the founding
lesson of this project is: *don't build the house before the foundation is poured.*

---

## The plan, in phases

### ✅ Phase 0 — Foundation (the governing documents)
Build every `docs/` file so the project can evolve under version control. **← we are here.**

### ▶️ Phase 1 — Volume I skeleton
- Draft `manuscript/volume_1/` chapter by chapter (story first).
- Draft `workbook/volume_1/` missions 1–5 (using the mission template).
- Keep each chapter a separate file. One artifact per session.

### Phase 2 — Volume I missions 6–20
- Missions 6–19 (training).
- **Mission 20:** build `source_code/volume_1/treasure_quest/` — the real playable game.

### Phase 3 — Volume I polish & first release
- Solutions + hints + teaching guide in `teacher/`.
- Certificates and badges in `assets/`.
- Generate PDF/DOCX/HTML from the markdown.
- Tag the repo **`v1.0`** on GitHub. First real release. 🎉

### Phase 4+ — Volumes II, III, IV
Repeat the pattern, one volume at a time, always evolving the same game.

---

## Working rhythm (so it never becomes overwhelming)

- **One session = one artifact = one commit = one donut.** 🍩
- Never try to write a whole volume in a single conversation.
- End every session by updating this file: what got done, what's next.

---

## Session log (append newest at the top)

| Date | Session goal | Donut delivered | Next |
|------|--------------|-----------------|------|
| _(session 15)_ | Phase 1: Volume I, Chapter 6 (The Secret Treasure) — while loops, !=, random.randint, infinite loops, counters | manuscript/volume_1/06_the_secret_treasure.md | Chapter 7 / The Safe Password Checker — asking many questions at once (fresh convo) |
| _(session 14)_ | Phase 1: Volume I, Chapter 5 (Rock, Paper, Scissors) — import, random.choice, == vs =, and | manuscript/volume_1/05_rock_paper_scissors.md | Chapter 6 / The Secret Treasure — the magic of loops (fresh convo) |
| _(session 13)_ | Phase 1: Volume I, Chapter 4 (The Ninja Health Check) — float, operators (`*` `/`), operator precedence, round() | manuscript/volume_1/04_ninja_health_check.md | Chapter 5 / Rock, Paper, Scissors — the magic of `random` (fresh convo) |
| _(session 12)_ | Make Claude Project hand off logging + Git fully to Codie; remind to re-sync repo into Project knowledge | docs/CLAUDE_PROJECT_CONFIG.md | Chapter 4 / The Ninja Health Check (fresh convo) |
| _(session 11)_ | Phase 1: Volume I, Chapter 3 (The Age Machine) — if / elif / else (control flow, comparisons) | manuscript/volume_1/03_the_age_machine.md | Chapter 4 / The Ninja Health Check (fresh convo) |
| _(session 10)_ | Phase 1: Volume I, Chapter 2 (The Hungry Pizza Robot) — input + int (text vs. numbers) | manuscript/volume_1/02_hungry_pizza_robot.md | Chapter 3 / The Age Machine (fresh convo) |
| _(session 9)_ | Phase 1: Volume I, Chapter 1 (Captain Byte Sets Sail) — our first Python: variables | manuscript/volume_1/01_captain_byte_sets_sail.md | Chapter 2 / Hungry Pizza Robot (fresh convo) |
| _(session 8)_ | Wire Codie to log + commit only; sort GitHub connector | .claude/commands/ship-chapter.md | Chapter 2 / Hungry Pizza Robot (fresh convo) |
| _(session 7)_ | Phase 1: Volume I, Chapter 0 (Welcome) | manuscript/volume_1/00_welcome.md | Chapter 1 (our first line of Python) |
| _(session 6)_ | Add Real World box | STYLE_GUIDE.md (style guide v1.1) | In the Real World box + professionalism ladder |
| _(session 5)_ | Add Sir Quizzalot to canon | CHARACTERS.md v1.2 (co-master of the Riddle Theatre) | Phase 1: Volume I chapters (in their own conversations) |
| _(session 4)_ | Add two new characters to canon | CHARACTERS.md v1.1 (Prof. Pycasso + Maestro Monty) | Phase 1: Volume I, Chapter 0 (Welcome) |
| _(session 3)_ | Configure the Claude Project itself | CLAUDE_PROJECT_CONFIG.md (custom instructions + knowledge list) | Add new characters to canon |
| _(session 2)_ | Build the instruction layer | AI Working Agreement, mission + chapter templates, Treasure Chest, Changelog | Configure the Claude Project |
| _(founding)_ | Restructure the ChatGPT conversation into a real repo | Foundation docs + repo scaffold | Build the instruction layer |

> When you finish a session with Claude, add a row here before you close the tab.

---

## The finish line (what "success" means)

Not the number of copies read.
The number of children who someday say:

> *"I have an idea."*
> *"...I think I know how to build it."*

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
| 2026-07-09 | Lock D-35 (Advanced Pycasso's Gallery: skill-gated 3D/motion showpieces, art-twin of the Dojo's advanced tiers, capstone Spinning Donut at Vol IV Ch 8) in DECISIONS.md; write the Guild Extras build kit (D-34 handoff: model choice, files to sync, rotation rules, quality bar, paste-ready prompt) so a dedicated writing session can compose Batch 1 from the SOURCE catalog | docs/DECISIONS.md, docs/GUILD_EXTRAS_BUILD_KIT.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-09 | Distill the 1,485-line Gemini brainstorm into one tight SOURCE catalog for the Guild Extras (D-34): 15 jokes, 26 riddles, 14 code-art pieces, one line each, plus a re-skinning key (foreign characters → ours) so a writer never re-reads the raw transcript | docs/GUILD_EXTRAS_SOURCE.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Create the living Dojo missions backlog: map all ~38 planned missions across 4 volumes to their chapters, mark new vs. Echo (D-23), track status, ensure no chapter 6+ empty and all skill-gated; Vol I: 10 in-book missions (5 new engines + 5 echoes); Vol II–IV planned with distribution principles (tiers earned not forced, mountain outside) | typing_dojo/MISSIONS_PLAN.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Create the Advanced Gallery (Pycasso's 3D/motion aspirational art tier): 6 skill-gated showpieces (Matrix Rain, Starfield, Rotating Sphere, Spinning Donut, Rocket Launch, Moon Landing) as a parallel to Dojo's higher tiers (D-28); wire into SERIES_OUTLINE.md as optional 🖼️ thread | docs/PYCASSO_GALLERY_ADVANCED.md, docs/SERIES_OUTLINE.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Lock D-34 (Guild Extras: rotating Art/Riddle/Joke beats, Ch 1+, re-skinned to our cast, separate from Dojo) in DECISIONS.md; clarify D-28/D-30 wording; log and commit | docs/DECISIONS.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Vol 1 Ch6 (The Secret Treasure) revision — added Dragon Debug's empathy response to TommyBot's frustration ("That hot flash of *why-is-it-doing-that*...It's a sign that you're *doing* this"), validating struggle; added TommyBot's initiative beat ("But TommyBot didn't wait to be told twice"); introduced the Typing Dojo (a practice space), its guardian The Tangle (Typo-Squid), and Dragon Debug's quiet double-act with Quackers; added the first 🥋 Typing Dojo block with Mission 001 (Guess the Number) canonical program, expected output, and 🕵️ Conan's Challenge (typo-finding) | manuscript/volume_1/06_the_secret_treasure.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Vol 1 Ch5 (Rock, Paper, Scissors) revision — expanded Dragon Debug's response to Captain Byte's frustrated "OH, COME ON!" with warmth ("That howl has come out of me too...More times than I'd like to count"), validating the impulse to shout and modeling universality of struggle; added TommyBot's initiative beat ("But you were already reaching for the keyboard"), continuing the pattern of learning by doing | manuscript/volume_1/05_rock_paper_scissors.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Vol 1 Ch4 (The Ninja Health Check) revision — deepened Dragon Debug's response to the `ValueError` with a moment of empathy ("That growl in your chest is allowed, Captain...Even dragons have wanted to throw a keyboard at the sea"), validating frustration and modeling that struggle is universal, softening the emotional tone around encountering the first real error message | manuscript/volume_1/04_ninja_health_check.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Vol 1 Ch3 (The Age Machine) revision — added TommyBot's initiative beat ("his hands were already on the keys...") showing he's learning by watching, and deepened Dragon Debug's response to "it's broken" with a moment of connection (admitting he too once felt the jolt, "more times than I've had cups of tea") to soften shame and model the Inverting Mentor arc (D-31) in miniature | manuscript/volume_1/03_the_age_machine.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Vol 1 Ch2 (The Hungry Pizza Robot) revision — deepened Dragon Debug's "Every Builder meets it" moment with a brief personal reflection (admitting he once thought the computer was broken, was just learning to listen), softening shame; added TommyBot's realization about type conversion ("So we have to *tell* it that the words are really a number") and Dragon Debug recognizing this as true learning ("You're building"), modeling the Inverting Mentor arc (D-31) in miniature | manuscript/volume_1/02_hungry_pizza_robot.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| 2026-07-06 | Vol 1 Ch1 (Captain Byte Sets Sail) revision — two small beats: TommyBot reaching for the keyboard (planting the "you're building" moment as something the reader does too), and a closing bonding scene where Captain Byte admits he thought he'd broken everything and Dragon Debug welcomes him (and the reader) into "the club" every programmer belongs to, reinforcing "errors are conversations" | manuscript/volume_1/01_captain_byte_sets_sail.md | Continue Vol 1 revision pass per MANUSCRIPT_AUDIT.md |
| _(session 36)_ | Guardrail exception (confirmed): built **Mission 001 (Guess the Number)** — the first canonical program in `coding_gold_mine/` (Engine 001: `while`, `!=`, `random.randint`, counter pattern, loop exit) plus its Layer-2 skin in `typing_dojo/missions/001_guess_the_number/` (Tier I clean copy, Tier II three-typo Conan's Challenge, README with story hook + expected output); both files bash-tested (canonical engine run via simulated input, challenge_2's typos confirmed to raise the documented `NameError` first). Also trimmed `DECISIONS.md` D-22 to a short MERGED pointer, closing V-1. Unblocks `MANUSCRIPT_AUDIT.md` R-1/R-5 | typing_dojo/coding_gold_mine/001_guess_the_number.py, typing_dojo/missions/001_guess_the_number/, docs/DECISIONS.md | Chapter 6 revision — add the Typing Dojo debut + first 🥋 block using Mission 001 (fresh convo) |
| _(session 35)_ | Guardrail exception (confirmed): re-audited `docs/MANUSCRIPT_AUDIT.md` to v2 against the canon shipped since v1 (D-26–D-33, STYLE_GUIDE §4a, the Voice museum) — verdict unchanged (prose is strong), findings reframed as new-canon gaps: Ch 6 needs the Typing Dojo debut + first 🥋 block (R-1, blocked on Mission 001 per R-5), the Inverting Mentor (R-3) and Builder's Heart (R-4) need only light seeding elsewhere, teaching-bugs need a re-run bash check (R-6); recommends the order Mission 001 → Ch 6 revision → light 0–5/7 passes → Ch 8 | docs/MANUSCRIPT_AUDIT.md | Mission 001 (Guess the Number) — the template mission (fresh convo), then the Chapter 6 revision (Typing Dojo debut) |
| _(session 34)_ | Guardrail exception (multi-file session, approved): added "The Voice — a museum of lines" to `PHILOSOPHY.md` — verbatim canon sentences to quote, not paraphrase — and wired it into the boot sequence (`AI_WORKING_AGREEMENT.md` step 6 + Rule 5, `STYLE_GUIDE.md` §1); fixed a stale D-22→D-28 citation in `STYLE_GUIDE.md` (closes V-2 from `INTEGRITY_CHECK.md` v3); locked three decisions — D-31 (The Inverting Mentor), D-32 (Builder's Heart resilience thread), D-33 (AI Friendship Rules for Volume IV) | docs/PHILOSOPHY.md, docs/AI_WORKING_AGREEMENT.md, docs/STYLE_GUIDE.md, docs/DECISIONS.md | Tidy remaining stale-vocabulary citations (V-1: D-20/D-21 still say "Challenge I/II"; V-3: README mission-format header wording), then the chapter-revision pass (fresh convo) |
| _(session 33)_ | Added a 🐛 Debug Log box to Chapter 1 (`01_captain_byte_sets_sail.md`) — a worked example of the chapter's `NameError` teaching-bug (`tresure_depth` vs. `treasure_depth`), showing the bug/cause/fix table so Builders see the box filled in once before using it themselves | manuscript/volume_1/01_captain_byte_sets_sail.md | Tidy V-1/V-2 stale-vocabulary citations, then the chapter-revision pass (fresh convo) |
| _(session 32)_ | Two donuts: (1) refreshed `docs/INTEGRITY_CHECK.md` to v3 — a pre-flight audit after the Dojo arc (D-26–D-30), confirming the Dojo model agrees with itself everywhere and flagging three cosmetic stale-vocabulary spots (D-20/D-21 still say "Challenge I/II," `STYLE_GUIDE.md` §4 cites superseded D-22) to tidy before the chapter-revision pass; (2) added new content to Chapter 0 (`00_welcome.md`) — Captain Byte introduces the "Fog of 'I Can't'" (the self-doubt every Builder feels before starting, beaten by writing one line) and a new 🏗️ In the Real World box on source code | docs/INTEGRITY_CHECK.md, manuscript/volume_1/00_welcome.md | Tidy V-1/V-2 stale-vocabulary citations, then the chapter-revision pass (fresh convo) |
| _(session 31)_ | Follow through on D-27–D-30 across the rest of canon (session 30 locked the decisions and `typing_dojo/README.md`): `CHARACTERS.md` now credits Dragon Debug as the Dojo's owner/host and expands The Tangle's entry with the owner/guardian double-act; `SIDE_QUESTS.md`'s Typing Dojo entry rewritten to the finalized four-tier ladder, the honor rule, and the in-book/outside gate; `STYLE_GUIDE.md` (v1.3) gains §4a, the optional 🥋 Typing Dojo block at chapter ends from Ch 6 on | docs/CHARACTERS.md, docs/SIDE_QUESTS.md, docs/STYLE_GUIDE.md | Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 30)_ | Lock four Typing Dojo decisions: D-27 (Dragon Debug owns the Dojo, The Tangle is its guardian — a warm double-act, not enemies), D-28 (finalizes the four tier names — Keyboard Ninja, Conan's Challenge, Dragon Debug's Den, The Lost Heaven — supersedes D-22), D-29 (the gate splits by tier: I/II openly offered in-book from Ch 6 on, III/IV self-select outside per D-24), D-30 (Dojo scope: ~50 in-book missions; the system is canon, a 300–500-program mountain is a parked dream, not a promise); brought `typing_dojo/README.md` (v1.1) into line with all four | docs/DECISIONS.md, typing_dojo/README.md | Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 29)_ | Follow through on D-26: rewrite `STYLE_GUIDE.md` §4 from the old 12-part workbook worksheet template to the embedded-in-chapter mission shape (Story → task → honest bug → Testing Table/Debug Log boxes → Achievement → Cliffhanger), and retire `workbook/README.md` as an active track — it's now a signpost pointing authors to `manuscript/` and flagging `_TEMPLATE_mission.md` as deprecated | docs/STYLE_GUIDE.md, workbook/README.md | Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 28)_ | Lock D-26: retire `workbook/` as a separate authored track — missions live inside the story chapters (as the shipped chapters 0–7 already do), keeping the Testing Table & Debug Log as in-chapter boxes instead of standalone worksheets; also closed two open Treasure Chest items (`PHILOSOPHY.md` marked done, `STYLE_GUIDE.md` §4 update queued) | docs/DECISIONS.md | Mission 001 (Guess the Number) — the template mission (fresh convo); then `STYLE_GUIDE.md` §4 update per D-26 |
| _(session 27)_ | Close M-2 from the manuscript audit: `CURRICULUM.md`'s story-order note was ahead of shipped reality (listed modulo before the shipped chapters use it) — rewrote it into a shipped-vs-planned skill list plus a ladder ↔ shipped-chapters reconciliation table; tightened `SERIES_OUTLINE.md`'s Volume I status line and legend to match (chapters 0–7 shipped, 8–15 planned) and added the two Fog Creature tags (Shortcut Serpent, Ego Gremlin) to their Volume II chapters | docs/CURRICULUM.md, docs/SERIES_OUTLINE.md | Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 26)_ | Close F-1 from the integrity check: add The Tangle, the Typing Dojo's Typo-Squid guardian, to `CHARACTERS.md` as a Side-Quest Guardian, kept distinct from Bug Monster and the Fog Creatures | docs/CHARACTERS.md | Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 25)_ | Whole-project cross-reference audit: verify decisions/citations/canon/index all resolve correctly; project is in strong structural health, one small canon gap found (The Tangle missing from CHARACTERS.md) | docs/INTEGRITY_CHECK.md | Add The Tangle to CHARACTERS.md (F-1); then Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 24)_ | Link `docs/PHILOSOPHY.md` into `PROJECT_BIBLE.md`'s core-lessons section and glossary, so the Constitution points to the soul beneath it | docs/PROJECT_BIBLE.md | Author Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 23)_ | Write the side-quest world index: how side-quests work (optional, reward not gate), the Typing Dojo featured entry (with its guardian The Tangle, the Typo-Squid), the parked Side-Quest Board, and the checklist for adding a new one | docs/SIDE_QUESTS.md | Author Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 22)_ | Wire `docs/PHILOSOPHY.md` and the side-quest world (`docs/SIDE_QUESTS.md`, `typing_dojo/`) into `MASTER_BOOT.md`'s file index and boot sequence, so nothing new gets missed | MASTER_BOOT.md | Author Mission 001 (Guess the Number) — the template mission (fresh convo); write `docs/SIDE_QUESTS.md` |
| _(session 21)_ | Write up "The Art of Teaching Without Any Teaching" — the project's deepest why (curiosity over education, invisible teaching, invitation not obligation, discovery must self-select, joyful repetition) as promised by D-25 | docs/PHILOSOPHY.md | Author Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 20)_ | Lock 6 decisions (D-20–D-25) for the Typing Dojo & side-quest world: the arcade-beside-the-spine policy, Engine + Skin architecture, the four-tier mastery ladder, strategic repetition, discovery-must-self-select, and "The Art of Teaching Without Any Teaching" | docs/DECISIONS.md | Author Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 19)_ | Freeze the Typing Dojo v1.0 system spec: an arcade of typing missions (Engine + Skin, four mastery tiers, Batch 01's first ten missions) that lives alongside the main story without ever teaching | typing_dojo/README.md | Author Mission 001 (Guess the Number) — the template mission (fresh convo) |
| _(session 18)_ | Phase 1: Volume I, Chapter 7 (The Safe Password Checker) — booleans, `len()`, `and` / `or` / `not`, Sir Boolean joins the crew | manuscript/volume_1/07_the_safe_password_checker.md | Chapter 8 / Recycling Robot — sorting and counting a pile (fresh convo) |
| _(session 17)_ | Canon expansion: Fog Creatures roster, the Widening Circle spine, whole-series outline, Builder's Logbook (ranks/pacing), Human & AI Manifesto draft, and MASTER_BOOT reorganized to index + boot-sequence it all | docs/CHARACTERS.md, docs/PROJECT_BIBLE.md, docs/SERIES_OUTLINE.md, docs/SETUP.md, docs/BUILDERS_LOGBOOK.md, docs/HUMAN_AI_MANIFESTO.md, MASTER_BOOT.md | Chapter 7 / The Safe Password Checker (fresh convo) |
| _(session 16)_ | Lock 7 parked decisions (D-13–D-19): semantic Markdown authoring + per-device responsive rendering, the professionalism ladder / "In the Real World" box, personal-mastery progress (no leaderboard), flexible age-informed pacing bands, Human & AI Manifesto as Vol IV canon, the Widening Circle theme, original-IP-only policy | docs/DECISIONS.md | Continue Chapter 7 / The Safe Password Checker (fresh convo) |
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

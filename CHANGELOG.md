# 📜 CHANGELOG

All notable changes to the Guild of Builders, newest at the top.
We follow the spirit of Semantic Versioning: big milestones get whole numbers,
small improvements get decimals. (Kaizen, with a memory.)

---

## [Unreleased]
### Added
- `docs/DECISIONS.md` — locked D-20 through D-25: the Typing Dojo & side-quest world (optional, never gating, unlocks by skill), the Engine + Skin architecture (canonical programs as the durable asset), the four-tier mastery ladder (Typing Dojo → Detective Mode → Dragon Debug's Den → The Lost Heaven, v1 builds only the first two), strategic repetition as an intentional exception to DRY for the learner, discovery-must-self-select (no "NEW UNLOCKED!" banners), and "The Art of Teaching Without Any Teaching" as a named canon principle.
- `typing_dojo/README.md` (v1.0, frozen system spec) — added the Typing Dojo, an arcade of typing missions living alongside the main story: the Engine + Skin model (canonical programs in `coding_gold_mine/`, story wrappers in `missions/`), four mastery tiers (Typing Dojo, Detective Mode, Dragon Debug's Den, The Lost Heaven — v1 builds only the first two), the frozen one-screen mission format (Passive Memory + Detective Mode challenges, typos-only bugs), and Batch 01's first ten missions from Guess the Number through Tiny Chatbot.
- `manuscript/volume_1/07_the_safe_password_checker.md` — added Volume I, Chapter 7 (The Safe Password Checker): teaching **booleans** (`True`/`False`), **`len()`**, and the flag-words **`and`**, **`or`**, **`not`** — Sir Boolean joins the crew, and Captain Byte learns why one blurry `and`-guard lets `"password"` slip through, while separate `if` / `elif` questions catch it and explain why.
- `docs/HUMAN_AI_MANIFESTO.md` (DRAFT) — added the Human & AI Manifesto, Volume IV's philosophical capstone credo preparing a Builder's "righteous mindset" for the Human+AI age; structured by Brave (see `DECISIONS.md` D-17).
- `docs/SERIES_OUTLINE.md` — added the whole-series chapter map (30,000-ft view), all four volumes; Volume I near-canon, Volumes II–IV a compass rather than a contract.
- `docs/BUILDERS_LOGBOOK.md` (DRAFT) — added the Builder's personal progress tracker: Guild Ranks (earned by shipping, not speed), pacing tracks (Fast/Standard/Gentle), and the Fog Creatures' weapons list (see `DECISIONS.md` D-15, D-16).
- `docs/SETUP.md` (DRAFT/reference) — added "Preparing for the Voyage": install steps and the per-volume requirements ladder, kept out of the manuscript per `DECISIONS.md` D-13 since install facts drift.
- `docs/CHARACTERS.md` modified — added the **Fog Creatures** (DRAFT): the inner-antagonist roster (Fog of "I Can't," Snooze Kraken, Quicksand of Later, Gremlin of Never-Good-Enough, Siren of Distraction) plus later-volume seeds (Stage-Fright Wraith, Shortcut Serpent, Ego Gremlin) — distinct from the external, friendly Bug Monster.
- `docs/PROJECT_BIBLE.md` modified — added section 6.5, **The Widening Circle**, the series' thematic spine (self → family → community → world across Vol I–IV), and linked the Human & AI Manifesto into the AI Philosophy section (see `DECISIONS.md` D-17, D-18).
- `MASTER_BOOT.md` modified — file index and boot sequence reorganized to include `SERIES_OUTLINE.md`, `SETUP.md`, `BUILDERS_LOGBOOK.md`, and `HUMAN_AI_MANIFESTO.md`, and reordered so `AI_WORKING_AGREEMENT.md` and `DECISIONS.md` are read first.
- `docs/DECISIONS.md` — locked D-13 through D-19: semantic-Markdown authoring with per-device responsive rendering (print/e-ink/web), the professionalism ladder & "In the Real World" box, personal-mastery progress with no reader-vs-reader leaderboard, flexible age-informed pacing bands (a map not a deadline), the Human & AI Manifesto as Volume IV canon, the Widening Circle as the series' thematic spine, and an original-creations-only (no copyrighted IP) policy.
- `manuscript/volume_1/06_the_secret_treasure.md` — added Volume I, Chapter 6 (The Secret Treasure): teaching **`while` loops**, **`!=`**, **`random.randint()`**, the infinite loop as a rite-of-passage bug, and the counter pattern (`attempts = attempts + 1`) — Captain Byte hunts a hidden number and learns every loop needs a way out.
- `manuscript/volume_1/05_rock_paper_scissors.md` — added Volume I, Chapter 5 (Rock, Paper, Scissors): teaching **`import`** (waking up a module), **`random.choice()`** (the tool of chance), the difference between `=` and `==`, and the word **`and`** — Captain Byte faces Ninja Cat and teaches the ship to be unpredictable.
- `manuscript/volume_1/04_ninja_health_check.md` — added Volume I, Chapter 4 (The Ninja Health Check): teaching **`float`** (numbers with a dot), arithmetic operators (`*`, `/`) with bracket precedence, and **`round()`** — Captain Byte calculates a readiness score to cross the Cliffs of Health.
- `docs/CLAUDE_PROJECT_CONFIG.md` modified — handoff to Codie made explicit: the Claude Project no longer logs or touches Git itself; it just reminds Brave to (a) ship the finished chapter with Codie and (b) re-sync the repo into Project knowledge before the next chapter.
- `manuscript/volume_1/03_the_age_machine.md` — added Volume I, Chapter 3 (The Age Machine): teaching **`if` / `elif` / `else`** (control flow) and comparisons (`>=`, `<=`, `==`, `>`, `<`) — the ship refuses to move until Captain Byte's age is turned into a decision.
- `manuscript/volume_1/02_hungry_pizza_robot.md` — added Volume I, Chapter 2 (The Hungry Pizza Robot): teaching **`input`** (the program asks and listens) and the classic "input is always text" bug (`"3" * 2 == "33"`), fixed with `int`.
- `docs/CLAUDE_PROJECT_CONFIG.md` modified - Claude Code auto logging changelog.md, roadmap.md. No need to instruct how to add entries in changelog, roadmap and remind git commit > push
- `manuscript/volume_1/01_captain_byte_sets_sail.md` — added Volume I, Chapter 1 (Captain Byte Sets Sail): the Builder's first real line of Python, teaching **variables** (a box with a name) and the first `NameError` as a conversation.
- `.claude/commands/ship-chapter.md` added — one-command log + commit for pasted chapters (Codie stays out of authoring).
- `docs/CLAUDE_CODE_QUICKSTART.md` added - (Claude Code onboarding + a ready CLAUDE.md that auto-boots the workflow).
- `manuscript/volume_1/00_welcome.md` - added Volume I, Chapter 0 (Welcome): the cold-open that recruits the Builder. Story only, no syntax yet.
- `docs/STYLE_GUIDE.md` (style guide v1.1) added Real World box | In the Real World box + professionalism ladder 
- `docs/CHARACTERS.md` (v1.2) — added Sir Quizzalot, co-master of the Riddle Theatre (the pompous-knight foil to Maestro Monty).
- `docs/CHARACTERS.md` (v1.1) — added Professor Pycasso (the Artist) and Maestro Monty (the Riddle-Theatre Master) to the DRAFT supporting cast.
- `docs/CLAUDE_PROJECT_CONFIG.md` — Claude Project custom instructions + knowledge setup.
- `docs/AI_WORKING_AGREEMENT.md` — the session playbook that protects against AI drift.
- `workbook/_TEMPLATE_mission.md` — copy-paste mission template.
- `manuscript/_TEMPLATE_chapter.md` — copy-paste chapter template.
- `docs/TREASURE_CHEST.md` — backlog for good-but-not-yet ideas.
- `CHANGELOG.md` — this file.

## [1.0] — Foundation
### Added
- Repository scaffold and all governing documents:
  `MASTER_BOOT`, `README`, `PROJECT_BIBLE`, `CHARACTERS`, `STYLE_GUIDE`,
  `CURRICULUM`, `GAME_DESIGN`, `ROADMAP`, `DECISIONS`, `CONTRIBUTING`,
  `GIT_GUIDE`, `LICENSE`, `.gitignore`.
- Folder structure: `docs/`, `manuscript/`, `workbook/`, `source_code/`, `assets/`, `teacher/`.

# 📜 CHANGELOG

All notable changes to the Guild of Builders, newest at the top.
We follow the spirit of Semantic Versioning: big milestones get whole numbers,
small improvements get decimals. (Kaizen, with a memory.)

---

## [Unreleased]
### Added
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

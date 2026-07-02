# CLAUDE.md — Guild of Builders

We are not teaching Python. We are raising Builders.
NORTH STAR — before adding anything, ask: "Will this help a child become a better Builder?"
If no, it goes in docs/TREASURE_CHEST.md, not the book.

## Boot (read before writing anything)
1. docs/AI_WORKING_AGREEMENT.md   — how a session runs
2. docs/PROJECT_BIBLE.md          — LOCKED vision & principles
3. docs/DECISIONS.md              — settled calls (don't reopen LOCKED)
4. docs/ROADMAP.md                — where we are + this session's ONE goal
5. docs/CHARACTERS.md, docs/STYLE_GUIDE.md, docs/CURRICULUM.md, docs/GAME_DESIGN.md — as needed

## The Five Rules
1. One artifact per session. Edit ONE file (or a tiny related set). Never rewrite the world.
2. Edit files, don't re-dump them in chat. Ship a new version (v1.0 -> v1.1).
3. Every session ends with a real donut: a downloadable/runnable file, committed.
4. The North Star governs every addition.
5. Stay in canon: characters per CHARACTERS.md, voice + accessibility per STYLE_GUIDE.md.

## Canon quick-ref
- Captain Byte (brave, funny, pizza, creates the problems that become lessons)
- Dragon Debug (patient mentor — "Make it work. Make it clear. Make it kind." / tea)
- Professor Quackers (silent rubber duck; teaches by listening)
- TommyBot (every Builder; curious, learns by asking)
- Errors are conversations: "Excellent. Now the conversation begins."
- Accessibility is mandatory (Teppy, mild dyslexia): short lines, whitespace, plain words.
- ONE game, FOUR generations — it EVOLVES, never restarts.

## Code
- All Python shipped in a chapter must be real and tested before it goes in.
- Volume I uses only Volume I skills.

## Commit convention
- After shipping, update docs/ROADMAP.md session log + CHANGELOG.md, then:
  git add . && git commit -m "..." && git push
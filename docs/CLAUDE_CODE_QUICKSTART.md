# ⚓ Claude Code — Guild of Builders Quickstart

> For Brave. Assumes you can drive a terminal and Git.
> Goal: run Claude Code *inside* the repo so it reads the live files, edits in place,
> and commits — no more manual uploads. The repo becomes the memory, literally.

---

## 0. What it is (one line)

The same Claude, running in your project folder with hands on the filesystem and Git —
instead of chatting through uploads.

---

## 1. Requirements

- macOS 13+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (WSL or Git for Windows).
- Git installed (on native Windows, install **Git for Windows** so Claude Code gets Bash).
- A Claude **Pro/Max** subscription (recommended — unified login) *or* a Claude Console account with credits.
- Node.js 18+ is **only** needed if you take the deprecated npm route below. The native install doesn't need it.

---

## 2. Install (native — recommended)

**macOS / Linux / WSL**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell**
```powershell
irm https://claude.ai/install.ps1 | iex
```

Also available via Homebrew (`brew install claude-code`) and WinGet (`winget install Anthropic.ClaudeCode`); those don't auto-update.

**npm (deprecated, still works):**
```bash
npm install -g @anthropic-ai/claude-code
```
Don't use `sudo`. If you go this route, upgrade with `npm install -g @anthropic-ai/claude-code@latest`.

Check the install anytime:
```bash
claude doctor
```

---

## 3. Auth + first run

```bash
cd path/to/guild-of-builders
claude
```

First launch prompts you to log in (browser). Pick your **Pro/Max** account for the unified
subscription, or Console if you're on pre-paid credits. Switch later with `/login`.

That's it — you're in the repo, in a session.

---

## 4. The one thing that makes this sing: `CLAUDE.md`

Claude Code reads a file called **`CLAUDE.md`** at the repo root at the **start of every session**.
This is where you encode the boot sequence *once* so every session auto-boots in canon — no
re-explaining, no re-uploading. This is the Claude Code equivalent of your Working Agreement.

You can auto-generate a starter by running `/init` inside a session, then trim it. Or drop in
this ready-made version:

```markdown
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
```

Commit `CLAUDE.md` to the repo. Now any machine that clones it — and every future session —
boots correctly with zero setup.

---

## 5. A session, mapped to your ritual

| Your step | In Claude Code |
|-----------|----------------|
| **Boot** | Automatic — it reads `CLAUDE.md` + the files it points to. |
| **Aim** | "What's the ONE goal from ROADMAP.md this session?" — confirm before building. |
| **Build** | "Draft manuscript/volume_1/02_hungry_pizza_robot.md, story-first, in canon." It edits the file directly. |
| **Ship** | The file *is* the donut — already on disk, no upload. |
| **Log** | "Add the ROADMAP session-log row + a CHANGELOG line for this." |
| **Commit** | "Commit with message 'Vol I Ch2: Hungry Pizza Robot' and push." It runs Git for you. |

Start each new piece of work with a clean slate: type `/clear` (your "the chat is disposable"
rule, built in).

---

## 6. Cheat sheet

| Command | Does |
|---------|------|
| `claude` | Start a session in the current folder |
| `/login` | Sign in / switch account |
| `/init` | Generate a starter `CLAUDE.md` from the repo |
| `/clear` | Wipe context, start fresh (do this between artifacts) |
| `/desktop` | Hand off to the Desktop app for visual diff review |
| `claude doctor` | Health-check the install |

---

## 7. Notes & gotchas

- Claude Code proposes edits/commands and asks before doing anything destructive — read the diffs.
- It's powerful in a repo *with* Git: you can always `git revert` if it goes sideways. Commit often.
- Keep `CLAUDE.md` lean. It's loaded every session; a bloated one wastes context (same God-Object smell you already avoid).
- Prefer the terminal, but there are VS Code / JetBrains extensions and a Desktop app if you want a GUI later.
- Official docs (bookmark these):
  - Setup: https://docs.claude.com/en/docs/claude-code/setup
  - Quickstart: https://docs.claude.com/en/docs/claude-code/quickstart
  - CLAUDE.md / memory: https://docs.claude.com/en/docs/claude-code/overview

---

🐉 *Make it work. Make it clear. Make it kind. — and let it commit the donut for you.* 🍩

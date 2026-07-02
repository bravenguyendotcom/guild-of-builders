# 🧰 GIT_GUIDE.md

### How to put the Guild of Builders on Git & GitHub — step by step

> Written for someone doing this for the first time. Take it one step at a time.
> Each block is a command you type in a terminal, then press Enter.

---

## Part 0 — One-time setup (do this once ever)

**1. Install Git.**
- Windows: download from https://git-scm.com and install with default options.
- Mac: type `git --version` in Terminal; if it's missing, it will offer to install.
- Linux: `sudo apt install git` (Debian/Ubuntu).

**2. Make a free GitHub account** at https://github.com.

**3. Tell Git who you are** (use your GitHub email):
```bash
git config --global user.name "Brave"
git config --global user.email "you@example.com"
```

---

## Part 1 — Turn this folder into a Git repository

**1. Open a terminal inside the `guild-of-builders` folder.**
(Right-click the folder → "Open in Terminal", or `cd` into it.)

**2. Start version control here:**
```bash
git init
```

**3. See what Git notices:**
```bash
git status
```
You'll see all your files listed in red (untracked).

**4. Stage everything (prepare it to be saved):**
```bash
git add .
```

**5. Make your first commit (your first saved snapshot):**
```bash
git commit -m "Phase 0: foundation documents and repository structure"
```

🎉 You now have a Git repository with its first commit — your first donut is versioned.

---

## Part 2 — Put it on GitHub

**1. On github.com, click the `+` (top right) → "New repository".**

**2. Fill in:**
- Repository name: `guild-of-builders`
- Description: *An open-source adventure that teaches children to build software, games, AI — and themselves.*
- Choose **Public** (open-source) or **Private** (just for the family) — your call.
- **Do NOT** check "Add a README" (you already have one).
- Click **Create repository**.

**3. GitHub shows you commands. Use the "…push an existing repository" ones.**
They look like this (GitHub gives you *your* exact URL — copy it):
```bash
git remote add origin https://github.com/YOUR-USERNAME/guild-of-builders.git
git branch -M main
git push -u origin main
```

**4. When it asks you to sign in:**
- The easiest path is to install **GitHub Desktop** (https://desktop.github.com) — it
  handles login for you and gives you buttons instead of commands. Highly recommended if
  you're on a touch screen.
- Or, in the browser sign-in flow when the terminal opens it, log in and authorize.

🎉 Refresh your GitHub page — your whole project is now online.

---

## Part 3 — The everyday rhythm (after each work session)

Whenever you finish a session and have a new/edited file:

```bash
git add .
git commit -m "manuscript: add Volume I, Chapter 0 (Welcome)"
git push
```

That's it. Three lines: **add, commit, push.** Your work is saved and backed up online.

> Tip: write the commit message like a tiny changelog. Future-you will thank you.
> See `CONTRIBUTING.md` for message examples.

---

## Part 4 — Marking a release (end of a volume)

When Volume I is finished and polished:
```bash
git tag v1.0
git push origin v1.0
```
On GitHub, go to **Releases → Draft a new release**, pick tag `v1.0`, and write a short
note ("Volume I — The First Voyage: playable CLI game complete"). That's a real milestone. 🏴‍☠️

---

## If you prefer buttons over commands (recommended for touch screens)

Use **GitHub Desktop**:
1. Install it, sign in.
2. "Add local repository" → select the `guild-of-builders` folder.
3. From then on: it shows your changes; you type a summary and click **Commit**, then
   **Push origin**. Same idea as add/commit/push, but with buttons.

---

## The mental model (so Git stops feeling scary)

- **commit** = "save a snapshot with a label." Like a checkpoint in a game.
- **push** = "upload my snapshots to GitHub."
- **pull** = "download the latest snapshots" (matters when working on two devices).
- You can always go back to any past commit. Nothing is truly lost. That's the point.

---

🐉 *Version control is just Kaizen with a memory. Make it work. Make it clear. Make it kind.*

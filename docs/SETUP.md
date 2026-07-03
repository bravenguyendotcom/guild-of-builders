# ⚓ SETUP.md — Preparing for the Voyage

### How to get Python running, and what you'll need as the adventure grows

> **Status:** DRAFT (reference — facts here drift; update as tools change).
> **Why this is a reference, not a chapter:** install steps and version numbers change over
> time, so per `DECISIONS.md` D-13 they live here where they're easy to update — not baked
> into the story. A kid-facing manuscript pre-chapter ("Preparing for the Voyage") will draw
> from this doc in friendly, story voice.

---

## The golden rule of setup

**You need almost nothing to start.** 🍩

Don't let "getting ready" become a wall in front of the fun. For the very first chapters, a
free browser tab is enough. You can set up a "real" workshop later, when the game grows and
actually needs it. *Version 1 beats perfect.* Start building; upgrade the workshop as you go.

---

## Two ways to run Python

### 🚀 Path A — No install (fastest; great on mobile)

Open an **online Python editor** in any browser and start typing. Examples (check what's
current): the interactive console on **python.org**, **Google Colab**, or **Replit**.

- **Best for:** Volume I's early missions, and for anyone on a phone or a school Chromebook.
- **Watch out:** some online tools forget your files when you close the tab. Once you start
  *saving* your game (Volume II), you'll want Path B.

### 🖥️ Path B — Install Python on your computer (grows with you)

This is the real workshop. Get **Python 3.14 or newer** (grab the latest from **python.org**).

**Windows**
1. Download the installer from python.org (or the Microsoft Store).
2. **Tick "Add Python to PATH"** during install (important!).
3. Open a terminal and check: `python --version`

**macOS**
1. Download the installer from python.org. *(Don't rely on the old system Python.)*
2. Check in Terminal: `python3 --version`

**Linux**
1. It's often already there: `python3 --version`
2. If not, install with your package manager (e.g. `sudo apt install python3`).

**To run your program:** save a file like `adventure.py`, then in the terminal type
`python adventure.py` (or `python3 adventure.py` on Mac/Linux).

---

## 📱 Mobile reality check (read this, Captain)

You *can* start on a phone — and that's wonderful for trying the early missions anywhere.

- **Android:** an app like **Pydroid 3** runs real Python on the phone.
- **iPhone / iPad:** apps like **a-Shell** or **Pythonista**, or just use an online editor
  in the browser (Path A).

**The honest part:** mobile is a great place to *start*, not to *finish*. The early CLI game
(Volume I) runs fine. But the graphics and screens of **Volume III**, and the AI of
**Volume IV**, really want a real computer. Think of mobile as the rowboat that gets you off
the shore — you'll want the full ship for the open sea.

---

## ✍️ Where you write your code (the editor)

- **Start simple:** the online editor, or **IDLE** (it comes free with Python).
- **Grow into a real editor** when you're ready — **VS Code** is free and widely used.

You do **not** need a fancy editor on day one. A real editor is a tool you grow *into*, not a
gate you must pass through first. (This is the professionalism ladder from `STYLE_GUIDE.md`:
first just *run* code; adopt pro tools as the work asks for them.)

---

## 🪜 The Requirements Ladder — what you need, volume by volume

This is the important part: it keeps every "you'll build a real game" promise **honest.**

| Volume | What you need | Device | New tools this volume |
|--------|---------------|--------|-----------------------|
| **I — First Voyage** (CLI game) | Python 3.14+ only — **no extra installs** (standard library) | Any: computer, phone, or online | An editor (online / IDLE) |
| **II — Growing** (save/load, modules) | Python + the ability to **save files** to a real disk | **Computer recommended** (online sandboxes lose files) | A real editor; first taste of `pip` / a virtual environment |
| **III — Living World** (graphics/web, published) | A real computer + **installable libraries** (via `pip`); a browser to test & share | **Computer required** (Win/Mac/Linux) — not mobile | Virtual environments as standard; a GUI/web library *(exact stack TBD — see DECISIONS)* |
| **IV — Infinite Guild** (AI) | Computer + internet + an **AI account/key**; **Git + a GitHub account** | **Computer required** | An AI provider *(TBD — see DECISIONS)*; Git & GitHub; care with keys & privacy |

> **Open on purpose:** the Volume III web/GUI library and the Volume IV AI provider are **not
> locked yet** (parked in `DECISIONS.md`). This doc will name them when those decisions are made.

---

## 🧰 Two words you'll meet later (don't worry now)

- **`pip`** — Python's tool for installing extra "libraries" (ready-made toolkits). You'll
  meet it when the game first needs something beyond the basics (around Volume II–III).
- **Virtual environment** — a clean, separate toolbox *per project*, so different games don't
  trip over each other's tools. A professional habit you'll grow into, not a day-one worry.

You'll learn each of these **in the chapter that needs it** — story first, never ahead of time.

---

## 👪 A note for parents — Volume IV (AI)

Volume IV uses an AI service, which means an account and possibly a little money.

- **A parent should set up the AI account and any API key**, and **set a spending limit** (free
  tiers are usually plenty for learning).
- Treat keys like passwords — never share them or paste them into public code.
- This ties straight into the series' ethics thread (*"make it kind"*): being a Builder
  includes being careful, honest, and safe with powerful tools.

---

## The spirit of this page

Setup should feel like packing a small bag for a big adventure — not like studying for an
exam. Grab the little you need, and set sail. The ship gets better *while* you're sailing it.

⚓ *You don't need the whole ocean today. You need one first step off the shore.*

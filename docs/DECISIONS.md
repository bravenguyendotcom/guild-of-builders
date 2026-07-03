# 🧭 DECISIONS.md

### The decision log — what we decided, and *why*

> **Status:** LIVING.
> This file exists so that six months from now, nobody re-opens a settled argument.
> Each decision is **LOCKED** (sacred — don't reopen without a very good reason) or
> **OPEN** (still up for discussion). Add new decisions at the bottom.

Format (like a software project's ADR — Architecture Decision Record):

```
### D-XX — Title
Status: LOCKED | OPEN
Decision: ...
Reason: ...
```

---

### D-01 — The project's true purpose
**Status: LOCKED**
**Decision:** We are raising *Builders*, not teaching Python. Python is the vehicle.
**Reason:** It's the emotional heartbeat and the North Star. Every other choice flows from it.

---

### D-02 — One game, four generations
**Status: LOCKED**
**Decision:** There is one project — *Captain Byte's Treasure Quest* — evolved across four
volumes (CLI → bigger game → published GUI/web → AI-powered). It is never restarted.
**Reason:** Children get emotionally attached to what they build. Throwing it away each
volume would break that attachment. Evolving it teaches real iterative development.

---

### D-03 — Language of the book
**Status: LOCKED**
**Decision:** The book is written **100% in English**.
**Reason:** Matches international CS materials, builds tech vocabulary, and prepares Tommy
and Teppy to read real documentation and AI/ML resources later.

---

### D-04 — Audience & accessibility
**Status: LOCKED**
**Decision:** Primary readers are Tommy (Grade 8) and Teppy (younger, mild dyslexia).
Accessibility rules (short lines, whitespace, plain words) are mandatory.
**Reason:** The book must welcome Teppy on every page, and any 10–15 year old beginner.

---

### D-05 — The canonical cast
**Status: LOCKED**
**Decision:** Captain Byte 🏴‍☠️, Dragon Debug 🐉, Professor Quackers 🦆, and TommyBot 🤖 are
permanent and appear across all volumes. New characters only when the story needs them.
**Reason:** Familiar faces are emotional landmarks; consistency earns the reader's trust.

---

### D-06 — Document architecture (no God Object)
**Status: LOCKED**
**Decision:** The project is many single-purpose documents, not one giant file. The
`PROJECT_BIBLE` governs; it does not contain the curriculum, manuscript, or code.
**Reason:** We caught ourselves pouring everything into one file — that's how projects
become spaghetti. One artifact, one job.

---

### D-07 — The Donut Law
**Status: LOCKED**
**Decision:** Every substantial session ends with a real, downloadable/runnable artifact
committed to the repo. No promises, no placeholders.
**Reason:** "Mommy's Donuts" (promised-but-undelivered files) killed momentum. Real donuts
keep the project honest and moving.

---

### D-08 — Edit artifacts, don't rewrite in chat
**Status: LOCKED**
**Decision:** We never rewrite a whole document inside a conversation. We edit the file and
ship a new version (v1.0 → v1.1 → ...) under version control.
**Reason:** It's how real software is maintained, and it protects against AI context limits.

---

### D-09 — Story first, Python second
**Status: LOCKED**
**Decision:** Every concept is motivated by the story before any syntax appears.
**Reason:** Wonder before syntax. It's the core teaching method.

---

### D-10 — Errors are conversations, not failures
**Status: LOCKED**
**Decision:** Debugging is framed as *"the computer and I are having a conversation."*
The house phrase: **"Excellent. Now the conversation begins."**
**Reason:** This single mindset shift separates fearful learners from confident engineers.

---

### D-11 — Version control with Git & GitHub
**Status: LOCKED**
**Decision:** The project lives in a Git repository on GitHub, open-source.
**Reason:** It teaches real workflow, enables versioning/releases, and lets the work be
shared and (eventually) contributed to by others.

---

### D-12 — Working title
**Status: OPEN**
**Decision (provisional):** *The Guild of Builders.*
**Reason:** Captures "raising Builders" and the community feel. Open to a better final title
before the first public release.

---

### D-13 — Author semantic Markdown; render responsively per device
**Status: LOCKED** (the principle) — **tooling OPEN**
**Decision:** The manuscript separates **content from presentation.** We author clean,
semantic Markdown and let each output format apply its own accessibility-first styling.
- **Source convention:** one sentence (or one intentional poetic beat) per line, with a
  blank line between paragraphs. This gives clean git diffs and easy edits. These
  per-sentence lines **reflow** — so we **never hard-wrap mid-sentence to force a column
  width**, and we **never bake layout into the source.**
- **Outputs, each responsive:**
  - *Print / PDF (color on paper):* measure ~60–70 characters/line, generous margins,
    dyslexia-friendly body font ~12–14pt, line spacing ~1.4–1.5, **left-aligned (never
    justified)**, no forced hyphenation.
  - *E-ink (Kindle / Kobo Clara Color):* export **EPUB** with minimal styling and **let the
    reader control font size and spacing** (vital for Teppy). Don't override reader settings.
  - *Mobile / web:* responsive HTML, `max-width` ~60–66 characters, comfortable spacing,
    dark mode.
- **The cross-device rule:** design to be **legible in grayscale first**; color is an
  enhancement, **never** the only carrier of meaning (Kindle is grayscale; Kobo Clara Color
  is low-saturation). The emoji character tags (🐉 🏴‍☠️ 🦆) carry meaning without color — keep it that way.

**Reason:** One source, many devices. Baking layout into the manuscript would break every
format except the one it was tuned for, and would hurt the exact reader we protect most
(Teppy, who needs to resize text freely). Authoring semantically keeps the work future-proof
and accessible everywhere.

**Still open (tooling):** the build tool (e.g. Pandoc) and per-format stylesheets are not
yet chosen. A future `docs/PUBLISHING.md` will specify the pipeline. Until then, this
principle governs how chapters are written.

---

### D-14 — The professionalism ladder & the "In the Real World" box
**Status: LOCKED**
**Decision:** Every volume gradually builds real-world professionalism through a recurring
🏗️ **"In the Real World"** box (rules in `STYLE_GUIDE.md` v1.1): after the story, never inside
it; max 3–4 lines; real vocabulary in bold; warm; optional; true things only. The ladder:
**Vol I vocabulary → Vol II rituals → Vol III artifacts → Vol IV the room.**
**Reason:** Wonder builds Builders, but confidence in the real world comes from *recognition*
— "I've done this, it has a name." The ladder lands the ultimate goal (proposing a real
solution with confidence) as the top rung, reached gradually, never as a leap.

---

### D-15 — Progress is personal: race yourself, never a leaderboard
**Status: LOCKED**
**Decision:** Motivation is built on **personal mastery (Kaizen)**, not competition between
readers. No reader-vs-reader leaderboard. Tools: personal **Guild Ranks** (earned by
*shipping* a volume's game, not by speed), a self-tracked **Builder's Logbook**, and playful,
non-shaming "world records" (ridiculous or personal-best only). The real enemies are the
**Fog Creatures** — the negative-self (procrastination, self-doubt, perfectionism) — which
visit *every* Builder and are never used to shame a child. (See `BUILDERS_LOGBOOK.md`, `CHARACTERS.md`.)
**Reason:** A competitive ranking would break the LOCKED emotional rules (never shame;
celebrate Version 1; every pace welcome) and hurt the reader we protect most (Teppy).
*"Finishing is the achievement. When you finish is not the point."*

---

### D-16 — Flexible, age-informed pacing (a map, not a deadline)
**Status: LOCKED** (bands OPEN to tuning)
**Decision:** Provide gentle whole-series time estimates as guidance, not deadlines:
**8–11 ≈ 6–10 months · 12–15 ≈ 3–6 months · 16+ ≈ 2–4 months** (≈6 weeks if focused &
experienced). Assumes ~2–4 hrs/week. Pace naturally slows in Vol III–IV (heavier). Three
switchable tracks (Fast / Standard / Gentle); fast finishers get side-quests & build-your-own
so they're never bored. (See `BUILDERS_LOGBOOK.md`.)
**Reason:** A project needs scope and forecasts, but pace must never shame. Different kids,
different speeds — the finish line doesn't move.

---

### D-17 — The Human & AI Manifesto is Volume IV canon
**Status: LOCKED** (text DRAFT/evolving)
**Decision:** Volume IV includes the **Human & AI Manifesto** (`docs/HUMAN_AI_MANIFESTO.md`) as
its philosophical capstone — structured by Brave, rendered in English (D-03). It prepares a
"righteous mindset" for the Human+AI age and is the source text for the Vol IV manuscript.
It expands the Bible's "AI Philosophy" section.
**Reason:** As capability grows, responsibility must grow with it. This is the maturity weight
of Vol IV, and among the most important things the series gives a child.

---

### D-18 — The Widening Circle is the series' thematic spine
**Status: LOCKED**
**Decision:** Impact widens as the Builder grows: **self → family/friends → community → world**,
mapped onto the four volumes (Vol I build for me · II for my people · III for society · IV for
the world). The weight of responsibility arrives *late* (Vol IV), after the wonder is earned.
*(To be recorded as a theme in `PROJECT_BIBLE.md`; already threaded in `HUMAN_AI_MANIFESTO.md` Part VII.)*
**Reason:** It gives the series a moral through-line without preaching, and points exactly where
we hope a Builder lands — helping others, maybe even building *with* Dad.

---

### D-19 — Original creations only (IP-safe homages)
**Status: LOCKED**
**Decision:** Because the series is open-source and meant to be published, it uses **no
copyrighted or trademarked characters/IP** (e.g. Marvel's Doc Ock, Spider-Man, Disney, Nintendo).
Inspiration is welcome; we keep the *fun mechanic* and give it an **original Python-Planet skin**
(e.g. the typing-boss "The Tangle / Typo-Squid" instead of Doc Ock). Song lyrics, etc., likewise
original.
**Reason:** Protects the project legally and teaches Builders to create, not copy. *"Kids look
at us to learn."*

---

## Open questions parked in the Treasure Chest 🧰
_(not decided yet — revisit when relevant, don't let them block progress)_

- Final public title & cover.
- License choice specifics (see `LICENSE` — currently permissive placeholder).
- Which web framework for the Volume III published game.
- Which AI provider(s) for Volume IV.
- Whether to build a companion website with live hints/tests.
- **Side-quests doc** (`docs/SIDE_QUESTS.md`) — home for the Typing Dojo/"The Tangle" and fast-finisher extras (incl. optional ZTM-style breadth as *side-quests only*, never core spine).
- The publishing pipeline & tool (Pandoc?) + per-format stylesheets — to become `docs/PUBLISHING.md` (see D-13).

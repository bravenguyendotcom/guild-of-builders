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

## Open questions parked in the Treasure Chest 🧰
_(not decided yet — revisit when relevant, don't let them block progress)_

- Final public title & cover.
- License choice specifics (see `LICENSE` — currently permissive placeholder).
- Which web framework for the Volume III published game.
- Which AI provider(s) for Volume IV.
- Whether to build a companion website with live hints/tests.

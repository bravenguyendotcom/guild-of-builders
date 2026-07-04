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
*(Recorded as a theme in `PROJECT_BIBLE.md` §6.5; threaded in `HUMAN_AI_MANIFESTO.md` Part VII.)*
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

### D-20 — The Typing Dojo & the Side-Quest world
**Status: LOCKED**
**Decision:** The series has an **optional arcade beside the main spine** — the **Typing Dojo**
(`typing_dojo/`), plus a wider side-quest world. Side-quests are **always optional** (a Builder
reaches 🏛️ Guild Builder without any of them), **never gate** the main story, **unlock by skill**
(D-16 logic), use **original creatures/skins only** (D-19), and reward **personal progress, not
competition** (D-15). Their only jobs: practice typing, reward quick learners, keep them in the
Guild universe, and quietly spark curiosity. **The teaching stays in the main story.**
**Reason:** Fast Builders need somewhere to linger so they're never bored, without turning the
side-quest into another lesson. *"If a kid Googles 'what is A*?' because of a side-quest, it worked."*

---

### D-21 — Engine + Skin architecture (the durable asset is the library)
**Status: LOCKED**
**Decision:** Dojo missions are **assembled, not authored**: a **canonical Python program**
(`typing_dojo/coding_gold_mine/`, Layer 1, written once) wrapped in a lightweight **skin**
(`typing_dojo/missions/`, Layer 2 — story hook + Challenge I/II + flavor). If the concept later
deserves real teaching, the **main story** (Layer 3) does it properly, at the right time. One
engine wears many skins (one `bfs.py` → Maze Escape, Robot Vacuum, Fire Rescue…).
**Reason:** The durable investment is a curated **library of canonical programs**, not a list of
missions. Improve the engine once, every mission improves (DRY). This is what lets the Dojo scale
for years without re-designing.

---

### D-22 — The four-tier mastery ladder (v1 = tiers 1–2 only)
**Status: LOCKED** (tier *content* DRAFT)
**Decision:** The Dojo grows through four tiers, each training a different faculty:
🥋 **Typing Dojo** (fingers) → 🕵️ **Detective Mode** (eyes) → 🐉 **Dragon Debug's Den** (mind /
logic bugs) → ☁️ **The Lost Heaven** (systems thinking / whole unfamiliar codebases). Each tier
**unlocks by skill**, so later tiers naturally arrive in later volumes. **v1 builds only tiers 1–2.**
The Den and The Lost Heaven are **parked design seeds** (need debugging / OOP / multi-file skills).
Detective Mode uses **typos only — never logic bugs.** The Lost Heaven openly invites an **AI
companion** (ties to `HUMAN_AI_MANIFESTO.md`).
**Reason:** A clean progression from precision → observation → reasoning → systems, delivered as
places to explore, never as graded levels.

---

### D-23 — Strategic repetition is intentional (for the learner, not the code)
**Status: LOCKED**
**Decision:** The Dojo deliberately repeats ideas: the same engine returns under many skins;
**Echo Missions** are earlier missions in a new costume; author-only tags mark maturity
(🌱 Seed → 🌿 Sprout → 🌳 Tree → 🌲 Forest). The goal: *"meet a beautiful idea hundreds of times
until your fingers know it before your brain does."*
**Reason:** Fluency is carved by repetition, like music or martial arts. This is a conscious
exception to "Don't Repeat Yourself" — DRY governs the *codebase* (D-21); repetition governs the
*learner*. The two never conflict.

---

### D-24 — Don't advertise the treasures; discovery must self-select
**Status: LOCKED**
**Decision:** Side-quests (especially Dragon Debug's Den and The Lost Heaven) are **not announced**
with "NEW UNLOCKED!" banners. At most, a small in-world sign. `TREASURE_CHEST.md` is the **Guild
Masters' private notebook** (for authors), not a public feature list shown to Builders. We do not
prescribe the treasures — not even to Tommy and Teppy.
**Reason:** *"Discovery loses something when it's prescribed."* Prescribed treasure becomes
homework; found treasure becomes *their* adventure. Invitation beats obligation.

---

### D-25 — The Art of Teaching Without Any Teaching
**Status: LOCKED**
**Decision:** The project optimizes **curiosity**; education is the *side effect*. Builders should
rarely feel they are studying — they feel they are solving mysteries, fixing machines, helping
friends, exploring worlds, chasing bugs, discovering treasures. Principle: *don't teach computer
science — let children behave like computer scientists.* Full text lives in `docs/PHILOSOPHY.md`;
this entry records the principle as canon.
**Reason:** The best teaching becomes invisible. Years later a Builder can't name who taught them
debugging — *"I just kind of grew up doing it."* That is the highest compliment the series can earn.

---

### D-26 — The workbook is embedded in the manuscript, not a separate track
**Status: LOCKED**
**Decision:** Missions live *inside* the story chapters, not in a parallel `workbook/` of
standalone worksheets. The shipped chapters (0–7) already fold story + coding task +
teaching-bug + achievement into one flowing read, and that is the model going forward. The
worksheet elements worth keeping (the **Testing Table** and **Debug Log**) become **boxes inside
chapters**, not a separate document. `workbook/` is **retired as an authored track**: it keeps a
short `workbook/README.md` pointer (missions now live in the chapters; see D-26), and
`_TEMPLATE_mission.md` is **deprecated** (kept for reference). The **Typing Dojo** (`typing_dojo/`)
remains the distinct *pure-practice* track with its own one-screen format (no worksheets — D-22).
`STYLE_GUIDE.md` §4 (the mission-template section) is to be updated to match (next session).
**Reason:** One flowing read is more accessible (Teppy) than story-then-worksheet, roughly halves
the authoring burden, and matches how chapters are *actually* being written. It also removes a
drift trap: three different "mission" formats (workbook worksheet vs. embedded-in-chapter vs.
Dojo one-screen) previously disagreed. Now each track has one clear job.

---

## Open questions parked in the Treasure Chest 🧰
_(not decided yet — revisit when relevant, don't let them block progress)_

- Final public title & cover.
- License choice specifics (see `LICENSE` — currently permissive placeholder).
- Which web framework for the Volume III published game.
- Which AI provider(s) for Volume IV.
- Whether to build a companion website with live hints/tests.
- **Side-quests doc** (`docs/SIDE_QUESTS.md`) — home for the Typing Dojo/"The Tangle" and fast-finisher extras (incl. optional ZTM-style breadth as *side-quests only*, never core spine).
- **Future side-quests (seeds, not commitments):** Dragon Debug's Den (logic-bug hell levels), The Lost Heaven (fix whole unfamiliar projects), The Time Machine, Archaeology, The Museum, Reverse Engineering, Bug Zoo, Hall of Fame, Blacksmith (refactor ugly→beautiful), The Librarian (read-only), Whispering Compiler (explain errors), Ghost Repository (revive abandoned projects).
- **`docs/PHILOSOPHY.md`** — write up "The Art of Teaching Without Any Teaching" (recorded as D-25). ✅ done.
- The publishing pipeline & tool (Pandoc?) + per-format stylesheets — to become `docs/PUBLISHING.md` (see D-13).
- **`STYLE_GUIDE.md` §4 update** — revise the mission-template section to match D-26 (workbook embedded in the manuscript; keep Testing Table & Debug Log as in-chapter boxes).

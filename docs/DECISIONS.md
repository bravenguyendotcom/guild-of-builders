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
(`typing_dojo/missions/`, Layer 2 — story hook + the tier(s) the topic deserves + flavor). If
the concept later deserves real teaching, the **main story** (Layer 3) does it properly, at the
right time. One engine wears many skins (one `bfs.py` → Maze Escape, Robot Vacuum, Fire Rescue…).
*(Wording clarified to the finalized tier vocabulary — see D-28; the decision itself is unchanged.)*
**Reason:** The durable investment is a curated **library of canonical programs**, not a list of
missions. Improve the engine once, every mission improves (DRY). This is what lets the Dojo scale
for years without re-designing.

---

### D-22 — The four-tier mastery ladder *(merged into D-28)*
**Status: MERGED → see D-28.**
This entry's content was finalized and absorbed into **D-28** (finalized tier names, taglines,
the honor rule, tiers-as-repetition). The number is kept so older references don't break;
**D-28 is the single source of truth for the Dojo tiers.** Nothing to see here — sail on. 🐉

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

### D-27 — Dragon Debug owns the Typing Dojo; The Tangle guards it
**Status: LOCKED**
**Decision:** **Dragon Debug** is the owner/host of the Typing Dojo (`typing_dojo/`). **The
Tangle** (the Typo-Squid, D-19) is its guardian. They are not enemies — it's a double-act:
Dragon Debug pretends the squid is a nuisance he "hasn't gotten around to removing" (*sips tea*,
*"one day I'll deal with that squid"*), but he keeps it **on purpose** — a Dojo with nothing to
push against teaches nothing. The running secret (teased, never told): type cleanly enough and
The Tangle doesn't get *defeated*, it gets *bored and impressed* and wanders off to find a
sloppier Builder. Dragon Debug never admits he planned it. **Quackers knows. Quackers says nothing.** 🦆
**Reason:** Gives the Dojo a canonical host (a permanent hero, D-05) and a warm, funny mystery
that fits both characters — and plants *"wait, is the Tangle actually helping me?"* curiosity,
which is osmosis-flavored (D-25). Recorded in `CHARACTERS.md` and `typing_dojo/README.md`.

---

### D-28 — The four Dojo tiers (finalized names; supersedes D-22)
**Status: LOCKED** (tier *content* DRAFT)
**Decision:** The Typing Dojo grows through **four tiers**, each training a different faculty.
Finalized names + taglines (these are canon):
- 🥋 **Tier I — Keyboard Ninja** — *"Slice your caps."* Passive Memory: type the canonical
  program, run it, smile. Any error is probably your own typo. (Trains the **fingers**.)
- 🕵️ **Tier II — Conan's Challenge** — *"Do you have any clue?"* Detective Mode: the supplied
  code has **typos only — never logic bugs**. Find and fix them. (Trains the **eyes**.)
- 🐉 **Tier III — Dragon Debug's Den** — *"Welcome to the kingdom of bugs."* **Logic bugs are
  now allowed.** The **observable input→output must match the canonical mission**, but the
  *implementation may be twisted* (for↔while, recursion↔iteration, dict↔list, built-in↔hand-rolled).
  (Trains the **mind**.)
- ☁️ **Tier IV — The Lost Heaven** — *"You may feel lost; befriend AI for help."* Not a single
  file and **not typing**: a whole project folder to understand and fix to meet requirements —
  patterns and system design. (Trains **systems thinking**.)
- **No sub-levels.** *"Hell I–V"* is only a **difficulty rating** of how brutal a Den (Tier III)
  mission is — not a level name.
- **The honor rule (stated, enforced culturally):** in Tier III and IV you **must not open the
  Tier I/II canonical source.** That refusal to peek is what makes the challenge real.
- **Tiers = repetition (osmosis).** A mission has **only the tiers its topic deserves**:
  introductory topics ship Tier I only; important CS ideas earn more tiers — *because more tiers
  = more times the idea is carved into memory* (D-23). A topic's tier-siblings may publish as
  **separate mission IDs**, so a learner never knows they're the same idea in a new costume.
**Reason:** The ladder is secretly the real software workflow — Developer (copy) → Reviewer
(proofread) → Senior Engineer (code review) → Architect (systems) — delivered as places to
explore, never announced as lessons. *"They start by typing and end up debugging — code, then
life, then the world's bugs."* Tier III's reward (*"You fixed the idea"*) and Tier IV's *"befriend
AI"* both loop into `HUMAN_AI_MANIFESTO.md`.

---

### D-29 — The Dojo gate splits by tier (what's in the book vs. outside)
**Status: LOCKED** (refines D-20 & D-24 for the Dojo specifically)
**Decision:** *"Don't advertise; discovery self-selects"* (D-24) does **not** apply to the gentle
tiers.
- **Tiers I & II are openly offered** — they appear at the **end of chapters from Chapter 6
  onward**, freely repeating (osmosis). Openly labeled, never hidden.
- **Tiers III & IV self-select** — reached by a quiet in-world sign, never a banner (D-24 applies
  here).
- **In the book (gentle end only):** Tiers I–II freely; **Tier III only rarely, and only at
  Hell I–II** difficulty (so an "optional" chapter-end never sandbags a kid).
- **Outside the book (the wider Dojo, reachable by URL):** **Hell III–V** Den missions and **all
  of Tier IV** live here — for quick learners and contributors. **The gate is always open — in
  and out of the book.**
**Reason:** Tier I/II are the osmosis engine and must be frequent and casual, so hiding or gating
them would defeat their purpose. Tier III/IV are the "unmarked cave" treasures curiosity finds on
its own. The URL is another multiplier and the growth path for contributors.

---

### D-30 — Dojo scope: ~50 in-book missions; the system is canon, the mountain is not
**Status: LOCKED**
**Decision:** The **book** carries roughly **one Dojo mission per chapter (~50 total across the
series)** — topics chosen carefully and smartly, multiplied by tier-variants and story "skins"
(D-21 engine/skin). The **wider library grows *outside* the book** (the Dojo repo/URL), built up
over time by curious Builders and contributors. We record the **system** as canon (engine/skin,
the four tiers, tiers-as-repetition) but **do not commit** to 300–500 canonical programs — that
number is a long-term dream, parked, not a promise.
**Reason:** *v1 > perfection.* A framework that inspires and can grow beats a mountain we can't
finish. Our task is to build the framework to practice and, ultimately, to inspire — the library
scales through contribution, not through us authoring hundreds up front.

---

### D-31 — The Inverting Mentor (Tommy doesn't start as the hero — he *becomes* one)
**Status: LOCKED**
**Decision:** The emotional spine of the whole series is a **deliberate inversion of the
mentor/student balance.** At the start, Dragon Debug knows (almost) everything and TommyBot
knows almost nothing. Across the four volumes that balance **slowly shifts** — and by Volume IV,
**Dragon Debug begins asking TommyBot questions.** Not because the dragon forgot, but because
*the student has become a Builder.* Authors thread this quietly through the cast's dialogue and
roles: TommyBot grows from asking to answering; the mentors step back as the Builder steps up.
Never announced, always felt.
**Reason:** *"Tommy should not be the hero. He should become the hero."* Children love competence
— if they grow alongside TommyBot, they feel that growth in themselves. That transformation, not
any single Python skill, is the real story the series is telling. (Voice line preserved in
`PHILOSOPHY.md`; the arc lands in `SERIES_OUTLINE.md` Vol IV.)

---

### D-32 — Builder's Heart (emotional resilience is an explicit strand)
**Status: LOCKED** (content DRAFT)
**Decision:** The series carries an explicit, recurring **EQ / resilience** thread — *Builder's
Heart* — not left to chance. It names and normalizes the real feelings of building: frustration,
anger at a stubborn bug, the urge to compare yourself to others, the fear of not being good
enough — and answers them with a **growth mindset**, the **Debug Break** (step away, breathe,
come back), and honest role models (*"real developers have broken keyboards too"*; Edison,
Jordan — greatness is built on handled failure). It is **distinct from the Fog Creatures**: the
Fog Creatures are the *enemies* (D-15); Builder's Heart is the *training* that equips a Builder
to face them. It **never shames** — every hard feeling is normal, and every one is beatable with
one small brave step.
**Reason:** The #1 reason a young Builder quits isn't difficulty — it's discouragement. Teaching
the *heart* to persevere is as important as teaching the hands to type. This is core to *raising
Builders, not coders,* and to the promise that we never shame a child (`PROJECT_BIBLE.md` §10).
A future home may be a dedicated Guild Hall / section; recorded here as canon so it's threaded
from the start.

---

### D-33 — The AI Friendship Rules (Volume IV canon, under the Manifesto)
**Status: LOCKED**
**Decision:** Volume IV teaches children to work *with* AI through **five kid-facing rules**
(the concrete, in-story companion to `HUMAN_AI_MANIFESTO.md`):
1. **Be curious.** Don't only ask *"What's the answer?"* — ask *"Can you explain it another way?"*
2. **Think first, ask AI second.** Spend five minutes trying it yourself first; you'll learn far more.
3. **Ask better questions.** Ask AI to help you *find the bug* — not to hand you the finished
   solution. Good questions create good answers.
4. **Never copy what you can't explain.** If you can't read it and say why it works, don't use it
   yet. Knowledge grows through understanding, not copying.
5. **Build together.** AI is a **teammate, not a servant.** Great teammates don't do your work —
   they help you get better at it.
**Reason:** These give the Manifesto's *"Think first. Ask AI second."* / *"Never outsource your
values."* spirit a form a child can actually hold and use. *"The best programmers don't ask AI
to think instead of them. They ask AI to think with them."* (Voice line preserved in
`PHILOSOPHY.md`; ties to D-17.)

---

### D-34 — The Guild Extras: one rotating Art / Riddle / Joke beat, every chapter
**Status: LOCKED** (content DRAFT — the library grows in `docs/GUILD_EXTRAS.md`)
**Decision:** From **Chapter 1 onward, every chapter carries exactly one "Guild Extra"** — a
short, funny beat that rotates in a fixed order: **😄 Joke → 🧩 Riddle → 🎨 Code Art → (repeat).**
- **It is separate from the Dojo.** The optional 🥋 Typing Dojo block (Ch 6+, D-29/§4a) is a
  disguised side-quest and is **not** a Guild Extra. From Ch 6 on, a chapter can carry **both**
  a Dojo block *and* its Guild Extra — they do different jobs and never substitute for each other.
- **Re-skinned to our cast only (D-05, D-19).** Extras use **our** characters — Captain Byte,
  Dragon Debug, Professor Quackers, TommyBot, Professor Pycasso, Maestro Monty & Sir Quizzalot,
  Sir Boolean, Ninja Cat, The Tangle. Foreign characters from source brainstorms (e.g. a
  snake-"Monty," Glitch, Dunder, Pip, Cal, Dr. Byte-Size) are **dropped or re-skinned**, never
  imported. Jokes drawn from public-domain programmer folklore are fine; everything is rewritten
  in our voice, never pasted.
- **🎨 Code Art follows *Run it → Hack it → Own it*.** Art extras never ask a child to copy a
  finished picture. They give a small runnable engine with "knobs" (variables/levers) and invite
  the child to change it and make it theirs — creativity over mimicry. Professor Pycasso hosts,
  with his saying: *"Every child is an artist, every terminal is a canvas."*
- **The library lives in `docs/GUILD_EXTRAS.md`** — the adapted, re-skinned content, mapped to
  chapters and rotation slots.
**Reason:** Humor and art are **load-bearing, not decoration** (the Voice museum in
`PHILOSOPHY.md`). Delivered *often*, they deepen the reader's friendship with the Guild and carry
computer-science ideas by **osmosis** (D-25) — the same repetition logic as the Dojo (D-23).
Rotating three kinds keeps every chapter fresh without overloading a page, and starting at
Chapter 1 (a joke needs no code skills) means the fun and the friendship begin on page one.
Accessibility holds: one short Extra per chapter is well within a comfortable read for Teppy.

---

### D-35 — The Advanced Pycasso's Gallery (the art-twin of the Dojo's advanced tiers)
**Status: LOCKED** (content DRAFT — the library grows in `docs/PYCASSO_GALLERY_ADVANCED.md`)
**Decision:** Alongside the per-chapter **Guild Extras** (D-34, simple and universal from Ch 1),
the project also carries an **Advanced Gallery** — skill-gated 3D/motion CLI art, exactly
parallel to the Typing Dojo's higher tiers (D-28). It is **not** part of the Ch-1+ rotation;
it is reached by curious Builders in the **later volumes**, and by contributors in the
**open-source gallery** (same "mountain grows outside the book" logic as D-30).
- **Seed showpieces (six, placed in `SERIES_OUTLINE.md`):** 🟢 Matrix Rain (Vol I Ch 13 —
  Pycasso's debut) · 🚀 Rocket Launch (Vol II Ch 1) · 🌙 Moon Landing (Vol II Ch 11) ·
  ✨ Starfield (Vol III Ch 11) · 🌍 Rotating Sphere (Vol IV Ch 4) · 🍩 **Spinning Donut**
  (Vol IV Ch 8 — the Gallery **capstone**, and the Guild's own emblem).
- **Skill-gated placement**, not a fixed level system: each showpiece lists the real skills it
  needs (loops → coordinates/trig → 3D projection/z-buffer) and lands where a Builder can
  actually reach it — the same honesty principle as the Dojo's tiers.
- **Run it → Hack it → Own it applies here too** (D-34's rule): every showpiece ships with
  labelled "knobs" (colour, shape, speed, light angle) so a Builder changes and owns it, never
  just runs a copy.
- **The donut is not incidental.** *"`.md` doesn't mean Markdown — it means Mommy's Donuts,"*
  the file Dad joked he'd promised but never shipped. The Guild's law became: **never promise a
  donut you don't ship** — why donuts sit beside the pizzas throughout the book, and why the
  Gallery's capstone is a donut made **real**, spinning in 3D, at the exact chapter where
  Builders learn to ship for real (Git/GitHub, Vol IV Ch 8).
**Reason:** These are the *"whoa, I want to build THAT"* pieces — the Matrix rain, the spinning
donut — that make a Builder chase trigonometry and 3D math because the result is this cool, not
because a textbook said so (pure `PHILOSOPHY.md` osmosis, D-25). Placing them where their real
skills exist keeps the wonder honest instead of overwhelming. As an open-source project, this is
also the natural growth edge: contributors add showpieces the way they add Dojo missions.

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

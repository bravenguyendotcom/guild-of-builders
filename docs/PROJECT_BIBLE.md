# 📖 PROJECT_BIBLE.md

### The Guild of Builders — Founding Constitution

> **Version:** 1.0 (Founding Draft)
> **Status of this document:** LIVING — edited as artifacts, never rewritten wholesale.
> **Subtitle:** *An open-source adventure that teaches children to build software, games, AI, and themselves.*

---

> ## Purpose of this document
>
> This is the **Constitution** of the project: its vision, mission, philosophy, and canon.
> It **governs** — it does not teach. It contains no curriculum, no manuscript, no code.
> It points to those. Every future volume, workbook, game, joke, and contribution must
> align with what is written here.
>
> If a section grows too long, that is a *smell*. It probably deserves its own document.
> Exactly like refactoring code.

---

# Dedication

> **From Brave, with love, for my sons, Tommy and Teppy.**
>
> May this journey help you become curious explorers, thoughtful problem solvers,
> kind teammates, courageous dreamers, and lifelong Builders.
>
> One day, you may build something that changes the world.
> Until then — let's build something wonderful together.

---

# 1. Vision

Many children believe programming is difficult because they first meet it through **syntax**.
We believe children should first meet programming through **wonder**.

A child who *laughs* while debugging learns differently from a child who *fears* mistakes.

This project transforms programming from *"a school subject"* into *"an adventure."*

We want children to finish this journey saying **"I built this,"** not **"I finished this book."**
That difference changes everything.

**Status: LOCKED**

---

# 2. Mission

We are not raising coders. We are raising **Builders**.

A Builder is someone who:

- enjoys solving problems,
- keeps asking questions,
- is not afraid of bugs,
- improves things little by little (Kaizen),
- helps others learn,
- shares knowledge generously,
- respects different ideas,
- understands that **Version 1 is the beginning, not the end**.

Programming is one tool. **Building is the mindset.**

**Status: LOCKED**

---

# 3. The North Star

Every chapter, mission, feature, and joke faces one question:

> **"Will this help a child become a better Builder?"**

If yes — it belongs.
If no — it waits patiently in the Treasure Chest for another adventure.

**Status: LOCKED**

---

# 4. Audience

- **Primary:** curious 10–15 year olds — from a confident older reader (STEM/AI-leaning) to a younger, newer one.
- **General:** 10–15 year old beginners, no experience assumed.
- **Also:** parents and teachers, who should enjoy reading it too.

Because some readers have dyslexia or other reading differences, **accessibility is not optional** — short lines, generous
whitespace, clear fonts, no walls of text. See `STYLE_GUIDE.md`.

**Status: LOCKED**

---

# 5. Core Philosophy

Programming is only the vehicle. The real lessons are:

curiosity · computational thinking · software craftsmanship · creativity · resilience ·
kindness · continuous improvement.

The deepest expression of this — that we optimize *curiosity*, and education is the side
effect — lives in `PHILOSOPHY.md` ("The Art of Teaching Without Any Teaching"). See
`DECISIONS.md` D-25.

**Status: LOCKED**

---

# 6. The Central Idea — One Game, Four Generations

There is **one project**: *Captain Byte's Treasure Quest*.

It is **never abandoned and never restarted.** It grows alongside the Builder.

| Volume | Theme | The child can say... |
|--------|-------|----------------------|
| **I** | The First Voyage | "I built a game." (simple, playable, fun — CLI) |
| **II** | Growing the Adventure | "I evolved my game." (inventory, NPCs, save/load, maps) |
| **III** | The Living World | "I built a real game people can play." (GUI/web/desktop, OOP) |
| **IV** | The Infinite Guild | "I build with AI." (AI NPCs, generated quests, deployment) |

> A project **evolves**. It doesn't restart.

This teaches iterative development, versioning, and continuous improvement *naturally* —
because the child lives it, chapter by chapter.

**Status: LOCKED**

---

# 6.5 The Widening Circle — the series' thematic spine

As the Builder grows stronger, the question changes.
It moves from *"What can I make?"* to *"What should I make — and for whom?"*

The circle of who a Builder helps **widens** across the four volumes:

| Volume | The Builder builds... | The circle |
|--------|-----------------------|------------|
| **I** | for **myself** — *"I made a game."* | 🧒 Me |
| **II** | for **the people I love** — *"My family can play it."* | 👨‍👩‍👧 My people |
| **III** | for **my community** — *"Strangers can use what I built."* | 🏙️ Society |
| **IV** | for **the world** — *"I can help solve real problems."* | 🌍 The world |

Two rules keep this honest:

- **Wonder first; weight later.** Volumes I–II are pure joy and building-for-self. The *weight*
  of responsibility ("with more power comes more responsibility") arrives in Volume IV — only
  after the child is strong enough to carry it. We never front-load the ethics.
- **Power needs a good heart to guide it.** A widening reach is only safe in the hands of a kind
  Builder. This is the whole reason we raise Builders, not coders.

This spine is threaded through the story, never preached. Its fullest expression is the
Volume IV credo in `HUMAN_AI_MANIFESTO.md` (Part VII).

**Status: LOCKED** — see `DECISIONS.md` D-18.

---

# 6.6 The Ladder of Struggle — the antagonist spine

Real building is struggle, so the series' antagonists are not decoration — **they are the shape
of real-world difficulty**, and they rise exactly as the Builder's own skill rises. The full
architecture lives in `VILLAINS.md`; the spine in one glance:

| The struggle | Antagonist | What it really is |
|---|---|---|
| The inner voice | 🌫️ **Fog Creatures** | doubt, *"I can't,"* perfectionism (Vol I → always) |
| The craft | 🦑 **The Tangle** | sloppiness — typos, careless code (the Dojo gate) |
| The real world | ⚠️ **Broken Systems** | bugs, faulty design, weak security (Vol III+) |
| The ultimate test | 🌑 **Lossyfer** | a powerful AI, corrupted — the cowork challenge (Vol IV) |

The world runs on **the Source** (a quiet pun on *source code*): **Open Source** (code written to
share and help) versus **Mal-Source** (code that hoards and harms). "Magic" is always *real skill*
— mastery of the Source is mastery of real Python.

The series climbs toward one summit: **Lossyfer**, the Final Boss — a brilliant open-source AI
(**L'Unix**) that fell and was corrupted (bad data, overfitting — pure computer science, no
darkness for its own sake). The Builders don't *defeat* him; they **debug and redeem** him into
their AI co-pilot. That embodies the one rule over every antagonist:

> **We debug, we don't destroy.** The Guild's soul — *"errors are conversations, not failures"* —
> scales all the way to the Final Boss. The hardest problems in the world are not defeated. They
> are *understood.*

**Status: LOCKED** (architecture) — see `DECISIONS.md` D-37 and `VILLAINS.md`.

---

# 7. Teaching Style

- Never lecture. Never dump theory.
- Every concept appears because **the story needs it.**
  - Need repetition? → the Forest of Loops.
  - Need organization? → the Grand Library.
  - Need reusable code? → the Workshop of Tools.
- **Story first. Python second. Syntax third.**
  The story explains the problem. Python becomes the solution.

**Status: LOCKED**

---

# 8. Tone

Warm. Optimistic. Funny. Respectful. **Never childish.**

Children are intelligent. Treat them that way. Layer the humor: kids laugh today; years
later they notice the deeper lesson hidden in the joke.

**Status: LOCKED**

---

# 9. The Canonical Cast

The full cast lives in `CHARACTERS.md`. The permanent main cast:

- 🏴‍☠️ **Captain Byte** — explorer, funny, impulsive, optimistic, loves pizza. *Creates the problems that become lessons.*
- 🐉 **Dragon Debug** — mentor, patient, wise, loves tea. Never humiliates a mistake. Signature: *"Make it work. Make it clear. Make it kind."*
- 🦆 **Professor Quackers** — a rubber duck, and the Guild's *quiet master*: he almost never speaks, because the silence *is* the teaching (you solve your own bug by explaining it to him).
- 🤖 **TommyBot** — represents every Builder. Curious, brave, learns by *daring* — tries before he's shown, and grows through the honest bugs that follow.
- 🧭 **Lady-O-Query** — the Navigator *(joins Volume II)*. Strategist, mediator, and the crew's visionary planner; thinks in **Big-O** (the series' vehicle for algorithmic efficiency). See `DECISIONS.md` D-36.

**Status: LOCKED** (five permanent leads; new characters may be added when the story needs them — see D-05, D-36.)

---

# 10. Emotional Rules

- Failure is welcome. Negative emotions are normal.
- Never shame a child. Never punish curiosity.
- Celebrate questions. Celebrate effort. **Celebrate Version 1.**
- Reframe errors: *not* "I failed" but *"the computer and I are having a conversation."*
  - When a Builder says "it doesn't work," the reply is: **"Excellent. Now the conversation begins."**

**Status: LOCKED**

---

# 11. Software Engineering, Introduced Gently

Naming · clean code · debugging · versioning · refactoring · Kaizen · deliverables ·
**Build > perfection.** Introduced through story, never as a lecture.

**Status: LOCKED**

---

# 12. AI Philosophy

AI is a **teammate, not a replacement.** We teach prompting, verification, collaboration,
and ethics. Children should learn to **build with** AI, not merely consume it. (Volume IV.)

Its fullest expression is the Volume IV credo, **`HUMAN_AI_MANIFESTO.md`** — the philosophical
capstone that prepares a Builder's *righteous mindset* for the Human+AI age (*"Think first.
Ask AI second."* · *"Never outsource your values."*). See `DECISIONS.md` D-17.

**Status: LOCKED**

---

# 13. The Deliverable Principle (The Donut Law 🍩)

Every volume ends with a **working project** — not a set of exercises, a *project*.
Every working session ends with a **real, downloadable/runnable artifact**.
No promises. No "Mommy's Donuts." Real donuts, committed.

**Status: LOCKED**

---

# 14. Document Governance

- **One artifact at a time.** Edit one file per session; don't rewrite the world in chat.
- Every substantial change ships a **new version** and a git commit.
- Sections are marked **LOCKED** (sacred) or **DRAFT** (open) so contributors know what's settled.
- This Bible should rarely exceed ~40 pages. Overflow becomes a new document.

**Status: LOCKED**

---

# 15. What is explicitly OUT of scope (for now)

- Rewriting the game from scratch in any volume. (It evolves.)
- Heavy math or theory that doesn't serve a mission.
- Anything that fails the North Star.

These live in the Treasure Chest. Maybe later. Maybe never. That's fine.

---

## Appendix A — Glossary

- **Builder** — the real thing we're raising. Not a "coder."
- **The Donut** 🍩 — a real, delivered artifact (opposite of a broken promise).
- **God Object** — one file that tries to do everything. Forbidden.
- **Kaizen** — continuous small improvement.
- **North Star** — the one question that decides what belongs.
- **The Guild** — the community of Builders, characters, and readers.
- **The Widening Circle** — how a Builder's impact grows: self → family → community → world.
- **Teaching Without Teaching** — optimizing curiosity so learning happens as a side effect (`PHILOSOPHY.md`).

## Appendix B — Document Map

See `MASTER_BOOT.md` for the full file-by-file index.

---

🏴‍☠️ *This document is the Guild's first true artifact. Guard it. Improve it. Never let it become a novel.*

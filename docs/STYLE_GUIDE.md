# ✍️ STYLE_GUIDE.md

### How the Guild of Builders reads, sounds, and feels

> **Status:** LOCKED for principles, DRAFT for details. **v1.2** — §4 rewritten for D-26
> (missions are embedded in the manuscript, not a separate workbook). **v1.1** — added the
> 🏗️ In the Real World box and the professionalism ladder.
> If the Bible is *what* and *why*, this file is *how it reads*.

---

## 1. The voice

Warm. Optimistic. Funny. Respectful. **Never childish.**

- Write *to* an intelligent child, not *down* at one.
- Humor is layered: a joke that lands for a 10-year-old today should reveal a real
  engineering lesson when they reread it at 20.
- Encourage, never shame. Curiosity is always celebrated.

---

## 2. Accessibility (non-negotiable — Teppy has mild dyslexia)

- **Short lines. Short paragraphs.** Often one sentence per line in the manuscript.
- **Generous whitespace.** White space is a feature, not wasted paper.
- Prefer plain, concrete words over clever vocabulary.
- Break big ideas into small, sequential steps.
- Use clear visual anchors: emoji character-tags (🐉, 🏴‍☠️), badges, boxes.
- Never a wall of text. If a page feels dense, it's wrong.

Reference feel: **No Starch Press**, **DK**, **CS50**, **MIT Scratch** books.
Lots of whitespace, large fonts, illustrations, funny icons.

---

## 3. Story first, Python second

Every concept must be *motivated by the story* before any syntax appears.

> Bad: "Today we learn `if` statements."
> Good: "The cave has three tunnels. Captain Byte can only take one. How does a program
> choose?" → *then* `if`.

---

## 4. The mission — embedded in the chapter (see `DECISIONS.md` D-26)

**There is no separate workbook.** The mission the child *does* lives **inside the story
chapter** — one flowing read, not a story followed by a worksheet. (This is kinder for Teppy,
roughly halves the authoring work, and matches how the shipped chapters 0–7 are already
written. The old standalone 12-part worksheet template is deprecated.)

A chapter carries the mission through its natural arc, not a form to fill in:

1. **Story** — Captain Byte hits a problem the reader feels. (Story first.)
2. **The task** — what to build, revealed *by* the story, not announced as "Mission 3."
3. **The honest bug** — a real error the reader would actually hit, framed as a conversation
   (*"Excellent. Now the conversation begins."*), then fixed.
4. **The two boxes that survived from the old workbook** (use when they fit):
   - 🧪 **Testing Table** — `Input | Expected | Actual`. A professional habit, taught early
     and gently — Builders check their work.
   - 🐛 **Debug Log** — *"My bug / What caused it? / How did I fix it?"* Turns a frustrating
     moment into a small, proud record.
5. **Achievement Unlocked** — the badge earned (see §6).
6. **Cliffhanger** — pulls the reader into the next chapter.

**Bonus challenges (⭐)** are welcome inline as an optional "want more?" — never required.

> **Two other tracks, kept separate (don't confuse them with the chapter mission):**
> - **Pure typing practice** → the **Typing Dojo** (`typing_dojo/`), its own one-screen
>   format with *no* worksheet fields (D-22).
> - **Optional extra adventures** → **`docs/SIDE_QUESTS.md`** (always optional, never gating).

---

## 5. Recurring boxes (use with intention)

- **Toolbox Card** — a reusable programmer mindset (e.g. *"Ask what the computer is telling
  you, not why you're bad at this."*).
- **Dragon Debug's Wisdom** — a single memorable line.
- **Dad's Story** — a true anecdote from Brave.
- **🧪 Testing Table** — `Input | Expected | Actual`, when a mission benefits from checking (see §4).
- **🐛 Debug Log** — my bug / cause / fix, when a chapter has a bug worth recording (see §4).
- **Achievement Unlocked ⭐** — badge earned at the end of a mission.
- **Cliffhanger** — a "To be continued..." that pulls the reader to the next chapter.
- **🏗️ In the Real World** — the bridge to professional life. See section 5a; it has
  its own rules because it's the easiest box to get wrong.

### 5a. The "In the Real World" box 🏗️

**Its job:** connect what just happened in the story to real software-engineering life —
so the child learns that their adventure skills have grown-up names, and real Builders
use them every day. This is how wonder gradually becomes professionalism.

> 🏗️ **In the Real World**
> Grown-up Builders show each other their code before shipping it.
> It's called a **code review**.
> Nobody's code is perfect on the first try. Not even the seniors'.

**The rules (strict, to protect the flow):**

1. **After the story, never inside it.** The narrative is sacred. The box is a window
   the child may look through — not a wall in the middle of the road.
2. **Max 3–4 short lines.** If it needs more, it's a lecture wearing a disguise. Cut it.
3. **Real vocabulary in bold** — one or two terms max (**bug**, **version**, **code
   review**, **spec**, **standup**, **deadline**, **QA**). The child collects the words
   of the trade like treasure.
4. **Always warm, never scary.** The real world is presented as a place where the child
   already belongs: *"You just did what professionals do."*
5. **Optional by design.** A tired reader (or Teppy on a heavy day) can skip every box
   and lose no story. A curious reader collects them all.
6. **True things only.** No fairy tales about the industry. Real Builders have bugs,
   reviews, deadlines, and teammates. That's the point.

**The professionalism ladder (how the box grows across volumes):**

| Volume | The box teaches... | The child becomes... |
|--------|--------------------|--------------------------|
| **I** | Vocabulary — "this thing has a name" (bug, version, test, review) | someone who *recognizes* the trade |
| **II** | Rituals — mini standups with Dad, a tiny spec before coding | someone who *practices* the trade |
| **III** | Artifacts — READMEs for strangers, demos to the family | someone who *presents* with confidence |
| **IV** | The room — proposing solutions to real problems, real collaboration | someone who *belongs* in the room |

By Volume IV, talking to a real engineer or proposing a software solution isn't a leap.
It's just the next rung of a ladder the child has been climbing since Chapter 1.

---

## 6. Achievements & badges (canon)

Rookie Python 🐍 · Bug Hunter 🪲 · Algorithm Master ⚙️ · CLI Builder 💻 · Python Adventurer 🏅
(+ printable certificates at the end of each volume.)

---

## 7. Formatting conventions

- Markdown is the **source of truth**. PDF / DOCX / HTML / web are *generated* from it.
- Character tags use the canonical emoji from `CHARACTERS.md`.
- Code blocks are always real, runnable Python (test before shipping).
- File and version names are explicit: `Treasure_Quest_v1`, not "the game".

---

## 8. What to avoid

- Lecturing. Theory dumps. Vocabulary showing-off.
- Walls of text (fails accessibility).
- Sarcasm aimed at the child. (Aim it lovingly at bugs and keyboards instead.)
- Adding features/characters that fail the North Star.
- A separate worksheet after the story — the mission lives *in* the chapter now (D-26).

---

🐉 *Make it work. Make it clear. Make it kind. — this applies to the writing too.*

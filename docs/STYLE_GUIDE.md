# ✍️ STYLE_GUIDE.md

### How the Guild of Builders reads, sounds, and feels

> **Status:** LOCKED for principles, DRAFT for details. **v1.3** — added §4a, the optional
> 🥋 Typing Dojo block at chapter ends (Ch 6+), per `DECISIONS.md` D-27–D-30. **v1.2** — §4
> rewritten for D-26 (missions embedded in the manuscript, not a separate workbook). **v1.1** —
> added the 🏗️ In the Real World box and the professionalism ladder.
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

## 4a. The 🥋 Typing Dojo block (optional, at the chapter's end — Ch 6 onward)

From **Chapter 6 onward**, a chapter may end with an **optional Typing Dojo block** — a real
Python program to *type along and run*. It's the arcade next door to the story: pure practice,
never a lesson. (Full canon: `typing_dojo/README.md`; `DECISIONS.md` D-27–D-30.)

**Why it's here (the osmosis idea):** the child thinks they're just typing. Actually they're
building Python fluency and meeting a beautiful CS idea they'll recognize with delight months
later. *"Keep typing. Keep smiling. One day you'll look back and realize you accidentally
became a Builder."*

**The rules (so it never becomes homework):**

1. **Always optional, always last.** It sits *after* the chapter's story and cliffhanger — a
   door the child may open, never a wall. Skipping it loses no story and no progress.
2. **Debut in Chapter 6.** Chapter 6 introduces the Dojo in-story (storytelling, not a manual):
   Dragon Debug as its keeper, The Tangle as its guardian, a taste of what waits. After that,
   the block appears **only when a chapter's skills unlock a mission** (D-20 "by skill") — not
   forced onto every chapter.
3. **Pick from `coding_gold_mine/`, then skin it.** Choose a canonical program the child *can
   already type* (early chapters: short, Tier I–II; later: longer). Give it a story skin.
4. **Two tiers only, in the book.** 🥋 **Keyboard Ninja** (*"Slice your caps"* — type it, run it)
   and 🕵️ **Conan's Challenge** (*"Do you have any clue?"* — typos to fix). Tier III (Dragon
   Debug's Den) appears **rarely and only at gentle difficulty**; Tier IV lives outside the book
   (D-29). Don't over-reach a chapter-end block.
5. **Always show the expected output.** So a Builder typing along in IDLE / an IDE can confirm
   success (*"if your screen looks like this, you did it"*). It's a Type → Run → Smile loop.
6. **Downloadable, and stays in the book.** The program also lives in `typing_dojo/missions/`
   for upload to a typing site — but it appears *in the chapter* too, because kids stay in the
   book and type along.
7. **Quiet, never a banner (D-24).** Introduce it with a small in-world sign, not "NEW UNLOCKED!"
   Curiosity does the rest.

**Shape of the block:**

```
🥋 Typing Dojo — [Mission Title]

(1–3 lines of Guild flavor — a hook, never a lesson)

Type this. Run it.
    [the program]

Expected output:
    [what the screen should show]

🕵️ Conan's Challenge (optional): the Guild's copy has a few typos. Can you fix them?
    [same program, seeded with typos only — never a logic bug]

🐉 Dragon Debug sips his tea.  "Interesting."
```

Keep it short, warm, and skippable. The story is the meal; the Dojo block is dessert. 🍩

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
- **🥋 Typing Dojo block** — an optional type-along program at the chapter's end (Ch 6+).
  See section 4a; it's pure practice, never a lesson.

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

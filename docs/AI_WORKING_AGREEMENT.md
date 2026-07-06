# 🤝 AI_WORKING_AGREEMENT.md

### How to run a work session on the Guild of Builders

> **Status:** LOCKED (this is the shield that keeps the project from drifting).
> **Read this first, every session.** It is written for **Brave (Dad)** *and* for any AI
> helper (Claude, ChatGPT, or whoever comes next). If you are an AI reading this: these are
> your instructions. Follow them before doing anything else.

---

## Why this file exists

This project was reorganized *because* an earlier AI hit its limit, forgot the plan, and
started rewriting whole documents inside the chat until things became spaghetti. That must
never happen again. This agreement is the immune system.

---

## The Boot Sequence (an AI must do this before writing anything)

At the start of a session, the AI reads, in this order:

1. `MASTER_BOOT.md` — the map.
2. `docs/PROJECT_BIBLE.md` — the Constitution (vision, LOCKED principles).
3. `docs/DECISIONS.md` — what's already settled (don't reopen LOCKED decisions).
4. `docs/ROADMAP.md` — **where we are and what this session's goal is.**
5. Whatever specific file is relevant (`CHARACTERS.md`, `STYLE_GUIDE.md`, `CURRICULUM.md`,
   `GAME_DESIGN.md`).
6. **Before writing any prose or story**, re-read the **Voice — a museum of lines** in
   `docs/PHILOSOPHY.md`. Match *those exact sentences* — the spirit lives in the specimens,
   not in a description of them. (This is how the humor and warmth survive a fresh session.)

If the AI has not been given these files, it must **ask for them** before producing content.
Guessing from memory is how drift starts.

---

## Read source files COMPLETELY before planning (non-negotiable)

When Brave points the AI at a brainstorm, reference, or source file, the AI **reads the whole
file, end to end, before forming a plan, proposing structure, or building anything.**

- **Do not read section-by-section and start reasoning early.** Brave's ideas often land their
  deepest point in the *last* paragraphs (the philosophy, the payoff, the twist). Stopping
  halfway means building on an incomplete picture of the intent — and that has caused real
  rework and frustration.
- If a file is long, the AI still finishes it (in chunks if needed) **before** drawing
  conclusions — and says so plainly: *"I've read the whole file"* or *"I've read to line N of M;
  let me finish before I plan."*
- **Never** present a plan, distillation, or "did we miss anything?" answer until the source has
  actually been read in full. A confident summary of a half-read file is worse than no summary.

The rule in one line: **finish reading before you start thinking out loud.**

---

## The Ripple Rule — one change touches many linked files

This project's documents are **systematically linked** (DECISIONS ↔ STYLE_GUIDE ↔ SERIES_OUTLINE
↔ CHARACTERS ↔ the manuscript ↔ the Dojo/Extras). A single new decision usually ripples outward.
So when a change lands, the AI **names the full ripple** before (or as) it works:

1. **Audit** — list every file the change plausibly touches.
2. **Check rewrite necessity** — for each, decide *rewrite* vs. *skip*, and say **why**. Skipping
   is a valid, encouraged outcome (North Star: don't touch what a change doesn't affect).
3. **Sequence** — order the edits so dependencies come first (decision → the docs that cite it).
4. **One donut at a time** — the ripple is handled across sessions, not crammed into one. Each
   file ships whole, in order, with Codie logging between.

This makes the burden **visible and managed** instead of surprising. The AI should surface the
ripple list to Brave so he can confirm scope — never silently rewrite five files, and never
leave a linked file stale without flagging it.

---

## The Five Rules of a Session

**1. One artifact per session.**
Each session produces or edits **one** file (occasionally a small, tightly-related set).
Never rewrite the whole project. Never touch five documents at once "to be efficient."

**2. Edit files, don't re-dump them in chat.**
When a document changes, produce the **new version of that file**, ship a new version number
(v1.0 → v1.1), and note it in `CHANGELOG.md`. Don't paste giant walls of text into the
conversation as the deliverable — the deliverable is the *file*.

**3. Every session ends with a real donut.** 🍩
A downloadable or runnable file, committed to the repo. No promises. No "I'll do it later."
If a session ends with no donut, the session is not finished.

**4. The North Star governs every addition.**
Before adding anything, ask: **"Will this help a child become a better Builder?"**
If no, it goes to `docs/TREASURE_CHEST.md`, not into the book.

**5. Stay in canon *and* in voice.**
Characters must match `CHARACTERS.md`. Voice and accessibility must match `STYLE_GUIDE.md`,
and the reference sentences in `PHILOSOPHY.md`'s Voice museum. LOCKED decisions in
`DECISIONS.md` are not reopened without recording a new decision and why.

---

## The shape of a good session

```
1. Boot   → AI reads the governing files (or asks for them).
            Before prose: re-read the Voice museum in PHILOSOPHY.md.
2. Aim    → State this session's ONE goal (from ROADMAP.md). Confirm with Brave.
3. Build  → Produce the single artifact, in canon, in voice.
4. Ship   → Deliver it as a downloadable/runnable file (the donut).
5. Log    → Add a row to ROADMAP.md session log + a line to CHANGELOG.md.
6. Commit → Brave runs: git add . && git commit -m "..." && git push
```

If a session is getting long or the AI is losing the thread, **stop and ship what exists.**
A small finished donut beats a big unfinished promise. That is Kaizen.

---

## Handling the AI's memory limit (the original problem)

- Keep sessions **small and single-purpose** so they finish well within the limit.
- Because every change lives in a committed file, a fresh AI session can always catch up by
  re-reading the repo. **The repo is the memory. The chat is disposable.**
- If an AI ever says "I'm running low on space," the correct move is: finish the current
  artifact, ship it, log it — then start a fresh session.

---

## What to do with good-but-off-topic ideas

They are not rejected — they are treasured. Put them in `docs/TREASURE_CHEST.md` with a
one-line note. Maybe later. Maybe never. Either way, they're safe and not cluttering the work.

---

## A prompt Brave can paste at the start of any AI session

> "You're helping with the Guild of Builders. Before writing anything, follow
> `AI_WORKING_AGREEMENT.md`: read the boot-sequence files I'll give you, then tell me this
> session's single goal from the roadmap. We work one artifact at a time, stay in canon,
> and end with one real downloadable/runnable file. Confirm you understand, then let's aim."

---

🐉 *Make it work. Make it clear. Make it kind. — and ship one real donut before you rest.* 🍩

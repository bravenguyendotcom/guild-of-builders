# 🛠️ GUILD_EXTRAS_BUILD_KIT.md

### How to build the Guild Extras library — the handoff for a dedicated writing session

> **Status:** BUILD KIT (a how-to + paste-ready prompt). Not the extras themselves.
> **Purpose:** let a focused writing session (Sonnet-class is ideal) compose all the Guild
> Extras (D-34) **from the distilled catalog** — never re-reading the 1,485-line raw brainstorm.
> **The golden rule:** compose each extra *fresh, in our voice and cast* (D-19/D-34). The catalog
> gives the gag/mechanic + the re-skin; the writer writes it clean. Never paste the source.

---

## What model, and why

- **Jokes & riddles:** Sonnet-class is perfect — warm, punchy, voice-driven writing.
- **Code Art (CLI):** Sonnet-class is fine **only if the prompt enforces bash-testing** every
  art snippet and pasting the *real* output. ASCII art must actually render aligned — that's a
  correctness step, not a vibe. (See Quality Bar below.)
- **Not Opus:** this is composition from a clear spec, not canon reconciliation. Save Opus for
  chapter/canon work.

---

## Files to upload / have synced into the writing session

1. `docs/GUILD_EXTRAS_SOURCE.md` — **the distilled catalog** (read THIS, not the raw brainstorm).
2. `docs/DECISIONS.md` — D-34 (extras), D-05 (cast), D-19 (original-only), D-23/D-25 (repetition/osmosis).
3. `docs/CHARACTERS.md` — the cast to re-skin *to* (voices + running jokes).
4. `docs/STYLE_GUIDE.md` — voice + accessibility (short lines, whitespace, Teppy).
5. `docs/PHILOSOPHY.md` — the **Voice museum** (match those exact sentences; don't paraphrase).
6. `docs/SERIES_OUTLINE.md` — so each extra can be matched to its chapter's topic.

**Do NOT upload** the raw `riddles_and_jokes_brainstorming.md` — the whole point is to not read it
again. Everything needed is distilled in `GUILD_EXTRAS_SOURCE.md`.

---

## The rotation & distribution rules (from D-34)

- **One extra per chapter, from Chapter 1.** Rotation: **😄 Joke → 🧩 Riddle → 🎨 Art → (repeat).**
  So Ch1 Joke, Ch2 Riddle, Ch3 Art, Ch4 Joke, …
- **Match to the chapter's topic where possible** (a modulo joke near the modulo chapter, a
  strings riddle near the strings chapter) — distribute *mindfully*, using the catalog's topic tags.
- **Separate from the Dojo.** From Ch 6+, a chapter has BOTH a 🥋 Dojo block (side-quest) AND its
  rotating Extra. They never substitute for each other.
- **Advanced 3D/motion art is NOT in this rotation** — that's `PYCASSO_GALLERY_ADVANCED.md`
  (skill-gated, later volumes). Don't pull those into early chapters.

---

## Re-skinning (mandatory — D-19/D-05)

Use the **re-skinning key** at the top of `GUILD_EXTRAS_SOURCE.md`. In short: every foreign
character (snake-Monty, Glitch, Dunder, Pip, Cal, Dr. Byte-Size) is **dropped or re-skinned to
our cast** (Captain Byte, Dragon Debug, Quackers, TommyBot, Pycasso, Maestro Monty & Sir
Quizzalot, Sir Boolean, Ninja Cat, The Tangle). Public-domain programmer jokes are fine —
**rewritten in our voice**, never pasted. Pycasso's saying: *"Every child is an artist, every
terminal is a canvas."*

---

## The quality bar (every extra must pass)

**All extras:**
- In our voice (check the Voice museum) and warm — funny *with* the reader, never at them.
- Accessible: short lines, whitespace, plain words (Teppy).
- Uses only skills the child has by that chapter (skill-gated, like the Dojo).
- One screen. No lecture. Wonder first.

**Riddles (interactive) & Art (code) — additionally:**
- **Bash-run the code before writing it up.** Paste the **real** output as "Expected output."
- Runnable in IDLE / a plain terminal, standard library only (no installs).
- **Art = Run it → Hack it → Own it:** ship a small engine with clearly labelled "knobs"
  (variables the child changes) + one line inviting them to make it theirs. Never copy-to-mimic.

---

## Output format (what the writer produces)

For each extra, write a small block ready to drop into a chapter's Extra slot:

```
[emoji] Guild Extra — [Title]        (Joke / Riddle / Art)

(the joke, OR the riddle's runnable code, OR the art engine)

Expected output:        (riddles & art only — the REAL bashed output)
    ...

🎨 Hack it: (art only — 1 line: "change MY_PAINT to your own symbol and run it again")
```

Keep it short. The chapter's story is the meal; the Extra is a bite of dessert.

---

## Batch plan (don't build all 50 at once)

- **Batch 1 — Volume I (Ch 1–15):** ~15 extras, following the rotation. Ship these first; they
  cover the chapters actually being written now.
- **Batch 2+ — later volumes:** as those chapters approach. The catalog has 55 items — plenty.
- **One file per batch** (e.g. `docs/GUILD_EXTRAS.md`, grown over time), or per-volume files —
  writer's choice, but keep it ONE artifact per session.
- Build the format on the **first 3** (one joke, one riddle, one art), get them right, then the
  rest go fast and consistent.

---

## Paste-ready prompt for the writing session

```
You're writing the Guild Extras for "The Guild of Builders" — short joke/riddle/code-art beats,
one per chapter (rotation: Joke → Riddle → Art, from Chapter 1).

Before writing: read GUILD_EXTRAS_SOURCE.md (the distilled catalog — your ONLY source; do not
ask for the raw brainstorm), plus PHILOSOPHY.md's Voice museum, CHARACTERS.md, and STYLE_GUIDE.md.
Match our voice exactly; don't paraphrase the museum lines.

Rules:
- Re-skin every character to OUR cast (see the key in GUILD_EXTRAS_SOURCE.md). Never import
  foreign names. Public-domain jokes are fine, rewritten in our voice. (D-19/D-34)
- One extra per chapter, matched to that chapter's topic where possible (use the catalog's tags
  and SERIES_OUTLINE.md).
- Accessibility: short lines, whitespace, plain words (Teppy). One screen. Wonder first, never a lecture.
- For riddles and art: the code must actually run. Bash-test it, then paste the REAL output as
  "Expected output." Art follows Run it → Hack it → Own it (a small engine with knobs the child
  changes). Standard library only, runs in IDLE.

This session: build Batch 1 — Volume I (Chapters 1–15), following the rotation. Produce ONE file.
Start with the first three (a joke, a riddle, an art) to lock the format, then continue.
```

---

🛠️ *Distill once, write many. The catalog is the pantry; this kit is the recipe; the writer cooks
in our voice.* 🐉🍩

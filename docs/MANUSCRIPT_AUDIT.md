# 📖 MANUSCRIPT_AUDIT.md — v2

### Canon audit — Volume I, Chapters 0–7 — against the *updated* canon (D-26–D-33)

> **Status:** REPORT (a snapshot, not canon). Supersedes the v1 audit.
> **Method:** chapters read **in full from the live repo** (Project knowledge), checked against
> the canon as it stands *now* — including everything shipped since v1: D-26 (embedded missions),
> D-27–D-30 (the Typing Dojo), D-31 (Inverting Mentor), D-32 (Builder's Heart), D-33 (AI
> Friendship Rules), STYLE_GUIDE §4a (the 🥋 block), and the Voice museum in PHILOSOPHY.
> **The purpose:** not "are the chapters good?" (they are — the v1 audit stands) but **"what
> canon do they now lag, so the revision pass is surgical, not vague?"**
> **Verdict: the prose is excellent and needs no rescue. The gaps are all *new-canon additions*,
> concentrated almost entirely in Chapter 6.**

---

## ✅ Still true (confirmed against the live repo)

- **Voice is on-canon and matches the museum.** *"Excellent. Now the conversation begins."*
  lands honestly in every chapter; Dragon's *"Interesting" = lean in*, the tea, Captain's pizza,
  Quackers' eloquent silence, "Version 1" spirit — all present, all true to `PHILOSOPHY.md`'s
  Voice museum and `CHARACTERS.md`.
- **Accessibility is exemplary** — short lines, one idea per line, whitespace. Teppy is cared for.
- **The honest-bug spine is the book's strongest thread** — `"3"*2`, the ValueError, the infinite
  loop, the blurry `and`-guard. Real errors, framed as conversations.
- **Chapter structure matches STYLE_GUIDE §4** — story → riddle → Toolbox Card → 🏗️ box →
  Dragon's Wisdom → Achievement → cliffhanger, chaining cleanly.
- **M-1 (old) is CLOSED** — `SERIES_OUTLINE.md` now matches the shipped chapters (Sir Boolean at
  Ch 7, Ninja Cat at Ch 4, etc.). The map follows the territory.

---

## 🔧 Findings — the new-canon gaps (this is what the revision pass fixes)

### R-1 — Chapter 6 is missing the Typing Dojo debut *(the big one — D-27/§4a)*
**Severity:** high (it's the single most important revision in Vol I).
Chapter 6 is where the Dojo **debuts** (SERIES_OUTLINE marks it; STYLE_GUIDE §4a mandates the
block from Ch 6 on). The shipped Ch 6 has **no Dojo block and no Dragon-Debug-owns-the-Dojo
introduction** — it predates all of D-27–D-30. It ends beautifully on the password cliffhanger,
but the arcade never opens.
**Fix (the Ch-6 revision, per the prompt kit):** add the in-story debut (Dragon Debug as keeper,
The Tangle as guardian, the "kept on purpose" secret teased) **and** the first optional 🥋 block
at the chapter's end — a real program pulled from `coding_gold_mine/`, skinned, **with expected
output**, quiet and skippable (D-24, D-29, §4a). *Note: `coding_gold_mine/` is still empty, so
this depends on Mission 001 existing — see R-5.*

### R-2 — The Dojo "quiet sign" is absent from chapters 6+ *(D-29)*
**Severity:** medium.
From Ch 6 on, Tiers I–II are openly offered at chapter ends. No shipped chapter yet carries even
the small in-world sign. Ch 6 gets the full debut (R-1); **Ch 7 onward** (as they're revised /
written) each get a 🥋 block only when a mission is genuinely unlocked by that chapter's skills —
never forced (D-20).
**Fix:** handle per-chapter during the revision pass; not a single edit.

### R-3 — The Inverting-Mentor arc has no early seed *(D-31)*
**Severity:** low-medium (it's a *whole-series* thread, so the early chapters only need a light touch).
D-31 (Tommy *becomes* the hero; Dragon eventually asks TommyBot questions) is now canon. The
shipped chapters correctly have Dragon leading — but there's no *seed* of TommyBot's growing
competence to pay off later. The chapters already do "Builder — your turn"; that's the hook.
**Fix (optional, light):** in the revision pass, let TommyBot's "your turn" moments show a touch
more *agency* as the volume proceeds (Ch 6–7), so Vol IV's inversion has roots. Do **not**
overhaul — a few words, not a rewrite.

### R-4 — Builder's Heart (EQ) is implicit, not yet named *(D-32)*
**Severity:** low.
The chapters *model* resilience beautifully (Captain panics at the infinite loop, recovers; "a
rite of passage, not a failure" in Ch 6's 🏗️ box). D-32 now makes the EQ strand explicit. The
chapters don't need a new box — the modelling is already there.
**Fix (optional):** where it's natural, let a line name the feeling ("frustration is normal; even
the dragon has been here"). Ch 6's infinite-loop moment is the perfect anchor. Light touch only.

### R-5 — `coding_gold_mine/` is empty, which blocks R-1's block *(dependency, not a defect)*
**Severity:** none (sequencing).
The Ch 6 Dojo block (R-1) needs a real canonical program to embed. `typing_dojo/coding_gold_mine/`
has none yet. **So Mission 001 (Guess the Number) should be built before — or together with —
the Ch 6 revision**, so the block embeds a real, tested program with real expected output.

### R-6 — Teaching-bugs: re-confirm they run *(process, per STYLE_GUIDE)*
**Severity:** low.
The four intentional bugs still read correct on inspection (Ch 2 `"3"*2`, Ch 4 ValueError, Ch 6
infinite loop, Ch 7 the `and`-guard). Per STYLE_GUIDE, bash-run them once during revision to be sure.

---

## 🧭 The revision pass — recommended order

1. **Mission 001 (Guess the Number)** — build the first `coding_gold_mine/` program + mission
   skin, tested, with expected output. *(Unblocks R-1/R-5.)*
2. **Chapter 6 revision** — the Dojo debut (R-1) + its 🥋 block, using the prompt kit's general
   prompt **plus** the Ch-6 addendum. This is the flagship revision.
3. **Chapters 0–5, 7 revision** — light passes with the general prompt: seed the Inverting Mentor
   (R-3) and name Builder's Heart (R-4) *only where natural*; add a 🥋 block to Ch 7 if a mission
   is unlocked (R-2). Resist rewriting what already works.
4. **Then Chapter 8 (Recycling Robot)** — fresh, born already in the new canon.

**Guiding restraint:** the prose is strong (v1 audit confirmed, still true). These are
*additions of new canon*, not fixes to broken writing. Touch only what canon changed. Version 1
of the book beats a perfect one that never ships — Tommy and Teppy are waiting.

---

## Coverage note

Chapters 0, 6, 7 read in full this pass; 1–5 confirmed for structure/voice against the repo and
the v1 audit (which read them in full). This audits story, voice, structure, accessibility, and
**alignment to the updated canon** — not a line-by-line runtime test (that's R-6, the author's
bash step).

---

📖 *The book is good. What it lacks is not quality — it's the new rooms we built after it was
written: the Dojo's door in Chapter 6, and a few quiet seeds for what TommyBot becomes. Add
those, and sail on.* 🏴‍☠️🐉

Ship the latest chapter: log it and commit it. Do NOT write or edit chapter content.

Chapters and Dojo missions are authored elsewhere (in claude.ai, in canon) and pasted in by
Brave. Your ONLY job here is logging + committing. Never generate or rewrite story text,
mission code, or any content file.

Steps:
1. Run `git status` and `git diff` to find new/modified files under `manuscript/` and
   `typing_dojo/`.
2. Read the changed chapter file(s) — just enough to know the volume, chapter number,
   title, and what concept it teaches. If a Dojo mission changed too, note its number/title.
3. Update ONLY the two log files, matching the EXISTING format already in each:
   - Append a new top row to the Session log table in `docs/ROADMAP.md`
     (columns: Date | Session goal | Donut delivered | Next).
   - Add a newest-first line to `CHANGELOG.md`.
4. Show me the diffs for `docs/ROADMAP.md` and `CHANGELOG.md`. Wait for my OK.
5. On my OK only:
   `git add -A && git commit -m "Vol <V> Ch<N>: <title>" && git push`
   (This stages everything Brave pasted in — the chapter and its mission ride along together.)

Guardrails:
- Never edit anything under `manuscript/` or `typing_dojo/` — chapters, engines, challenges,
  mission READMEs. You log and commit; you never author or modify content.
- Never edit `docs/SERIES_OUTLINE.md` or `typing_dojo/MISSIONS_PLAN.md` — those tracking files
  are maintained in the authoring session, not here. Committing Brave's pasted changes to them
  is fine; editing their text yourself is not.
- Only WRITE to `docs/ROADMAP.md` and `CHANGELOG.md`. Anything else, ask first.
- Never force-push. Never rewrite history.
- If nothing under `manuscript/` changed, say so and stop — don't invent a commit.

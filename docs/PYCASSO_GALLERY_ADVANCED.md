# 🎨 PYCASSO_GALLERY_ADVANCED.md

### The Advanced Gallery — 3D & motion CLI art (the "whoa, I want to build THAT" tier)

> **Status:** LIVE (canon per `DECISIONS.md` D-35). The showpiece **code lives in the
> `pycasso_gallery/` folder** (the art-twin of `typing_dojo/coding_gold_mine/`). Seed topics: 6.
> **Built so far:** 🟢 Matrix Rain (`pycasso_gallery/matrix_rain.py`) — shown-and-runnable at Vol I
> Ch 13 · 🚀 Rocket Launch (`pycasso_gallery/rocket_launch.py`) — shown-and-runnable at Vol II Ch 1.
> Both real and bash-verified. The other four are planned topics, built as their chapters arrive.
> **What this is:** the *advanced* wing of Professor Pycasso's Gallery — aspirational, animated,
> math-and-loops-heavy CLI art. These are **not** the per-chapter Guild Extras (D-34). They are
> a **skill-gated advanced tier**, exactly parallel to the Typing Dojo's higher tiers (D-28):
> curious Builders reach for them in the later volumes or in the open-source gallery, not on
> page one.
> **Why they matter:** these are the pieces that make a kid whisper *"whoa — I want to make
> THAT."* (Think the Matrix rain.) That spark — *"I'll learn the math because the result is
> this cool"* — is pure North Star: curiosity pulling a Builder toward trigonometry, loops, and
> 3D projection they'd never chase from a textbook. *"Every child is an artist, every terminal
> is a canvas."* — Professor Pycasso.

---

## How these are placed (the rule)

Advanced art is **skill-gated**, like advanced Dojo missions (D-20/D-28). Each showpiece lists
the real skills it needs, so it lands where a Builder can actually reach it:

- **Vol I skills** (print, loops, strings, `time.sleep`, basic math) → a *simplified* version can
  appear as a late-Vol-I / Vol-II Gallery extra.
- **Vol II–III skills** (nested loops, 2D grids, trig `sin`/`cos`, coordinates) → the real thing.
- **Vol III–IV skills** (3D projection, z-buffers, vectors) → the full showpieces + the OS gallery.

All of them share one honest technique, so a Builder who learns it once can build the rest:
**clear the screen → compute each character from math for this frame → print → `sleep` → repeat.**
(The screen-clear is an ANSI escape; the math is what changes.)

---

## The 6 showpieces

### 1. 🟢 The Matrix Rain — *"the green code waterfall"*
- **What:** endless columns of green characters falling down the terminal, trails fading behind
  them. The iconic "hacker screen."
- **Why it fits us:** the ultimate *"I want to build that"* hook — and secretly it's just lists,
  random, and per-column counters. A perfect bridge from "loops are boring" to "loops make magic."
- **Real technique:** one falling position per column (a list), advance each per frame, print a
  random char at the head, dimmer chars for the trail, `time.sleep` between frames.
- **Skills:** lists, `random`, loops, `time`, ANSI colour codes. **Level: Medium** (Vol II).
- **Placement:** **Built** → `pycasso_gallery/matrix_rain.py` (adaptive width, `CHARS`/`COLOR`
  knobs). **Shown-and-runnable at Vol I Ch 13** (Pycasso's debut): the child runs a short version
  right in the chapter and watches it fall, even though the full four-idea build (a list that
  holds a *position*) isn't taught until Vol II. So it's not "shown, not built" — it's *shown,
  runnable, and gleefully unfinished*, with Pycasso handing the tweaks to the Builder.
- **Chapter fit:** Ch 13 (debut — inspire now, understand fully by Vol II); pairs with any later
  chapter about **lists + randomness**.

### 2. ✨ The Starfield — *"flying through space"*
- **What:** white dots streaming outward from the centre, faster as they near the edges — the
  sensation of flying forward through stars.
- **Why it fits us:** the first taste of **perspective / 3D projection** (near things move faster),
  but achievable with simple division. The "aha, that's how games fake depth" moment.
- **Real technique:** each star has an (x, y, z); each frame decrease z (fly toward it), project
  to screen as `x/z, y/z`, respawn when it passes the viewer.
- **Skills:** coordinates, division-as-projection, loops, respawn logic. **Level: Medium–Hard** (Vol III).
- **Placement:** Vol III Gallery (near the OOP/coordinates work).
- **Chapter fit:** a chapter introducing **coordinates or simple projection** (Treasure Quest's
  first move toward a visual world).

### 3. 🌍 The Rotating Sphere / Globe — *"a spinning planet in text"*
- **What:** a shaded sphere (or wireframe globe) rotating in place, lit from one side.
- **Why it fits us:** the gateway to real 3D — surface points, a light source, shading by
  brightness. Less code than the donut, same ideas.
- **Real technique:** sample points on a sphere with two angles, rotate, project to 2D, shade by
  the dot product with a light direction, z-buffer so the near side hides the far side.
- **Skills:** `sin`/`cos`, nested loops, 3D→2D projection, z-buffer, brightness→character mapping.
  **Level: Hard** (Vol III–IV).
- **Placement:** Vol III–IV Gallery.
- **Chapter fit:** a chapter about **the game world becoming visual / 3D** (Vol III).

### 4. 🍩 The Spinning Donut — *the legendary showpiece (and OUR symbol)*
- **What:** the famous a1k0n rotating, self-shading 3D torus in ASCII — *"a tiny masterpiece of
  geometry, math, and creativity."*
- **Why it fits us:** it is **literally a donut** 🍩 — the emblem of our Donut Law. Making the
  Guild's own symbol *spin in 3D you built from math* is the perfect capstone showpiece. It is
  famous, documented, and standard-library-only.
- **Real technique:** the sphere technique + a torus's two-radius parametric equation, rotated on
  two axes, z-buffered, shaded with `.,-~:;=!*#$@`. (Classic reference: Andy Sloane's "donut math.")
- **Skills:** trig, two-axis rotation, projection, z-buffer, luminance shading. **Level: Hard /
  Master** (Vol IV or the OS gallery's crown jewel).
- **Placement:** **the Gallery capstone** — the "you have arrived" piece. Ties to the Donut Law.
- **Chapter fit:** a **capstone / celebration** beat, or a standalone gallery legend. Not a filler.

### 5. 🚀 The Rocket Launch — *"liftoff in the terminal"*
- **What:** a rocket rising up the screen on a growing column of exhaust, a countdown, then
  clearing the top — a short, triumphant animation (a nod to the launch/landing spirit).
- **Why it fits us:** narrative *and* motion — a celebration you can trigger when a Builder ships
  something. Emotionally on-brand (shipping = liftoff). Achievable with string art + a moving
  vertical position.
- **Real technique:** an ASCII rocket sprite whose y-position decreases each frame; redraw the
  exhaust trail below it; clear + reprint per frame; a countdown before ignition.
- **Skills:** multi-line string art, a moving coordinate, loops, `time`. **Level: Medium** (Vol II).
- **Placement:** **Built** → `pycasso_gallery/rocket_launch.py` (adaptive to the terminal;
  `ROCKET`/`FLAME`/`COLOR`/`SPEED` knobs — a Builder can redraw the ship and set `FLAME = "01"` for
  binary exhaust). **Shown-and-runnable at Vol II Ch 1** ("The Map Grows"): the crew dreams bigger,
  and the rocket *actually lifts off* — even though the full build waits for the volume's later
  skills. Its closing line is the volume's thesis: *"Your dreams lift off the same way: one small
  number, going up, every single frame."* Also a lovely **"you shipped v1!"** celebration animation.
- **Chapter fit:** a **capstone/shipping chapter** (e.g. end of a volume — liftoff = you shipped).

### 6. 🌙 The Moon Landing — *"the eagle has landed"*
- **What:** a lander descending toward a surface, a slowing-descent readout (altitude ticking
  down), gentle touchdown, a little dust puff. A companion piece to the rocket.
- **Why it fits us:** teaches **controlled change over time** (the descent slows — a tiny taste of
  easing/deceleration), wrapped in a story kids love. Pairs with the rocket as a "launch → land"
  set.
- **Real technique:** a lander sprite whose y increases toward the surface, with the step size
  shrinking each frame (deceleration); an altitude counter; a touchdown frame.
- **Skills:** moving sprite, decreasing-step math (easing), loops, `time`. **Level: Medium–Hard** (Vol II–III).
- **Placement:** Vol II–III Gallery, paired with the Rocket.
- **Chapter fit:** a chapter about **controlled/looping change** or a mission-success beat.

---

## Difficulty ladder (at a glance)

| # | Showpiece | Level | Earliest home | Core new idea |
|---|-----------|-------|---------------|---------------|
| 1 | Matrix Rain 🟢 **built** | Medium | Vol I Ch 13 | lists + random + colour = motion |
| 5 | Rocket Launch 🚀 **built** | Medium | Vol II Ch 1 | a moving sprite over time |
| 6 | Moon Landing 🌙 | Medium–Hard | Vol II–III | change that slows (easing) |
| 2 | Starfield ✨ | Medium–Hard | Vol III | perspective by division |
| 3 | Rotating Sphere 🌍 | Hard | Vol III–IV | 3D→2D projection + shading |
| 4 | Spinning Donut 🍩 | Hard/Master | Vol IV / gallery | the full 3D torus (capstone) |

---

## How these connect to the rest of canon

- **Not per-chapter Extras (D-34).** These are the *advanced* Gallery tier; the rotating Extras
  (Joke/Riddle/Art) stay simple and per-chapter. This doc is the aspirational upstairs.
- **Parallel to the Dojo's higher tiers (D-28).** Same philosophy: openly-offered simple stuff,
  self-selected hard stuff; the mountain lives in the open-source gallery, growing by contribution.
- **The OS-project growth path.** The gallery is where curious Builders and contributors add more
  showpieces over time (D-30's "system is canon, mountain grows outside" logic, applied to art).
- **Run it → Hack it → Own it (D-34).** Even these ship with "knobs" — change the rain colour,
  the rocket shape, the sphere's light angle — so a Builder *owns* it, never just runs it.

> **Status of the build:** D-35 is locked; the `pycasso_gallery/` folder now exists with the
> first showpiece built (Matrix Rain). The remaining five get real, bash-verified code in that
> folder as their chapters arrive — built and tested like Dojo missions (Donut Law). The mountain
> grows outside the book by contribution (D-30).

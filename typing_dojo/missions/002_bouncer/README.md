# 🥋 Mission 002 — The Bouncer

> *Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

---

## Story Hook

The Guild door has a new bouncer, and he takes his job *seriously.*

To get in, your password must clear **two** rules:

it has to be **long enough**, and it can't be one of the passwords

every burglar tries first.

Fail, and the bouncer tells you **exactly** which rule you broke.

---

## 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Open **`challenge_1.py`**.

Type it out. Run it. Try to sneak past the bouncer.

Any error is *probably your own typo* — hunt it, fix it, smile.

### Expected output

Try a few passwords and watch the bouncer answer each one:

```
Password, please: abc
Too short. I need at least 8 characters.
```

```
Password, please: password
Nice try. That one is on every burglar's first-guess list.
```

```
Password, please: dragon-tea-42
Welcome in, Builder.
```

*(Notice: `password` is eight letters long — it passes the length rule, then gets caught by the*
*second one. Two separate checks, so the bouncer always knows which door you tripped.)*

---

## 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Open **`challenge_2.py`**.

Same bouncer — but **three typos** slipped in. No logic is broken. Only fingers.

Retype it, run it, and fix each slip until it runs clean.

Run it once and Python hands you your first clue:

```
NameError: name 'inupt' is not defined. Did you mean: 'input'?
```

**Excellent. Now the conversation begins.**

Two more are hiding on the lines below. Find them the same way. 🦑

---

## CS Seeds

`len()` · `booleans` · `and` / `or` / `not` · `if` / `elif` / `else` · `precise error messages`

---

## Guild Flavor

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Sir Boolean gives an approving nod — *this* is what he meant by a rule that explains itself. 🛡️

The Tangle prods the keyboard for a sloppy `elif`, finds none, and slinks away, bored.

Professor Quackers says nothing. Professor Quackers never does. 🦆

---

## Related Missions

- **Chapter 7 — The Safe Password Checker** (where you first *met* this idea — and saw one
  blurry `and`-guard let `"password"` slip through).
- **Mission 001 — Guess the Number** (its Dojo sibling: guess a secret, meet a rule-checker).
- *Coming later:* **The Vault** — a door that makes you guess *and* pass the bouncer at once.
  *(Wait — haven't I done both of these before?)*

---

<sub>**For authors/teachers — not shown to kids (D-30).**
`ID:` 002 · `Title:` The Bouncer · `Engine:` `coding_gold_mine/002_bouncer.py`
· `CS Seeds:` len · booleans · and/or/not · if/elif/else · precise-messages
· `Prerequisites:` Chapter 7 (booleans, `len()`, `and`/`or`/`not`) · `Tiers shipped:` I–II
· `Related:` Ch 7; Mission 001; future echo Mission 009 The Vault (Ch 14).</sub>

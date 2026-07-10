# Chapter 13 — The Painter's Deck

> *"A program that works is a gift. A program that works and looks like it means it —*
> *that's a welcome."*

---

Pycasso came down from the rafters the way weather arrives — unhurried, and impossible to ignore.

He didn't walk so much as *arrive*, trailing a brush that left no mark on anything

it touched, humming a tune nobody else could hear.

"So," he said, circling the Joke Board like a painter circling a blank wall.

"Plain. Functional. Entirely honest." He said *honest* the way some people say

*unfinished.*

Captain Byte crossed his arms. "It works perfectly."

"Oh, it does," Pycasso agreed warmly. "Every gear turns exactly as it should.

That was never in question." He tapped the screen with one paint-stained finger.

"But nobody has ever fallen in love with a gear, Captain. They fall in love with

what the gear *becomes.*"

Dragon Debug, tea in hand as always, allowed the smallest smile.

"Pycasso," he said, "meet TommyBot. TommyBot — the Guild's artist. He believes,

quite sincerely, that every program is a canvas."

"Because it is," said Pycasso, delighted someone had finally said it out loud.

TommyBot looked at the board — the same three lines it had shown since Chapter 12,

unchanged, unadorned. "It's never occurred to me that it could look like

anything at all. It just... prints."

"Everything 'just prints,' at first," said Pycasso. "Then someone decides it

shouldn't have to. Shall we?"

---

## The Task

Pycasso didn't hand over a finished picture. He never did.

"Two ingredients," he said, counting them off on paint-flecked fingers.

"One — give the board a proper **title**, painted in a color, so it *announces*

itself the moment it opens. Two — a little flourish beneath it. Something that

*grows.*"

"Grows how?" asked TommyBot.

"You already know how," said Pycasso, and wandered off to admire a stain on

the ceiling, leaving the actual work — as he always did — to the Builder.

TommyBot thought back to every loop the Guild had ever built. A loop that counts

is a loop that can *paint*, one row taller each time around.

```python
symbol = "\u2726"
height = 4

for row in range(1, height + 1):
    print(symbol * row)
```

`range(1, height + 1)` counts the rows for you — one, two, three, four — and

`symbol * row` repeats the symbol that many times on each line. Four short

lines of code. A little flourish grew right out of them, one row at a time.

Color came next, and it turned out to need almost no new words at all —

just a strange little sequence Dragon Debug called an **escape code**, tucked

in front of the text you actually wanted to show:

```python
GREEN = "\033[92m"

print(GREEN + "*" * 20)
print("GUILD JOKE BOARD")
print("*" * 20)
```

"`\033[92m`," Dragon Debug explained, "is a secret instruction the terminal

understands but never shows you. It doesn't print as text. It tells the

screen: *from here on, paint everything green.*"

TommyBot ran it. The border came up glowing — a soft, unmistakable green,

right where plain white text had always been.

"There," said Pycasso, drifting back over, genuinely moved. "*Now* it welcomes you."

---

## The Honest Bug

Captain Byte, thrilled, immediately started using the board.

He added a joke. Then read the jokes back. Then closed the board, same as always.

And that was when everyone noticed it.

The menu — green. The joke he'd just typed — green. Even *"Choose: "*, the plain

little prompt that had never once changed color in twelve whole chapters — green.

"Why is everything green?" Captain Byte asked, holding up a hand that was, of

course, not actually green, but he checked anyway.

"I only painted the title," said TommyBot, baffled, scrolling back through

the code. "One line. Two, counting the bottom border. That's it."

"Excellent," said Dragon Debug, settling in with his tea. "Now the conversation

begins."

TommyBot stared at the screen a while longer, and then — slowly — thought

back to Chapter 12. To a loop that kept saying goodbye and never actually

left.

"Wait," TommyBot said. "This feels familiar. Back at this same board, we said

goodbye out loud, but never told the loop to *leave* — so it just kept going."

"Go on," said Dragon Debug, which — from him — was practically applause.

"So maybe... painting something green is the same shape of problem. I *turned

the color on.* I never told it to turn back *off.*"

"Is there a word for that?" Dragon Debug asked. Not an answer. A question —

the same way he'd been answering fewer and fewer questions himself, lately,

and asking more of them instead.

TommyBot thought. Then found it, sitting quietly in the same family as the

color code itself — another secret instruction, meant only for the terminal.

```python
RESET = "\033[0m"

print(GREEN + "*" * 20 + RESET)
print("GUILD JOKE BOARD")
print(GREEN + "*" * 20 + RESET)
```

`RESET` doesn't say anything either. It just tells the terminal: *the special

instructions stop here — go back to plain.* Wrap the color at the start, wrap

the reset at the end, and only what sits between the two ever changes.

Captain Byte reopened the board. The title glowed green, exactly as it should.

Everything beneath it — the menu, the jokes, the ordinary "Choose: " — stayed

plain, steady, unpainted.

"There," said Pycasso, and this time even *he* looked satisfied. "A canvas

knows where it ends. That's half of what makes it art, instead of a mess."

---

## 🧪 Testing Table

| Action | Expected | Actual (before `RESET`) | Actual (after `RESET`) |
|---|---|---|---|
| Board opens | Title glows green; everything else stays plain | ❌ title *and* everything after it glows green | ✅ only the title glows |
| Choose 1, add a joke | Menu and prompt stay plain | ❌ menu, prompt, and joke text all tinted green | ✅ plain, as expected |
| Choose 3, close the board | Goodbye message stays plain | ❌ still green | ✅ plain |

---

## 🐛 Debug Log

**My bug:** One colored title line turned the *entire rest of the program* green — the menu, the prompts, even jokes that were never meant to be painted at all.

**What caused it?** `\033[92m` doesn't turn itself off. It's not a setting on one line of text — it's an instruction to the terminal that stays in effect *forever*, on every line that follows, until something explicitly tells it to stop.

**How did I fix it?** Added `RESET` — `"\033[0m"` — right after the colored text, every time. Turn it on, then say, plainly, where it ends.

---

## 🧰 Toolbox Card

> *If you turn something on — a loop, a color, anything at all — the computer will keep it*
> *running exactly as long as you let it. It never assumes you meant to stop. You have to say so.*

---

## 🏗️ In the Real World

> Real command-line tools use color on purpose, never by accident — `git status` shows
> untracked files in red and staged ones in green; installers turn a progress bar green
> only once it's actually done. Builders who design this well have a job title for it:
> **UX** (user experience) — making a tool not just *work*, but make sense at a glance.
>
> One rule travels with it everywhere: color is a bonus, never the only clue. Someone
> colorblind, or reading on an old black-and-white screen, still needs to understand
> everything color was helping to show. The words always have to work on their own first.

---

## 🐉 Dragon Debug's Wisdom

> *"Beautiful and correct are not two different jobs. They're the same job,*
> *finished a little further than most people bother to go."*

---

Captain Byte glanced sideways at his own screen — the plain, honest logic he'd

built with TommyBot, next to Pycasso's effortless flourish — and felt, just

for a second, like the less interesting half of the room.

Pycasso caught the look. He always seemed to.

"Don't do that," he said, gently, no drama in it at all for once. "I can't

make a loop remember anything. I can't fix a bug at two in the morning. What

I do only *works* because your logic was already standing underneath it,

holding the whole thing up." He tapped the screen. "Every Builder who paints

needs a Builder who calculates. You're not the plain half of anything."

TommyBot didn't say much back. Just nodded, and quietly felt a little less

plain.

---

### ⭐ Achievement Unlocked

**Board Painter 🎨** — *You gave a working program its first coat of color, met a bug that spread further than you ever painted it, and learned that "on" always needs a matching "off." The Joke Board finally looks like it means it.*

---

### To be continued...

"Of course," Pycasso added, as the crew packed up for the night, "this is

barely a sketch of what's possible."

He waved a hand at the dark theatre wall, and for just a moment — TommyBot

would swear to it later, though no one else quite saw — hundreds of tiny

green characters seemed to ripple down the stone like rain, then vanished.

"Someday," Pycasso said, watching TommyBot's face carefully, "when you've

got a few more loops in your pocket, and a list that can hold a *position* —

I'll show you what a whole *waterfall* of characters looks like. Falling.

Forever. On purpose."

"That sounds impossible," said TommyBot.

"It's four ideas you already half-know, stacked on top of each other," said

Pycasso. "Everything impossible usually is." And he was gone again, back up

into the rafters, humming.

From TommyBot's pocket, forgotten yet again, the encoded note sat exactly

where it always sat. Patient. Unread. Waiting for its own moment, same as

Pycasso's waterfall.

Some mysteries take longer to paint than others.

→ *Next: The Escape Room — where every trick the Guild has learned gets tested at once.* 🚪

---

## 😄🧩🎨 Guild Extra

😄 Guild Extra — Pycasso's Verdict        (Joke)

Professor Pycasso leaned over Captain Byte's shoulder
and studied a wall of broken code, deeply moved.

"A guitar string and a Python string have so much in common,"
he said. "Both of them just want to be *joined*."

Captain Byte blinked. "That's not — that has nothing to do with my bug."

"No," Pycasso agreed happily. "But look at the shape of that traceback.
Tragic. But honestly? A little beautiful."

He wandered off to go find more art in other people's errors.

---

## 🥋 Typing Dojo — Mission 008: The Sign Painter

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

Pycasso never speaks much about *how*. He just hands you a brush made of loops.

Pick a symbol. Pick a height. Watch a picture climb the screen, one row taller

than the last, until your sign stands finished. Loops don't just count anymore.

Now they draw.

**🥋 Tier I — Keyboard Ninja.** *("Slice your caps.")*

Type this. Run it. Try a few symbols and heights of your own — `*`, `#`, `@`, a `4`, a `9`.

```python
symbol = input("Paint with which symbol? ")
height = int(input("How tall? "))

for row in range(1, height + 1):
    print(symbol * row)
```

Expected output:

```
Paint with which symbol? *
How tall? 4
*
**
***
****
```

**🕵️ Tier II — Conan's Challenge.** *("Do you have any clue?")*

The Guild's copy has three typos hiding in it. No logic is broken — only fingers.

Two of them will stop the paint cold, and Python will point right at them. The

third won't. It paints just fine, and still isn't spelled the way you'd spell it.

```python
symbl = input("Paint with which symbol? ")
height = int(input("How tall? "))

for row ni ragne(1, height + 1):
    print(symbl * row)
```

Run it once, and Python hands you your first clue:

```
  File "challenge_2.py", line 8
    for row ni ragne(1, height + 1):
            ^^
SyntaxError: invalid syntax
```

Retype it, run it, fix what you find — and don't stop at two.

🐉 Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Pycasso says nothing, but paints a tiny dragon in the corner. It is, somehow,

sipping tea. Professor Quackers says nothing either. The two of them get along

beautifully. 🦆

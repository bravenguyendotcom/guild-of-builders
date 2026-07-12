# Chapter 15 — Captain Byte's Treasure Quest v1 🏴‍☠️

> *The one where all your loose games become one game — and you get to say, out loud, "I built this."*

---

It was the last morning of the first voyage.

Captain Byte stood on the deck with a mug of pizza-flavoured cocoa

(don't ask; he insisted; nobody had the heart to stop him)

and looked at everything the crew had made.

It was… a mess.

A wonderful mess.

There was the guessing game, in one file.

The password gate, in another.

The mirror. The coded message. The riddle.

Five little games, in five little files, scattered like coins across the deck.

Each one worked.

Each one, on its own, was finished.

But they didn't stand *together.*

Captain Byte scratched his head.

"Builder," he said, "I want to play *the game.* One game. The whole quest.

Not five separate windows I have to open one at a time like a very disorganised pirate."

TommyBot looked at the five files.

Then at the Captain.

Then at the five files again.

And felt the exact itch every Builder feels right before they learn something new.

---

## The problem with a pile of games

TommyBot could *see* what he wanted.

A ship's console — like the Quest Log from Chapter 12 —

that offered each trial, ran it, and remembered which ones you'd cleared.

But when he tried to write it, he got stuck immediately.

Because to "run the chest," he had to paste the *entire* chest game into the console.

And to "run the gate," paste the *entire* gate game underneath it.

And the mirror. And the cipher. And the riddle.

By the third paste, the file was a thousand lines long

and TommyBot had lost track of which loop belonged to which game.

"There has to be a way," he muttered, "to give each game a **name.**

So I can just… call it. By name. Like calling a friend across the deck."

Dragon Debug, who had been quietly watching over the rim of his tea,

set the mug down.

"There is," he said. "You just described it perfectly.

That thing you want — a chunk of code with a name you can call —

it's the most useful idea in all of programming.

It's called a **function.**"

---

## The one new word: `def`

A function is a box of code with a name on the lid.

You write the code *once.*

You give it a name.

And after that, you can run all of it by just saying its name — with two little parentheses.

You already know the word for making a box with a name.

For a *value*, it was `=`.

For a *chunk of code*, it's `def` — short for **define.**

Watch what happens to the guessing game from Chapter 6.

Here it is, wrapped in a name:

```python
def crack_the_chest():
    """The Chest — guess the number to crack it open (Mission 001)."""
    print()
    print("🔒 THE CHEST")
    print("A locked chest hums with treasure. Guess the number, 1 to 20.")
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Your guess (1-20): ")
        if not guess.isdigit():
            print("The lock only understands numbers, Captain.")
            continue
        guess = int(guess)
        attempts = attempts + 1
        if guess == secret:
            print("*click* The chest springs open! It took", attempts, "tries.")
            return True
        elif guess < secret:
            print("Too low. The lock stays shut.")
        else:
            print("Too high. The lock stays shut.")
```

Stop for a second.

Look at line one.

Then look at everything under it.

That's *your* guessing game.

The one you built in Chapter 6, all those adventures ago.

The `while` loop. The `random.randint`. The "Too low" and "Too high."

It hasn't changed.

You just wrote `def crack_the_chest():` on top and pushed everything one step to the right.

Now it has a **name.**

Now, anywhere in your program, you can run that whole game

by writing five little characters:

```python
crack_the_chest()
```

TommyBot stared at the screen.

"That's my game," he said quietly. "That's *my* chest game. From Chapter Six.

And now it has a name, and I can just… call it."

"Yes," said Dragon Debug.

"Say hello to your past self. She did good work."

---

## Five names, one deck

TommyBot did it five times.

He wrapped each loose game in a `def` and gave it a name:

- `crack_the_chest()` — the guessing game 🔒
- `pass_the_gate()` — the password check 🚪
- `face_the_mirror()` — the palindrome 🪞
- `decode_message()` — the Caesar cipher 🗝️
- `answer_riddle()` — Monty and Quizzalot's riddle 🎭

Notice the little `return True` at the end of each one.

That's the game *reporting back:* **"Cleared it."**

A function can hand you back an answer when it's done —

so the console can know whether you passed.

Then he built the console itself — the ship's wheel of the whole game.

It's the menu loop from Chapter 12, exactly.

A list. A `while True`. A choice. And now, five functions to call:

```python
    trials = [
        ("Crack the Chest      🔒", minigames.crack_the_chest),
        ("Pass the Gate        🚪", minigames.pass_the_gate),
        ("Face the Mirror      🪞", minigames.face_the_mirror),
        ("Decode the Message   🗝️", minigames.decode_message),
        ("Answer the Riddle    🎭", minigames.answer_riddle),
    ]

    cleared = []          # names of trials cleared

    while True:
        # ...show the menu, ✔ the ones you've cleared...
        choice = input("Orders, Captain? ")

        if choice in ["1", "2", "3", "4", "5"]:
            index = int(choice) - 1
            run_trial = trials[index][1]
            if run_trial():                 # <- call it! run the game!
                cleared.append(name)
```

Look at that list.

Each row pairs a *label you can read* with a *function you can call.*

"Crack the Chest" sits right next to `crack_the_chest`.

The menu picks one, and `run_trial()` **runs it.**

The pile of games became a ship.

---

## The honest bug 🐛

TommyBot ran it.

He was so excited he'd written the console at the *top* of the file,

and the little test call — `crack_the_chest()` — right at the very top, before anything else.

Python read the file top to bottom, hit the call, and stopped cold:

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    crack_the_chest()
    ^^^^^^^^^^^^^^^
NameError: name 'crack_the_chest' is not defined
```

TommyBot's face fell. "But I *did* define it! It's right there, below!"

Dragon Debug smiled.

**"Excellent. Now the conversation begins."**

He tapped the screen, gently.

"Python reads your file the way you read a book — top to bottom, one line at a time.

You asked it to *call* `crack_the_chest` on line 3.

But you didn't *define* it until line 40.

On line 3, Python has never heard that name in its life.

So it tells you the truth: *I don't know that name yet.*"

"So I just…"

"Define first. Call after.

Teach Python the name *before* you ask it to use the name."

That's exactly why the real, finished game

**defines every function first**

and puts the one line that starts everything —

```python
if __name__ == "__main__":
    main()
```

— at the *very bottom* of the file.

By the time Python reaches that last line,

it has already met every name it will ever need.

TommyBot moved his defs up.

He ran it again.

The console appeared. The menu waited. The chest opened when he called it.

Not a broken thing.

A *conversation* that ended in a handshake.

---

## 🐛 Debug Log

| 🐛 The bug | 🔍 The cause | 🔧 The fix |
|-----------|-------------|-----------|
| `NameError: name 'crack_the_chest' is not defined` | The function was *called* on line 3, but not *defined* until line 40. Python reads top-to-bottom and hadn't met the name yet. | **Define first, call after.** Move every `def` above the code that calls it — which is why the finished game calls `main()` on the last line. |

---

## 🧪 Testing Table

The real test of a whole game isn't one line.

It's this: *can you play it, start to finish, without it falling over?*

So TommyBot played the whole quest — every trial, then "Claim the Treasure."

| What I did | Expected | Actual |
|-----------|----------|--------|
| Chose **1**, guessed the chest number | `*click*` chest opens, trial marked ✔ | ✔ |
| Chose **2**, typed an 8-letter password | Gate rumbles open, marked ✔ | ✔ |
| Chose **3**, spoke `level` | Mirror lets me through, marked ✔ | ✔ |
| Chose **4**, decoded `wuhdvxuh` → `treasure` | Message decoded, marked ✔ | ✔ |
| Chose **5**, answered `echo` | Monty bows, marked ✔ | ✔ |
| Chose **6** with all five cleared | Treasure hatch opens, win ending, achievements | ✔ |

Every row a checkmark.

That's what "it works" actually means:

not "it ran once," but "it runs *all the way through,* the way a player would play it."

---

## 🧰 Toolbox Card

> *A function is a recipe with a name.*
>
> Writing `crack_the_chest` — just the name — is like reading the recipe card
> and putting it back in the drawer. Nothing cooks.
>
> Writing `crack_the_chest()` — with the two little parentheses —
> is like actually **making the dish.** The `()` means *"run it now."*
>
> And Python has to have *read* the recipe (`def ...`) before you can cook it.
> **Define first. Call after.**

---

## 🏗️ In the Real World

> Today you earned four real words that grown-up Builders use every single day.
>
> A **function** — a named piece of code you can call again and again.
> Real programs are made almost entirely of them.
>
> **Shipping** — the moment you stop building and let someone actually *use* it.
> Not "shown to the teacher." *Used.* By a friend. For real.
>
> **Version 1** — the first one that works. Not the best one you'll ever make.
> The first one real people can hold.
>
> And the most grown-up word of all: **done.**
>
> "Done" doesn't mean *done forever* — you'll make it better in Volume Two.
> "Done" means **done enough to share.**
>
> Knowing when something is done enough to share is called the **definition of done** —
> and it's one of the hardest, most important things a real Builder ever learns.
> You just learned it by living it.

---

## ⭐ Achievement Unlocked

**CLI Builder 💻** — *You didn't learn a lesson today. You crossed a line. This morning you were someone learning Python. Tonight you are someone who has **built and shipped a game** — a real one, made of your own five games, standing together on one deck. The game itself handed you two badges on the way out: 🏅 Trial Master and 🏅 Treasure Finder. But this one is yours to keep for good.*

---

## Say it out loud

TommyBot ran the finished game one more time,

start to finish, and reached the ending he had built without quite realising it.

The screen filled with gold.

And then Captain Byte's own words appeared —

the ones TommyBot had typed himself, days ago, without knowing they'd land like this:

```
Captain Byte claps you on the shoulder. 'You didn't just
play a game, Builder. You BUILT one. Say it out loud: I built this.'
```

There was a small, wobbly silence.

Because here's the secret nobody warns you about shipping something real:

right before you show it to someone, your stomach does a little flip.

*What if they don't like it. What if it breaks. What if it's not good enough.*

TommyBot felt every bit of that flip.

Dragon Debug saw it — dragons always see it — and said the truest thing he knew:

**"Version 1 beats perfect."**

"Your game isn't the best game that will ever exist.

It's better than that.

It's the first one that's *real,* and *finished,* and *yours,*

and a friend can play it tonight.

Show them. The flip in your stomach just means it matters."

So TommyBot did.

He said it out loud.

*"I built this."*

And meant it.

---

## The door at the end (this is Volume Two)

Then Captain Byte did something unusual.

He got quiet.

He looked at the console — the neat menu, the five clean trials — and tilted his head.

"It's brilliant, Builder. Truly. But…"

He pointed at the menu.

"Right now, the chest and the gate don't *know each other.*

You crack the chest. Then, separately, you open the gate.

But what if the number you crack out of the chest

was the **key** you carried to the gate?

What if your choices in one trial *mattered* in the next?

What if it wasn't a menu of five little games…

but **one woven journey**?"

TommyBot's eyes went wide.

Because he could *see* it now — a whole game where everything connected —

and he could also see, clearly, that he didn't quite know how to build it yet.

That itch. Right on cue.

Dragon Debug smiled into his tea.

"That feeling — *I can see something bigger than I can build yet* —

that's not frustration, Builder. That's the door to Volume Two."

He counted it out on three claws.

"Volume Two gives you a game that **remembers** —

one that can save your voyage and load it again tomorrow.

A world with **more than one room.**

Characters who **talk back.**

The very tools you'd need to weave this menu into a world."

"And here's the part I love most," said the Captain.

"You don't start over. You never start over.

This ship right here — *this exact game* — is the one that grows.

Same crew. Same treasure. Same *you.*

Just bigger."

He grinned.

"Same game. Bigger. See you in Volume Two."

---

Later, when the deck was quiet,

TommyBot reached into his pocket

and found the little encoded note that had been riding there since the Escape Room —

patient, unread, waiting.

He looked at it differently now.

Because somewhere in the game he'd just shipped

was a function that could shift letters back along the alphabet.

He *had* the tool now. He could read it.

He unfolded it halfway…

then stopped, and smiled, and tucked it away again.

Some notes point further than one voyage can sail.

This one pointed past the horizon —

toward a bigger ship, a woven world, and a treasure the menu couldn't hold.

"Interesting," said Dragon Debug, who had definitely not been reading over his shoulder.

He raised his tea to the Builder who, somewhere across this first voyage,

had quietly stopped being the student —

and started becoming the one *he'd* be asking questions of, one day soon.

We are not teaching Python.

We are raising Builders.

And this one just shipped their first game.

→ *Next: **Volume Two** — the same ship, grown. A game that remembers. A world with rooms. See you there.* 🏴‍☠️🍩

---

## 😄🧩🎨 Guild Extra

🎨 Guild Extra — The Victory Star        (Art)

One last spark, for the Builder who just shipped their first game.

```python
BOOM_FACTOR = 4
line = "*"

step = 0
while step < BOOM_FACTOR:
    spaces = BOOM_FACTOR - step
    print(" " * spaces + line)
    line = line + "**"
    step = step + 1
```

Expected output:
```
    *
   ***
  *****
 *******
```

🎨 Hack it: change `BOOM_FACTOR` to `8` and watch your victory star
grow as big as your first shipped game deserves.

---

## 🥋 Typing Dojo — Mission 010: The Ship's Console

*Dragon Debug's Typing Dojo. The tea is hot. The squid is watching.*

This is the last mission of the voyage — and it's the whole ship in one small screen.

Recruit your crew. Muster them on deck. Then give the order to set sail.

A menu that loops. A list that remembers. A word that ends it.

You built this shape once already, for your Quest Log. Now it steers the whole game.

*(You don't have to open this door. The story's finished — the treasure is claimed, Volume Two is already calling. This part is just here, if you want it. Pure play.)*

---

### 🥋 Tier I — Keyboard Ninja  *("Slice your caps.")*

Type it out. Run it. Recruit a few of your own crew — friends, heroes, the ship's cat.

Any error is *probably your own typo* — hunt it, fix it, smile.

```python
# The Ship's Console

crew = []

while True:
    print()
    print("=== CAPTAIN BYTE'S CONSOLE ===")
    print("1) Recruit a crew member")
    print("2) Muster the crew")
    print("3) Set sail")
    choice = input("Orders, Captain? ")

    if choice == "1":
        name = input("Name the recruit: ")
        crew.append(name)
        print(name, "signs the ship's book.")
    elif choice == "2":
        print("Crew aboard:", len(crew))
        for name in crew:
            print("-", name)
    elif choice == "3":
        print("Anchors aweigh! The voyage begins.")
        break
    else:
        print("That's not an order I know, Captain.")
```

**Expected output:**

```
=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 1
Name the recruit: Sir Boolean
Sir Boolean signs the ship's book.

=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 2
Crew aboard: 1
- Sir Boolean

=== CAPTAIN BYTE'S CONSOLE ===
1) Recruit a crew member
2) Muster the crew
3) Set sail
Orders, Captain? 3
Anchors aweigh! The voyage begins.
```

*(It's the Quest Log from Chapter 12, wearing a captain's hat. Same menu loop, same `.append()`, same `break`. The capstone didn't need a new trick — just the ones you kept.)*

---

### 🕵️ Tier II — Conan's Challenge  *("Do you have any clue?")*

Same console — but **three typos** slipped in. No logic is broken. Only fingers.

Two of them will stop the ship cold, and Python will point right at them.

The third won't. It sails just fine and still isn't spelled the way you'd spell it.

Type it, run it, fix what you find — and don't stop at two.

```python
# The Ship's Console
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

craw = []

while True:
    print()
    print("=== CAPTAIN BYTE'S CONSOLE ===")
    print("1) Recruit a crew member")
    print("2) Muster the crew")
    print("3) Set sail")
    choice = input("Orders, Captain? ")

    if choice == "1"
        name = input("Name the recruit: ")
        craw.append(name)
        print(name, "signs the ship's book.")
    elif choice == "2":
        print("Crew aboard:", len(craw))
        for name in craw:
            print("-", name)
    elif choice == "3":
        print("Anchors aweigh! The voyage begins.")
        braek
    else:
        print("That's not an order I know, Captain.")
```

Run it once and Python hands you your first clue:

```
  File "challenge_2.py", line 15
    if choice == "1"
                    ^
SyntaxError: expected ':'
```

**Excellent. Now the conversation begins.** 🦑

Fix that one, and try to set sail — Python steps forward with the next clue.

The third slip won't crash a thing. It'll sail just fine, and still isn't spelled the way you'd spell it. Hunt it anyway.

---

**Guild Flavor**

Dragon Debug takes a slow sip and murmurs, *"Interesting."*

Captain Byte recruits a pizza as his first mate. No one has the heart to stop him.

Professor Quackers says nothing — but signs the ship's book. 🦆

---

*This is Mission 007, promoted to captain. Same menu loop, now steering the whole game.*

*You've reached the end of the first voyage — every engine in this deck, you can now type by heart.*

***Version 1 beats perfect. And you just built your first one.*** 🏴‍☠️

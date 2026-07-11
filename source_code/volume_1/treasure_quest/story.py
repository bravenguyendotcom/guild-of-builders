# story.py
# All the words: the title screen, the intro, the map between stops,
# and the endings. Kept separate from the game logic so the story can
# grow without touching the machinery (Ch 13 taught us: a canvas knows
# where it ends).

GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def title_screen():
    print(GREEN + "=" * 44 + RESET)
    print(GREEN + "     CAPTAIN BYTE'S TREASURE QUEST  v1" + RESET)
    print(GREEN + "=" * 44 + RESET)
    print("            🏴‍☠️  a Guild of Builders game  🏴‍☠️")
    print()


def intro():
    print("Captain Byte leans on the ship's wheel and grins at you.")
    print()
    print('"Builder! The map is real. The treasure is out there —')
    print(' past a locked chest, a guarded gate, a magic mirror, a')
    print(' coded message, and two hosts who WILL make you groan."')
    print()
    print('"Everything we need, we already built together. Pick a')
    print(' heading from the console, clear each trial, and the')
    print(' treasure is ours. Ready?"')
    print()


def stop_cleared(name):
    print()
    print(YELLOW + "  ✔ " + name + " cleared!" + RESET)


def all_clear():
    print()
    print("Dragon Debug sips his tea. 'Every trial, standing behind you.")
    print("Now they stand together. That — is a program.'")


def win_ending(cleared_count, achievements):
    print()
    print(GREEN + "🏴‍☠️  THE TREASURE" + RESET)
    print("The final hatch opens. Gold spills across the deck — enough")
    print("to make even Professor Quackers say something. (He doesn't.)")
    print()
    print("You cleared", cleared_count, "of 5 trials.")
    if achievements:
        print("Achievements earned:")
        for a in achievements:
            print("   🏅 " + a)
    print()
    print("Captain Byte claps you on the shoulder. 'You didn't just")
    print("play a game, Builder. You BUILT one. Say it out loud: I built this.'")
    print()
    print("🌱 One more thing, though... right now this is a *menu* of")
    print("   adventures. But what if it were one woven journey — where")
    print("   the number you crack from the chest becomes the key to the")
    print("   gate? Where your choices carried across the whole voyage?")
    print("   Hold that thought. That's Volume II thinking. 🐉")


def goodbye():
    print()
    print("Fair winds, Builder. The Guild will be here when you sail back. 🍩")

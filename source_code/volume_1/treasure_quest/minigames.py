# minigames.py
# The five story-stops of Captain Byte's Treasure Quest v1.
# Each one is a mini-game you already built earlier in Volume I,
# now wrapped as a function the ship's console can call.
#
#   crack_the_chest()  -> guess-the-number   (Ch 6  / Mission 001)
#   pass_the_gate()    -> password check     (Ch 7  / Mission 002)
#   face_the_mirror()  -> palindrome puzzle  (Ch 9  / Mission 004)
#   decode_message()   -> Caesar cipher      (Ch 10 / Mission 005)
#   answer_riddle()    -> a riddle gate      (Ch 11 / Monty & Quizzalot)
#
# Every function returns True if the Builder cleared it, False if not.
# Volume I skills only: input, loops, if/elif/else, random, strings.

import random


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


def pass_the_gate():
    """The Gate — a password check (Mission 002)."""
    print()
    print("🚪 THE GATE")
    print("A stone gate blocks the path. The password is at least 8 letters,")
    print("and it is NOT the word 'password'. Choose one to open the gate.")
    while True:
        pw = input("Set the password: ")
        if len(pw) < 8:
            print("Too short — the gate needs at least 8 letters.")
        elif pw == "password":
            print("Too obvious! Any pirate would guess that.")
        else:
            print("The gate rumbles open. Well guarded, Captain.")
            return True


def face_the_mirror():
    """The Mirror — a palindrome puzzle (Mission 004)."""
    print()
    print("🪞 THE MIRROR")
    print("A magic mirror will only let a *palindrome* pass —")
    print("a word spelled the same forwards and backwards (like 'level' or 'noon').")
    while True:
        word = input("Speak a palindrome: ")
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        if len(word) > 0 and word == reversed_word:
            print("The mirror ripples and lets you through. Beautifully symmetric!")
            return True
        else:
            print("The mirror frowns. '" + word + "' reversed is '" + reversed_word + "'. Try again.")


def decode_message():
    """The Coded Message — decode a Caesar cipher (Mission 005)."""
    print()
    print("🗝️  THE CODED MESSAGE")
    print("A scrap of parchment holds a secret, shifted 3 letters down the alphabet.")
    secret_word = "treasure"
    shift = 3

    coded = ""
    for letter in secret_word:
        shifted = ord(letter) + shift
        if shifted > ord("z"):
            shifted = shifted - 26
        coded = coded + chr(shifted)

    print("The parchment reads:  " + coded)
    print("Shift each letter 3 back to read it.")

    while True:
        answer = input("What does it say? ").lower().strip()
        if answer == secret_word:
            print("Decoded! The message pointed the way all along.")
            return True
        else:
            print("That's not it yet. Shift each letter back by 3 and try again.")


def answer_riddle():
    """The Riddle — a riddle gate from Monty & Quizzalot (Ch 11)."""
    print()
    print("🎭 THE RIDDLE")
    print("Maestro Monty strikes a pose. Sir Quizzalot demands a drumroll. 🥁")
    print('"I speak without a mouth and hear without ears.')
    print(' I have no body, but I come alive with the wind. What am I?"')
    answers = ["echo", "an echo", "a echo"]
    tries = 0
    while tries < 3:
        answer = input("Your answer: ").lower().strip()
        if answer in answers:
            print('Monty bows. Quizzalot weeps with pride. "AN ECHO! Bravo!"')
            return True
        tries = tries + 1
        if tries < 3:
            print("Not quite. (Hint: you hear it in a canyon.)")
    print("The hosts wave you through anyway. 'Even heroes need a nudge,' says Monty.")
    return True

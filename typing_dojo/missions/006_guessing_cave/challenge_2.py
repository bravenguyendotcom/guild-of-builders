# The Guessing Cave
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

import random

secret = randon.randint(1, 100)
guess = 0
attemps = 0

whlie guess != secret:
    guess = int(input("Guess my number (1-100): "))
    attemps = attemps + 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print("You got it in", attemps, "guesses!")

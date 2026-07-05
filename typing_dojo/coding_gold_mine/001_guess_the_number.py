# 🥋 Typing Dojo — Coding Gold Mine
# Engine 001: Guess the Number
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   The computer hides a number from 1 to 100.
#   You guess. It says "Too low" or "Too high" — and counts your tries.
#   You never lose. You only find it.
#
# CS seeds: while-loop · != · random.randint · counter pattern · loop exit
# First typeable at: Chapter 6 (The Secret Treasure).

import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess my number (1-100): "))
    attempts = attempts + 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print("You got it in", attempts, "guesses!")

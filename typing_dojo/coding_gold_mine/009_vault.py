# 🥋 Typing Dojo — Coding Gold Mine
# Engine 009: The Vault  (composite Echo of 001 + 002, D-23)
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   Two locks on one door. First the bouncer from Chapter 7 checks your
#   password (long enough? not a silly one?) -- and if you get past it,
#   the guessing game from Chapter 6 makes you crack the combination.
#   Nothing new here on purpose: this is TWO old friends, working together.
#   Recognising them IS the lesson.
#
# CS seeds: len() + == check (echo 002) * while + != + counter + random (echo 001) * integration
# First typeable at: Chapter 14 (The Escape Room).

import random

password = input("Vault password: ")

if len(password) < 8:
    print("Too short. The vault won't even listen.")
elif password == "password":
    print("Really? 'password'? The vault laughs at you.")
else:
    secret = random.randint(1, 20)
    guess = 0
    attempts = 0
    while guess != secret:
        guess = int(input("Combination (1-20): "))
        attempts = attempts + 1
        if guess < secret:
            print("Higher.")
        elif guess > secret:
            print("Lower.")
    print("CLUNK! The vault opens in", attempts, "tries.")

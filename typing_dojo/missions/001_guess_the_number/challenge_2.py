# Guess the Number
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs — only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secrit:
    guess = int(imput("Guess my number (1-100): "))
    attempts = attempts + 1
    if guess < secret:
        pirnt("Too low.")
    elif guess > secret:
        print("Too high.")

print("You got it in", attempts, "guesses!")

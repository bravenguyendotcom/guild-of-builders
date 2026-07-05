# Guess the Number

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

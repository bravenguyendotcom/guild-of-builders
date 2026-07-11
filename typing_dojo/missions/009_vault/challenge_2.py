# The Vault
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

import random

 password = input("Vault password: ")

if lenn(password) < 8:
    print("Too short. The vault won't even listen.")
elif password == "password":
    print("Really? 'password'? The vault laughs at you.")
else:
    secret = random.randint(1, 20)
    guess = 0
    attempts = 0
    while guess =! secret:
        guess = int(input("Combination (1-20): "))
        attempts = attempts + 1
        if guess < secret:
            print("Higher.")
        elif guess > secret:
            print("Lower.")
    print("CLUNK! The vault opens in", attempts, "tries.")

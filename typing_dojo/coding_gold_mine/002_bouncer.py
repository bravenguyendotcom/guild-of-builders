# 🥋 Typing Dojo — Coding Gold Mine
# Engine 002: The Bouncer
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   A bouncer guards the Guild door. A password must pass TWO rules:
#     1. be at least 8 characters long
#     2. not be a famous, easy-to-guess password
#   It checks each rule on its own, so it can say EXACTLY which one failed.
#   (Chapter 7's lesson: one blurry `and`-guard hides the reason;
#    separate checks explain themselves.)
#
# CS seeds: len() · booleans · and / or / not · if / elif / else · precise messages
# First typeable at: Chapter 7 (The Safe Password Checker).

password = input("Password, please: ")

if len(password) < 8:
    print("Too short. I need at least 8 characters.")
elif password == "password" or password == "12345678":
    print("Nice try. That one is on every burglar's first-guess list.")
else:
    print("Welcome in, Builder.")

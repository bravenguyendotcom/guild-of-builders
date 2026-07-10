# 🥋 Typing Dojo — Coding Gold Mine
# Engine 005: Secret Cipher (Caesar)
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   Turns each letter into its secret number with ord(), slides that
#   number along by the shift, and turns it back into a character with
#   chr(). That's "character math" -- the oldest secret code in the
#   world, built from nothing but counting. Shift back by the same
#   amount to read it again. (No modulo yet -- that magic comes later.)
#
# CS seeds: ord() * chr() * character math * string building * encoding
# First typeable at: Chapter 10 (The Caesar Messenger).

message = input("Message to encode: ")
shift = int(input("Shift by how many? "))

secret = ""
for letter in message:
    code = ord(letter)
    secret = secret + chr(code + shift)

print("Encoded:", secret)

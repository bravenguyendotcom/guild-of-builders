# 🥋 Typing Dojo — Coding Gold Mine
# Engine 004: Mirror, Mirror
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   Builds the reverse of a word by walking it one letter at a time
#   and stacking each new letter in FRONT of the ones already found --
#   no .reverse() shortcut (strings don't have one; that's the honest
#   bug this mission's chapter teaches). Then compares the word to its
#   reverse to check whether it's a palindrome.
#
# CS seeds: string iteration * string concatenation * comparison * palindrome check
# First typeable at: Chapter 9 (The Palindrome Mirror).

word = input("Say a word for the Mirror: ")

reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    print(word, "is a palindrome. The Mirror agrees with itself.")
else:
    print(word, "is not a palindrome.")

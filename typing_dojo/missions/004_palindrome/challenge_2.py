# Mirror, Mirror
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

word = input("Say a word for the Mirror: ")

reversd_word = ""
fro letter in word:
    reversd_word = letter + reversd_word

if word = reversd_word:
    print(word, "is a palindrome. The Mirror agrees with itself.")
else:
    print(word, "is not a palindrome.")

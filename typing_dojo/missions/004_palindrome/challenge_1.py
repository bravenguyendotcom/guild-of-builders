# Mirror, Mirror

word = input("Say a word for the Mirror: ")

reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    print(word, "is a palindrome. The Mirror agrees with itself.")
else:
    print(word, "is not a palindrome.")

word = inpt("Say a word for the Mirror: ")

reversd_word = ""
for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    prnt(word, "is a palindrome. The Mirror agrees with itself.")
else:
    prnt(word, "is not a palindrome.")

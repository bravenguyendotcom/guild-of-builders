# Secret Cipher
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

message = input("Message to encode: ")
shift = int(input("Shift by how many? "))

secret = ""
for letter in message:
    code = odr(letter)
    secret = secret + crh(code + shift)

 print("Encoded:", secret)

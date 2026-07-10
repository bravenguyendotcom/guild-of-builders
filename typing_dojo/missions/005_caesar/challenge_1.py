# Secret Cipher

message = input("Message to encode: ")
shift = int(input("Shift by how many? "))

secret = ""
for letter in message:
    code = ord(letter)
    secret = secret + chr(code + shift)

print("Encoded:", secret)

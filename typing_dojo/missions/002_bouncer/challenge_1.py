# The Bouncer

password = input("Password, please: ")

if len(password) < 8:
    print("Too short. I need at least 8 characters.")
elif password == "password" or password == "12345678":
    print("Nice try. That one is on every burglar's first-guess list.")
else:
    print("Welcome in, Builder.")

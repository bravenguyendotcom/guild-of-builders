# The Bouncer
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs — only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

password = inupt("Password, please: ")

if lem(password) < 8:
    print("Too short. I need at least 8 characters.")
elif password == "password" or password == "12345678":
    prnt("Nice try. That one is on every burglar's first-guess list.")
else:
    print("Welcome in, Builder.")

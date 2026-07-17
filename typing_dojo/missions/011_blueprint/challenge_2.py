# The Blueprint
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

wishlsit = ["an inventory", "a shopkeeper who haggles", "save and continue",
            "many rooms", "a bestiary", "colour"]

print("=== TREASURE QUEST v2 - THE BLUEPRINT ===")
print("Dreams on the map:", len(wishlsit))
print()

count = itn(input("How many can you honestly ship first? "))

number = 1
for feature in wishlsit:
    if number =< count:
        print(number, "[v1]", feature)
    else:
        print(number, "[later]", feature)
    number = number + 1

print()
print("Ship", count, "things. Then sail again.")

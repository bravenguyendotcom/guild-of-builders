# The Blueprint

wishlist = ["an inventory", "a shopkeeper who haggles", "save and continue",
            "many rooms", "a bestiary", "colour"]

print("=== TREASURE QUEST v2 - THE BLUEPRINT ===")
print("Dreams on the map:", len(wishlist))
print()

count = int(input("How many can you honestly ship first? "))

number = 1
for feature in wishlist:
    if number <= count:
        print(number, "[v1]", feature)
    else:
        print(number, "[later]", feature)
    number = number + 1

print()
print("Ship", count, "things. Then sail again.")

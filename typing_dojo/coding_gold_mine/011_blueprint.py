# 🥋 Typing Dojo — Coding Gold Mine
# Engine 011: The Blueprint
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   Reads a tiny spec -- the v2 wishlist -- and turns it into a checklist,
#   drawing the line between what ships in version 1 and what waits. Every
#   dream stays on the map. Only the honest few get built first.
#
#   Nothing new here on purpose: a list, a walk, a counter, a compare --
#   all of it Volume I. Chapter 1 teaches a RITUAL, not a keyword. The new
#   thing you learn is the habit of planning, and the habit fits in code
#   you already own.
#
# CS seeds: reading a spec * list walk * counter * cutoff compare * scope / v1 thinking
# First typeable at: Volume II, Chapter 1 (The Map Grows).

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

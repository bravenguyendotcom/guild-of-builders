# 🥋 Typing Dojo — Coding Gold Mine
# Engine 010: The Ship's Console  (Echo of 007, D-23)
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   The main menu of the whole game -- recruit crew, muster them, set sail.
#   It's the exact shape of the Quest Log from Chapter 12: a menu that loops,
#   a list that remembers, a break that ends it. The capstone doesn't need a
#   new idea. It needs the ones you already have, standing together on deck.
#
# CS seeds: menu loop (while True + break) * list.append() * list state (echo 007)
# First typeable at: Chapter 15 (Captain Byte's Treasure Quest v1 -- capstone).

crew = []

while True:
    print()
    print("=== CAPTAIN BYTE'S CONSOLE ===")
    print("1) Recruit a crew member")
    print("2) Muster the crew")
    print("3) Set sail")
    choice = input("Orders, Captain? ")

    if choice == "1":
        name = input("Name the recruit: ")
        crew.append(name)
        print(name, "signs the ship's book.")
    elif choice == "2":
        print("Crew aboard:", len(crew))
        for name in crew:
            print("-", name)
    elif choice == "3":
        print("Anchors aweigh! The voyage begins.")
        break
    else:
        print("That's not an order I know, Captain.")

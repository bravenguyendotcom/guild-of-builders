# 🥋 Typing Dojo — Coding Gold Mine
# Engine 007: The Quest Log
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   A little program that keeps running, showing a menu, and remembering
#   your quests in a list between choices. Add quests, show them all,
#   close the log. This is the shape of almost every real program you'll
#   ever write: a loop, a menu, and some state that sticks around.
#
# CS seeds: menu loop (while True + break) * list.append() * list state * if/elif dispatch
# First typeable at: Chapter 12 (Menus & Mini-Programs).

quests = []

while True:
    print()
    print("QUEST LOG")
    print("1) Add a quest")
    print("2) Show all quests")
    print("3) Close the log")
    choice = input("Choose: ")

    if choice == "1":
        quest = input("New quest: ")
        quests.append(quest)
        print("Added:", quest)
    elif choice == "2":
        print("You have", len(quests), "quests:")
        for quest in quests:
            print("-", quest)
    elif choice == "3":
        print("The log closes. Fair winds, Builder.")
        break
    else:
        print("That's not on the menu.")

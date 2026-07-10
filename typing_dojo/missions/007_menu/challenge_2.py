# The Quest Log
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

quests = []

while True
    print()
    print("QUEST LOG")
    print("1) Add a quest")
    print("2) Show all quests")
    print("3) Close the log")
    choice = input("Choose: ")

    if choice == "1":
        quest = input("New quest: ")
        quests.apend(quest)
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

# The Quest Log

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

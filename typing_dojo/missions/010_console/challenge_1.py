# The Ship's Console

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

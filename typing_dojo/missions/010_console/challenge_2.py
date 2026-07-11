# The Ship's Console
# 🕵️ Conan's Challenge: three typos hide in here. No logic bugs -- only slips
# of the fingers. Retype it, run it, and fix each one until it runs clean.

craw = []

while True:
    print()
    print("=== CAPTAIN BYTE'S CONSOLE ===")
    print("1) Recruit a crew member")
    print("2) Muster the crew")
    print("3) Set sail")
    choice = input("Orders, Captain? ")

    if choice == "1"
        name = input("Name the recruit: ")
        craw.append(name)
        print(name, "signs the ship's book.")
    elif choice == "2":
        print("Crew aboard:", len(craw))
        for name in craw:
            print("-", name)
    elif choice == "3":
        print("Anchors aweigh! The voyage begins.")
        braek
    else:
        print("That's not an order I know, Captain.")

# main.py
# Captain Byte's Treasure Quest v1 — the ship's console.
#
# This is the menu loop from Chapter 12 (Missions 007 / 010), now steering
# a whole game. It doesn't need a new idea. It needs the ones you already
# have, standing together on deck.
#
# Run it:   python3 main.py
# Volume I skills only.

import story
import minigames


def play():
    story.title_screen()
    story.intro()

    # Each trial: menu label -> the function that runs it.
    trials = [
        ("Crack the Chest      🔒", minigames.crack_the_chest),
        ("Pass the Gate        🚪", minigames.pass_the_gate),
        ("Face the Mirror      🪞", minigames.face_the_mirror),
        ("Decode the Message   🗝️", minigames.decode_message),
        ("Answer the Riddle    🎭", minigames.answer_riddle),
    ]

    cleared = []          # names of trials cleared
    achievements = []

    while True:
        print()
        print("=== THE SHIP'S CONSOLE ===")
        for number in range(len(trials)):
            label = trials[number][0]
            mark = " ✔" if trials[number][0] in cleared else "  "
            print(str(number + 1) + ") " + label + mark)
        print("6) Claim the Treasure  🏴‍☠️")
        print("0) Weigh anchor (quit)")

        choice = input("Orders, Captain? ")

        if choice in ["1", "2", "3", "4", "5"]:
            index = int(choice) - 1
            name = trials[index][0]
            if name in cleared:
                print("Already cleared, Captain. Onward!")
                continue
            run_trial = trials[index][1]
            if run_trial():
                cleared.append(name)
                story.stop_cleared(name)
                if len(cleared) == len(trials):
                    story.all_clear()

        elif choice == "6":
            if len(cleared) == len(trials):
                if "Trial Master" not in achievements:
                    achievements.append("Trial Master")
                achievements.append("Treasure Finder")
                story.win_ending(len(cleared), achievements)
                return
            else:
                remaining = len(trials) - len(cleared)
                print("The treasure hatch won't budge —", remaining,
                      "trial(s) still stand in the way.")

        elif choice == "0":
            print("You weigh anchor with", len(cleared), "of 5 trials cleared.")
            story.goodbye()
            return

        else:
            print("That's not an order I know, Captain.")


def main():
    while True:
        play()
        again = input("Play again? (y/n) ").lower().strip()
        if again != "y":
            story.goodbye()
            break


if __name__ == "__main__":
    main()

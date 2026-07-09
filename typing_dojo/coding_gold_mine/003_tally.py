# 🥋 Typing Dojo — Coding Gold Mine
# Engine 003: The Tally Machine
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   The Recycling Robot walks a salvage pile ONE item at a time and
#   tallies how many match what you asked for -- without ever using
#   the .count() shortcut. You watch the counter climb, just like the
#   guess-counter back in Chapter 6, only now it's walking a list.
#
# CS seeds: list * for-loop * == * counter / accumulation * counting without .count()
# First typeable at: Chapter 8 (The Recycling Robot).

pile = ["bottle", "wire", "bottle", "boot", "wire", "bottle", "can", "bottle"]
target = input("What should I count in the pile? ")

count = 0
for item in pile:
    if item == target:
        count = count + 1

print("I found", count, "of those.")

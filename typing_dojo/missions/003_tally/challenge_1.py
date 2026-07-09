# The Tally Machine

pile = ["bottle", "wire", "bottle", "boot", "wire", "bottle", "can", "bottle"]
target = input("What should I count in the pile? ")

count = 0
for item in pile:
    if item == target:
        count = count + 1

print("I found", count, "of those.")

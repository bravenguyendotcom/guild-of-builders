# 🎨 Pycasso's Advanced Gallery
# Showpiece 01: The Matrix Rain
#
# The canonical program (D-35). Written once; the "shown" debut in
# Chapter 13 draws its real output from this file. Standard library only.
#
# What it does:
#   Green characters cascade down the terminal, forever, on purpose.
#   The famous "hacker screen." Secretly it is four small ideas you
#   already half-know, stacked together:
#     1. a LIST that remembers how far each column has fallen
#     2. a little RANDOMNESS (which character, and when a drop restarts)
#     3. the LOOPS you already build every chapter
#     4. one new trick: CLEARING THE SCREEN between frames
#
# Skill-gated to Vol II (D-35): shown at Ch 13, fully buildable later.
#
# The knobs (Run it -> Hack it -> Own it):
#   CHARS   -> the alphabet the rain falls in  (the easiest, best first hack:
#              try "01" for pure binary rain, or your own symbols)
#   COLOR   -> change the green to any ANSI colour
#   HEIGHT  -> how tall the screen
#   WIDTH   -> fills the terminal automatically; set a number to force it

import random
import time
import shutil

COLOR  = "\033[92m"        # bright green  (try \033[96m cyan, \033[91m red)
RESET  = "\033[0m"
# WIDTH fills whatever screen you run it on — the rain reaches the horizon.
# (shutil asks the terminal how wide it is; falls back to 80 if it can't tell.)
WIDTH  = shutil.get_terminal_size(fallback=(80, 24)).columns
HEIGHT = 20
CHARS  = "0123456789ABCDEF@#$%&*+=-"

# One "drop position" per column: how far down that column has fallen.
# They start at random heights so the rain doesn't fall in a flat line.
drops = [random.randint(0, HEIGHT) for _ in range(WIDTH)]

def draw_frame():
    # \033[H moves the cursor home (top-left) instead of scrolling —
    # that is the "clear the screen" trick that makes it animate.
    screen = "\033[H"
    for row in range(HEIGHT):
        line = ""
        for col in range(WIDTH):
            if row == drops[col]:
                line += COLOR + random.choice(CHARS) + RESET
            elif row < drops[col] and row > drops[col] - 6:
                line += COLOR + random.choice(CHARS) + RESET
            else:
                line += " "
        screen += line + "\n"
    print(screen, end="")

def main(frames=100):
    print("\033[2J", end="")          # clear once at the start
    for _ in range(frames):
        draw_frame()
        for col in range(WIDTH):
            drops[col] += 1
            if drops[col] > HEIGHT + random.randint(0, 10):
                drops[col] = 0        # this column starts falling again
        time.sleep(0.06)
    print(RESET)

if __name__ == "__main__":
    main()

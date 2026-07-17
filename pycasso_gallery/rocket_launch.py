# 🎨 Pycasso's Advanced Gallery
# Showpiece 05: The Rocket Launch  🚀
#
# "Let your dreams lift off."
#
# The canonical program (D-35). Volume II's opening wonder beat: a rocket
# rises up the screen on a growing column of exhaust, after a countdown,
# and clears the top of the world.
#
# What it really is — four small ideas you (nearly) already have:
#   1. STRING ART      -- a rocket drawn as a few lines of text (a "sprite")
#   2. A MOVING NUMBER -- one variable: how high the rocket is. It goes up.
#   3. THE LOOPS       -- you've built these since Volume I
#   4. CLEARING THE SCREEN between frames, so fast it becomes motion
#
# Skill-gated to Vol II (D-35): shown at Vol II Ch 1, fully buildable as the
# volume goes on.
#
# The knobs (Run it -> Hack it -> Own it):
#   ROCKET   -> the ship itself. Redraw it. Make it yours.
#   FLAME    -> the characters the exhaust is made of
#   COLOR    -> any ANSI colour (try 96m cyan, 93m yellow, 95m magenta)
#   SPEED    -> seconds per frame (smaller = faster)
#   COUNTDOWN-> how many seconds before ignition

import time
import shutil
import random

COLOR   = "\033[93m"      # bright yellow flame (try \033[91m red, \033[96m cyan)
BODY    = "\033[97m"      # white rocket
RESET   = "\033[0m"
SPEED   = 0.08
COUNTDOWN = 3

# The rocket, drawn as string art. Each string is one line of the sprite.
ROCKET = [
    "  /\\  ",
    " |  | ",
    " |  | ",
    "/|##|\\",
    " /||\\ ",
]

FLAME = "^*'`."

size   = shutil.get_terminal_size(fallback=(80, 24))
WIDTH  = size.columns
HEIGHT = max(size.lines - 2, 18)      # use the whole terminal height
PAD    = max((WIDTH - 6) // 2, 0)     # centre the rocket


def clear():
    print("\033[2J", end="")


def home():
    print("\033[H", end="")


def draw_frame(altitude):
    """Draw one frame: sky, rocket at `altitude` rows up, exhaust below it."""
    rocket_top = HEIGHT - len(ROCKET) - altitude
    lines = []
    for row in range(HEIGHT):
        # is this row part of the rocket?
        if 0 <= row - rocket_top < len(ROCKET) and rocket_top >= 0:
            lines.append(" " * PAD + BODY + ROCKET[row - rocket_top] + RESET)
        # or part of the exhaust trail below it?
        elif row > rocket_top + len(ROCKET) - 1:
            flame = "".join(random.choice(FLAME) for _ in range(4))
            lines.append(" " * (PAD + 1) + COLOR + flame + RESET)
        else:
            lines.append("")
    home()
    print("\n".join(lines))


def countdown():
    clear()
    for n in range(COUNTDOWN, 0, -1):
        home()
        print("\n" * (HEIGHT // 2))
        print(" " * max(PAD - 2, 0) + COLOR + "  " + str(n) + "  " + RESET)
        time.sleep(0.7)
    home()
    print("\n" * (HEIGHT // 2))
    print(" " * max(PAD - 4, 0) + COLOR + " LIFTOFF! " + RESET)
    time.sleep(0.5)


def launch():
    countdown()
    clear()
    # The whole animation is ONE number going up.
    for altitude in range(0, HEIGHT + len(ROCKET) + 2):
        draw_frame(altitude)
        time.sleep(SPEED)
    clear()
    home()
    print(COLOR + "  ...and it's gone. 🚀" + RESET)
    print()
    print("  Your dreams lift off the same way:")
    print("  one small number, going up, every single frame.")
    print()


if __name__ == "__main__":
    launch()

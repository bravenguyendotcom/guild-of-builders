# 🥋 Typing Dojo — Coding Gold Mine
# Engine 008: The Sign Painter
#
# The canonical program. Written once; every mission that wears this
# engine improves when this file improves (D-21).
#
# What it does:
#   Paints a growing triangle out of whatever symbol you choose. range()
#   counts the rows for you -- 1, 2, 3, up to the height -- and "symbol * row"
#   repeats the symbol that many times to draw each line. Loops don't just
#   count anymore. Now they make pictures.
#
# CS seeds: range() * string repetition (symbol * n) * loops build shapes
# First typeable at: Chapter 13 (The Painter's Deck).

symbol = input("Paint with which symbol? ")
height = int(input("How tall? "))

for row in range(1, height + 1):
    print(symbol * row)

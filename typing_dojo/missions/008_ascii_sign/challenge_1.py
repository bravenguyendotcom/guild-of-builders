# The Sign Painter

symbol = input("Paint with which symbol? ")
height = int(input("How tall? "))

for row in range(1, height + 1):
    print(symbol * row)

"""
https://adventofcode.com/2021/day/2
"""

print("advent of code 2021 day 2, challenge 1")
print("--------------------------------------")

lines = []
with open(R"E:\Code\adventofcode\2021\2\input.txt", "r") as fileContent:
    lines = fileContent.readlines()

print("lineCount", len(lines))
lines = [line.rstrip("\n") for line in lines]

# TESTING
# lines = lines[:5]
# print(lines)

x = 0
y = 0
for line in lines:
    direction, count = line.split()
    count = int(count)
    if direction == "forward":
        x += count
    elif direction == "down":
        y += count
    elif direction == "up":
        y -= count
    else:
        print("MISSING: ", direction)

print("x=", x, " y=", y, " mul=", x * y)

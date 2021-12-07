"""
https://adventofcode.com/2021/day/3
"""

import pathlib
import sys

path = pathlib.Path(__file__).parent.resolve()
codeDay = int(path.parts[-1])
challengeNum = int(__file__[-4:-3])
print("advent of code 2021 day %d, challenge %d" % (codeDay, challengeNum))
print("--------------------------------------")

lines = []
with open(path.joinpath(R"input.txt"), "r") as fileContent:
    lines = fileContent.readlines()

print("lineCount read :", len(lines))
lines = [line.rstrip("\n") for line in lines]

# TESTING
# lines = lines[:10]
# print(lines)

bitCount = len(lines[0])
gamma = 0
epsilon = 0
for bitIndex in range(bitCount):
    print("linecount", len(lines))
    countOn = sum([1 if int(line, 2) & 1 << bitIndex else 0 for line in lines])
    on = countOn >= len(lines) / 2
    print("bit", bitIndex, "found", countOn, "/", len(lines), "bigger than", len(lines) / 2)
    print("bit:", format(1 << bitIndex, "b"), on)
    lines = [line for line in lines if (1 << bitIndex & int(line, 2) > 0 and on) or ~on]

    # print("line1", lines[0], format(on << bitIndex, "b"), format(on << bitIndex & int(lines[0], 2), "b"))
    # print("on << bitIndex", on << bitIndex)
    # print("^", bitIndex ^ int(lines[0], 2))

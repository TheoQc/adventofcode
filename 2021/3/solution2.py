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
# lines = lines[:30]
# print(lines)


def formatBin(val):
    if type(val) is str:
        val = int(val, 2)
    return format(val, "b").zfill(12)


originalLines = tuple(lines)

bitCount = len(lines[0])


def extract(originalLines, big):
    lines = originalLines
    print("entering big", big)
    for bitIndex in range(bitCount - 1, -1, -1):
        # for bitIndex in range(bitCount - 1, 9, -1):
        print("linecount current:", len(lines))
        countOn = sum([1 if int(line, 2) & 1 << bitIndex else 0 for line in lines])

        cutoff = len(lines) / 2
        on = countOn >= cutoff if big else countOn < cutoff
        print("bit", bitIndex + 1, "found:", countOn, "/", len(lines), "bigger than", cutoff)
        print("bit:", formatBin(1 << bitIndex), "", on)

        # for line in lines:
        #    a = 1 << bitIndex & int(line, 2)
        #    print(formatBin(1 << bitIndex), formatBin(line), formatBin(a), a > 0, a > 0 == on)

        lines = [line for line in lines if (1 << bitIndex & int(line, 2) > 0) == on]

        print("new lines len", len(lines))
        if len(lines) == 1:
            return int(lines[0], 2)


oxygen = extract(originalLines, True)
print("Oxygen =", oxygen)

co2 = extract(originalLines, False)
print("CO2 =", co2)

print("Total =", oxygen * co2)

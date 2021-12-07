"""
https://adventofcode.com/2021/day/4
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

originalLines = tuple(lines)

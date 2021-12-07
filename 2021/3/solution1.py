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
# lines = lines[:5]
# print(lines)

bitCount = len(lines[0])
gamma = 0
epsilon = 0
for bitIndex in range(bitCount):
    gammaBit = sum([1 if int(line, 2) & 1 << bitIndex else 0 for line in lines]) > len(lines) / 2

    if gammaBit:
        gamma |= 1 << bitIndex
    else:
        epsilon |= 1 << bitIndex

print("gamma", gamma, format(gamma, "b"))
print("epsilon ", epsilon, format(epsilon, "b"))
print("answer:", gamma * epsilon)
print("validated answer:", 2640986)

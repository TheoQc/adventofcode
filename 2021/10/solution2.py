"""
https://adventofcode.com/2021/
"""

from os import linesep
import pathlib
import sys
from collections import namedtuple

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    challengeNum = int(__file__[-4:-3])
    print("advent of code 2021 day %d, challenge %d" % (codeDay, challengeNum))
    print("--------------------------------------")


def GetMissing(line, pairs):
    line = line.rstrip("\n")
    line = [char for char in line]
    # open = tuple([p.open for p in pairs])
    # print(open)
    stack = []
    for char in line:
        if char in pairs.keys():
            stack.append(char)
            # print("stack:", stack)
        elif len(stack) and pairs[stack[-1]] == char:
            stack.pop()
            # print("stack:", stack)
        else:
            return []
    return stack


def main():
    Intro()

    testInput = False
    # testInput = True

    # Read file
    lines = []
    inputFilename = "testinput.txt" if testInput else "input.txt"
    with open(filepath.joinpath(inputFilename), "r") as fileContent:
        lines = fileContent.readlines()

    # TEST
    # lines = lines[:1]

    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {"(": 1, "[": 2, "{": 3, "<": 4}

    lineBefore = len(lines)
    # lines = [line for line in lines if GetCorruption(line, pairs) is None]
    # print("removed %d/%d corrupted lines" % (lineBefore - len(lines), lineBefore))

    lineScores = []
    for index, line in enumerate(lines):
        lineTotal = 0
        remain = GetMissing(line, pairs)
        # print(remain)
        for char in remain[::-1]:
            lineTotal = (lineTotal * 5) + points[char]
        print("line %d score: %d with %s" % (index, lineTotal, "".join(remain)))
        lineScores.append(lineTotal)

    lineScores = sorted([line for line in lineScores if line])

    middleIndex = int(len(lineScores) / 2)
    print(lineScores)
    print("there are %d scores, midle is %d with %d" % (len(lineScores), middleIndex, lineScores[middleIndex]))

    answer = 0
    answer = lineScores[middleIndex]
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
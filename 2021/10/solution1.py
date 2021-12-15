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


def GetCorruption(line, pairs):
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
            return char


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
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    total = 0
    for index, line in enumerate(lines):
        char = GetCorruption(line, pairs)
        if char:
            print("corruption on line %d %c" % (index, char))
            total = total + points[char]

    answer = 0
    answer = total
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
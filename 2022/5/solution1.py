"""
https://adventofcode.com/2022/
"""

from os import linesep
import pathlib
from collections import deque
import sys
from collections import namedtuple

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    challengeNum = int(__file__[-4:-3])
    print("advent of code 2022 day %d, challenge %d" % (codeDay, challengeNum))
    print("--------------------------------------")


def main():
    Intro()

    # ------------------------------------------------
    testInput = False
    testInput = True
    # ------------------------------------------------

    # Read file
    lines = []
    inputFilename = "testinput.txt" if testInput else "input.txt"
    with open(filepath.joinpath(inputFilename), "r") as fileContent:
        lines = fileContent.read()
    # =====================================
    # =====================================

    lines = lines.splitlines()

    lineIndex = 0
    isStacksDefinition = True
    stackCount = int((len(lines[0]) + 1) / len("[N] "))
    stacks = [deque() for _ in range(stackCount)]
    print(stacks)

    while isStacksDefinition:

        lineIndex += 1
        if lines[lineIndex][:2] == " 1":
            isStacksDefinition = False
            lineIndex += 2

    answer = 0
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
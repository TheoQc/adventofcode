"""
https://adventofcode.com/2022/
"""

from os import linesep
import pathlib
import sys
from collections import namedtuple

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    challengeNum = int(__file__[-4:-3])
    print("advent of code 2022 day %d, challenge %d" % (codeDay, challengeNum))
    print("--------------------------------------")


def GetScore(c):
    ascii = ord(c)
    if ascii >= ord("a"):
        return ascii - ord("a") + 1
    return ascii - ord("A") + 27


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
    total = 0
    lines = lines.splitlines()
    for i in range(int(len(lines) / 3)):
        j = i * 3
        for c in lines[j]:
            if c in lines[j + 1]:
                if c in lines[j + 2]:
                    total += GetScore(c)
                    break

    answer = total
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
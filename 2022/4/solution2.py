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


def IsContained(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]


def Overlap(r1, r2):
    return r1[1] >= r2[0] and r1[0] <= r2[1]


def main():
    Intro()

    # ------------------------------------------------
    testInput = False
    # testInput = True
    # ------------------------------------------------

    # Read file
    lines = []
    inputFilename = "testinput.txt" if testInput else "input.txt"
    with open(filepath.joinpath(inputFilename), "r") as fileContent:
        lines = fileContent.read()
    # =====================================
    # =====================================
    count = 0
    for l in lines.splitlines():
        p1, p2 = l.split(",")
        p1 = p1.split("-")
        p2 = p2.split("-")
        p1 = [int(c) for c in p1]
        p2 = [int(c) for c in p2]

        if Overlap(p1, p2):
            count += 1

    answer = count
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
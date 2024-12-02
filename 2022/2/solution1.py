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
    score = 0
    shapePoints = {"X": 1, "Y": 2, "Z": 3}
    matchSign = {"A": "X", "B": "Y", "C": "Z"}
    meLose = {"A": "Z", "B": "X", "C": "Y"}

    for l in lines.splitlines():
        other, me = l.split(" ")
        score += shapePoints[me]
        if matchSign[other] == me:
            score += 3
        elif meLose[other] != me:
            score += 6

    answer = score
    # answer = len(paths)
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
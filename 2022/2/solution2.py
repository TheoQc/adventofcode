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
    shapePoints = {"A": 1, "B": 2, "C": 3}
    outcomePoints = {"X": 0, "Y": 3, "Z": 6}

    matchSign = {"A": "X", "B": "Y", "C": "Z"}
    meLose = {"A": "C", "B": "A", "C": "B"}
    meWin = {k: v for k, v in zip(meLose.values(), meLose.keys())}

    for l in lines.splitlines():
        other, me = l.split(" ")
        score += outcomePoints[me]

        if me == "X":
            score += shapePoints[meLose[other]]
        elif me == "Y":
            score += shapePoints[other]
        else:
            score += shapePoints[meWin[other]]

    answer = score
    # answer = len(paths)
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
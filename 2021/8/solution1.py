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


class Digit:
    def __init__(self, string) -> None:
        self.letters = [c for c in string]

    def GetDigit(self):
        if len(self.letters) == 2:
            return 1
        elif len(self.letters) == 3:
            return 7
        elif len(self.letters) == 4:
            return 4
        elif len(self.letters) == 7:
            return 8
        return None


class Encoded:
    def __init__(self, tup) -> None:
        self.example = [Digit(elem) for elem in tup[0]]
        self.result = [Digit(elem) for elem in tup[1]]

    def __str__(self) -> str:
        return "from :" + str(self.example) + " to :" + str(self.result)


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
    # lines = lines[:2]

    lines = [line.replace("\n", "") for line in lines]
    lines = [line.replace(" | ", "|") for line in lines]
    lines = [line.split("|") for line in lines]
    lines = [((tuple(line[0].split())), tuple(line[1].split())) for line in lines]
    lines = [Encoded(line) for line in lines]

    # print(lines)
    count = sum(1 for line in lines for segments in line.result if segments.GetDigit())

    answer = count
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
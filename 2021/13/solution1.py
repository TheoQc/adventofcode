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


class Point:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def __repr__(self) -> str:
        return format("(%d,%d)" % (self.x, self.y))


class Paper:
    def __init__(self, coords) -> None:
        coords = [Point(*vals.split(",")) for vals in coords.split("\n")]
        maxSize = Point(max([pt.x for pt in coords]) + 1, max([pt.y for pt in coords]) + 1)
        print("max size:", maxSize)
        print(coords)
        self.size = maxSize
        self.grid = [[False for _ in range(0, maxSize.x)] for _ in range(0, maxSize.y)]

        for point in coords:
            self.AddPoint(point)
        # self.AddPoint(Point(2, 14))

    def __repr__(self) -> str:
        result = ""
        for y in range(0, self.size.y):
            result = result + "".join(["#" if pt else "." for pt in self.grid[y]])
            result = result + "\n"
        return result

    def AddPoint(self, point):
        print("addingPoint", point)
        self.grid[point.y][point.x] = True

    def Fold(self):
        pass


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

    coords, folds = lines.split("\n\n")
    paper = Paper(coords)
    print(paper)

    # TEST
    # lines = lines[:1]

    folds = folds.split("\n")
    folds = [words.split(" ")[-1].split("=") for words in folds]
    for fold in folds:
        paper.Fold(fold)

    answer = 0
    # answer = len(paths)
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
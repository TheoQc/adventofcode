"""
https://adventofcode.com/2021/
"""

from os import linesep
import pathlib
import sys
from collections import namedtuple
from functools import reduce
import operator

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    challengeNum = int(__file__[-4:-3])
    print("advent of code 2021 day %d, challenge %d" % (codeDay, challengeNum))
    print("--------------------------------------")


Point = namedtuple("Point", ["x", "y"])


class Board:
    def __init__(self, lines) -> None:
        lines = [line.rstrip("\n") for line in lines]
        lines = [[int(char) for char in line] for line in lines]
        self.width = len(lines[0])
        self.height = len(lines)
        print("map is %d X %d" % (self.width, self.height))
        self.lines = lines

    def __repr__(self) -> str:
        res = ""
        for y in range(0, self.height):
            # asStr = [str(num) for num in self.lines[y]]
            res = res + " ".join([str(num) for num in self.lines[y]]) + "\n"

        print(res)
        return res

    def GetLowPoints(self):
        lowPoints = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                current = self.lines[y][x]
                if y == 0 or self.lines[y - 1][x] > current:
                    if y == self.height - 1 or self.lines[y + 1][x] > current:
                        if x == 0 or self.lines[y][x - 1] > current:
                            if x == self.width - 1 or self.lines[y][x + 1] > current:
                                lowPoints.append((current, Point(x, y)))
                                print("found a low point %d at [%d,%d]" % (current, x, y))
        return tuple(lowPoints)

    def GetPoint(self, x, y):
        return (self.lines[y][x], Point(x, y))

    def GetConnected(self, lp, uniquePts):
        if lp[1] in uniquePts or self.lines[lp[1].y][lp[1].x] == 9:
            return [], uniquePts

        pts = [lp]
        uniquePts = tuple((*uniquePts, lp[1]))

        if lp[1].y > 0:
            newPts, uniquePts = self.GetConnected(self.GetPoint(lp[1].x, lp[1].y - 1), uniquePts)
            pts = pts + newPts

        if lp[1].y < self.height - 1:
            newPts, uniquePts = self.GetConnected(self.GetPoint(lp[1].x, lp[1].y + 1), uniquePts)
            pts = pts + newPts

        if lp[1].x > 0:
            newPts, uniquePts = self.GetConnected(self.GetPoint(lp[1].x - 1, lp[1].y), uniquePts)
            pts = pts + newPts

        if lp[1].x < self.width - 1:
            newPts, uniquePts = self.GetConnected(self.GetPoint(lp[1].x + 1, lp[1].y), uniquePts)
            pts = pts + newPts
        # print("getconnected", pts, uniquePts)
        return (pts, tuple(set(uniquePts)))


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

    board = Board(lines)
    print(board)

    lowPoints = board.GetLowPoints()
    print(lowPoints)

    # TEST
    # lowPoints = lowPoints[1:2]

    # uniquePts = [lp[1] for lp in lowPoints]
    uniquePts = ()
    poolSizes = []

    for index, lp in enumerate(lowPoints):
        poolPoints, newUniquePts = board.GetConnected(lp, uniquePts)
        uniquePts = tuple(set(uniquePts + newUniquePts))
        print("pool:%d numPts:%d sum:%d" % (index, len(poolPoints), sum([pt[0] for pt in poolPoints])))
        poolSizes.append(len(poolPoints))

    answer = 0
    answer = reduce(operator.mul, sorted(poolSizes, reverse=True)[:3])
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
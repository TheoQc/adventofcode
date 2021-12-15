"""
https://adventofcode.com/2021/day/5
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


Point = namedtuple("Point", ["x", "y"])


class Line:
    def __init__(self, inputString):
        ptFrom, _, ptTo = inputString.split()
        ptFrom = ptFrom.split(",")
        ptTo = ptTo.split(",")
        self.ptFrom = Point(int(ptFrom[0]), int(ptFrom[1]))
        self.ptTo = Point(int(ptTo[0]), int(ptTo[1]))

    def __str__(self) -> str:
        return str(format("from:%d,%d to:%d,%d" % (self.ptFrom[0], self.ptFrom[1], self.ptTo[0], self.ptTo[1])))

    def IsHoriz(self):
        return self.ptFrom.x == self.ptTo.x

    def IsVert(self):
        return self.ptFrom.y == self.ptTo.y

    def GetDelta(self):
        return (self.ptTo.x - self.ptFrom.x, self.ptTo.y - self.ptFrom.y)

    def IsStraight(self):
        return self.IsHoriz() or self.IsVert()

    def GetPoints(self):
        points = []
        if self.IsHoriz():
            fromP, toP = sorted((self.ptFrom.y, self.ptTo.y))
            for y in range(fromP, toP + 1):
                points.append(Point(self.ptFrom.x, y))
        elif self.IsVert():
            fromP, toP = sorted((self.ptFrom.x, self.ptTo.x))
            for x in range(fromP, toP + 1):
                points.append(Point(x, self.ptFrom.y))
        return tuple(points)


class Board:
    def __init__(self, maxSide):
        self.points = [[0 for x in range(maxSide)] for y in range(maxSide)]

    def __str__(self) -> str:
        res = ""
        for row in self.points:
            for point in row:
                res = res + (str(point) if point else ".")
            res = res + "\n"
        return res

    def AddPoint(self, pt):
        self.points[pt.y][pt.x] = self.points[pt.y][pt.x] + 1

    def GetBiggerThan(self, val):
        return sum([1 for row in self.points for pt in row if pt >= val])


def main():
    Intro()

    # Read file
    lines = []
    with open(filepath.joinpath(R"input.txt"), "r") as fileContent:
        # with open(filepath.joinpath(R"testinput.txt"), "r") as fileContent:
        lines = fileContent.readlines()

    # TEST
    # lines = lines[:2]

    lines = [Line(line) for line in lines]

    # Only straight lines
    prevcount = len(lines)
    lines = [line for line in lines if line.IsStraight()]
    print("Straight lines are now %d/%d" % (len(lines), prevcount))

    maxSide = 1000
    # maxSide = 10
    board = Board(maxSide)

    for line in lines:
        for pt in line.GetPoints():
            # print("adding pt", pt.x, pt.y)
            # board[pt.x][pt.y] = board[pt.x][pt.y] + 1
            board.AddPoint(pt)

    print(board)
    dangerous = board.GetBiggerThan(2)
    print("dangerous points found: %d/%d" % (dangerous, maxSide * maxSide))


if __name__ == "__main__":
    main()
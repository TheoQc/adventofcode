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


class Swarm:
    def __init__(self, lines) -> None:
        lines = [line.rstrip("\n") for line in lines]
        lines = [[int(char) for char in line] for line in lines]
        self.lines = lines
        self.iteration = 0
        self.size = len(lines)
        self.flash = 0
        print(self)

    def __repr__(self) -> str:
        string = ""
        for line in self.lines:
            string = string + " ".join([str(num) for num in line]) + "\n"
        return string

    def HasNeighbout(self, x, y):
        return (y > 0, x < self.size - 1, y < self.size - 1, x > 0)

    def Grow(self, x, y):
        val = self.lines[y][x]
        if val > 0 and val <= 9:
            self.lines[y][x] = val + 1

    def Distribute(self):
        atLeastOne = False
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.lines[y][x] > 9:
                    atLeastOne = True
                    self.flash = self.flash + 1
                    self.lines[y][x] = 0
                    top, right, bottom, left = self.HasNeighbout(x, y)
                    if top:
                        self.Grow(x, y - 1)
                        if left:
                            self.Grow(x - 1, y - 1)
                        if right:
                            self.Grow(x + 1, y - 1)
                    if bottom:
                        self.Grow(x, y + 1)
                        if left:
                            self.Grow(x - 1, y + 1)
                        if right:
                            self.Grow(x + 1, y + 1)
                    if right:
                        self.Grow(x + 1, y)
                    if left:
                        self.Grow(x - 1, y)

        if atLeastOne:
            # print(self)
            self.Distribute()

    def Tick(self):
        print("Tick", self.iteration + 1)
        self.iteration = self.iteration + 1
        for x in range(0, self.size):
            for y in range(0, self.size):
                self.lines[y][x] = self.lines[y][x] + 1
        # print(self)
        self.Distribute()
        # print(self)

    def IsSync(self):
        syncTo = self.lines[0][0]
        if all(syncTo == val for val in [digit for line in self.lines for digit in line]):
            # if all(row[0] == row for row in self.lines):
            return True
        return False


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

    swarm = Swarm(lines)
    for _ in range(0, 1000):
        swarm.Tick()
        if swarm.IsSync():
            break

    answer = 0
    answer = swarm.iteration
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
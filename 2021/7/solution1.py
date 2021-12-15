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
    def __init__(self, string) -> None:
        inputPos = string.split(",")
        inputPos = [int(p) for p in inputPos]
        self.max = max(inputPos) + 1
        positions = [0 for p in range(0, self.max)]
        for p in inputPos:
            positions[p] = positions[p] + 1
        self.positions = tuple(positions)
        print("input positions:", str(self.positions))

    def FuelForPos(self, index):
        if index < 0 or index > self.max:
            return None
        totalFuel = 0
        for i in range(0, self.max):
            totalFuel = totalFuel + (abs(index - i) * self.positions[i])
        return totalFuel

    def BestFuel(self):
        bestFuel = None
        for i in range(0, self.max):
            fuelForPos = self.FuelForPos(i)
            print("Fuel for pos %d is %d" % (i, fuelForPos))
            if bestFuel is None or fuelForPos < bestFuel:
                bestFuel = fuelForPos
        return bestFuel


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

    swarm = Swarm(lines[0])

    bestFuel = swarm.BestFuel()

    print("Final answer: %d" % (bestFuel))


if __name__ == "__main__":
    main()
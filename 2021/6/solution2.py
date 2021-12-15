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


class School:
    def __init__(self, vals) -> None:
        self.timers = tuple(vals)
        self.iteration = 0
        print("School initial timers:", self.timers)

    def Iterate(self):
        newVals = []
        self.iteration = self.iteration + 1
        for i in range(0, len(self.timers)):
            if self.timers[i] == 0:
                newVals.append(6)
                newVals.append(8)
            else:
                newVals.append(self.timers[i] - 1)
        self.timers = tuple(newVals)

    def Print(self):
        print("iteration %d:" % self.iteration, str(self.timers))

    def Result(self):
        print("After %d days there are %d fishes" % (self.iteration, len(self.timers)))


class School2:
    def __init__(self, vals) -> None:
        timers = [0 for i in range(0, 9)]
        for val in vals:
            timers[val] = timers[val] + 1
        self.timers = tuple(timers)
        self.iteration = 0
        print("School initial timers:", self.timers)

    def Iterate(self):
        newVals = [0 for i in range(0, 9)]
        self.iteration = self.iteration + 1

        for i in range(0, len(self.timers)):
            if i == 0:
                newVals[6] = newVals[6] + self.timers[i]
                newVals[8] = self.timers[i]
            else:
                newVals[i - 1] = newVals[i - 1] + self.timers[i]

        self.timers = tuple(newVals)

    def Print(self):
        print("iteration %d:" % self.iteration, str(self.timers))

    def Result(self):
        total = sum([fishes for fishes in self.timers])
        print("After %d days there are %d fishes" % (self.iteration, total))


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

    # school = School([int(timer) for timer in lines[0].split(",")])
    school = School2([int(timer) for timer in lines[0].split(",")])

    # iterations = 256
    iterations = 256
    for i in range(iterations):
        school.Iterate()
        # school.Print()

    school.Result()
    # print("Final answer: %d" % (len(school.timers)))


if __name__ == "__main__":
    main()
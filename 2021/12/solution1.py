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


class Cave:
    def __init__(self, name) -> None:
        self.name = name
        self.multiple = name.isupper()
        self.connections = []
        pass

    def __repr__(self) -> str:
        string = "cave:" + self.name
        string = string + " --> " + ",".join([con.name for con in self.connections])
        return string

    def AddConnection(self, cave):
        self.connections.append(cave)


def MakeSystem(lines):
    system = {}
    for line in lines:
        fromName, toName = line.rstrip("\n").split("-")

        fromCave = None
        toCave = None
        if fromName not in system:
            fromCave = Cave(fromName)
            system[fromName] = fromCave
        else:
            fromCave = system[fromName]
        if toName not in system:
            toCave = Cave(toName)
            system[toName] = toCave
        else:
            toCave = system[toName]

        fromCave.AddConnection(toCave)
        toCave.AddConnection(fromCave)
    return system


def GetPaths(fromNode, exclude):
    fullPaths = []
    if fromNode.name == "end":
        print("found end")
        fullPaths.append(tuple([fromNode]))
        return fullPaths

    if not fromNode.multiple:
        exclude = (*exclude, fromNode)
    for connection in fromNode.connections:
        if connection not in exclude:
            for subPath in GetPaths(connection, exclude):
                fullPaths.append((fromNode, *subPath))

    return tuple(fullPaths)


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

    system = MakeSystem(lines)

    print("Cave System:", system.values())

    paths = GetPaths(system["start"], ())
    for index, path in enumerate(paths):
        print("Path %d:" % index, ",".join([node.name for node in path]))

    answer = 0
    answer = len(paths)
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
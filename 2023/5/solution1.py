"""
https://adventofcode.com/2023/
"""

from os import linesep
import pathlib
import sys
from collections import namedtuple
import pprint

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    codeYear = int(filepath.parts[-2])
    challengeNum = int(__file__[-4:-3])
    print("advent of code %d day %d, challenge %d" % (codeYear, codeDay, challengeNum))
    print("--------------------------------------")

def GetVal(maps, fromCat, index):
    for c in maps.keys():
        if c[0]==fromCat:
            for source, dest in maps[c]:
                if (source == index):
                    return dest
    return index

def main():
    Intro()

    # ------------------------------------------------
    testInput = False
    #testInput = True
    # ------------------------------------------------

    # Read file
    lines = []
    inputFilename = "testinput.txt" if testInput else "input.txt"
    with open(filepath.joinpath(inputFilename), "r") as fileContent:
        lines = fileContent.read()
    # =====================================
    # =====================================

    seeds = ()
    maps = {}
    currentSection = ()
    for lineIndex, l in enumerate(lines.splitlines()):
        if not l:
            continue
        elif l.startswith('seeds:'):
            seeds = l.split(':')[1].split(' ')
            seeds = tuple(int(s) for s in seeds if s.isdigit())
        elif l[0].isdigit():
            dest, source, rangeNum = l.split(' ')
            for x in range(int(rangeNum)):                                
                maps[currentSection].append((int(source)+x, int(dest)+x))

        elif len(l)>0 and not l[0].isdigit() and not l[0]==' ':
            label = l.split(' ')[0].split('-')
            currentSection = (label[0], label[2])
            maps[currentSection] = []
    lowestLocation = 999999999999
    for seed in seeds:
        val = GetVal(maps, 'seed', seed)
        val = GetVal(maps, 'soil', val)
        val = GetVal(maps, 'fertilizer', val)
        val = GetVal(maps, 'water', val)
        val = GetVal(maps, 'light', val)
        val = GetVal(maps, 'temperature', val)
        val = GetVal(maps, 'humidity', val)
        val = GetVal(maps, 'location', val)
        lowestLocation = min(lowestLocation, val)
        

    answer = lowestLocation
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
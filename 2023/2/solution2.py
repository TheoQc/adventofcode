"""
https://adventofcode.com/2023/
"""

from os import linesep
import pathlib
import sys
from collections import namedtuple

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    codeYear = int(filepath.parts[-2])
    challengeNum = int(__file__[-4:-3])
    print("advent of code %d day %d, challenge %d" % (codeYear, codeDay, challengeNum))
    print("--------------------------------------")

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
    gameIndex = 0
    totalSum = 0
    for l in lines.splitlines():
        gameIndex +=1
        gameFailed = False
        games = l.split(":")[1]
        gameMax = {"red":0, "green":0, "blue":0}
        for g in games.split(';'):            
            
            for p in g.split(','):                                
                count, color = p.strip().split(' ')
                gameMax[color] = max(int(count), gameMax[color])
        totalSum += gameMax['red']*gameMax['green']*gameMax['blue']
                
    answer = totalSum
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
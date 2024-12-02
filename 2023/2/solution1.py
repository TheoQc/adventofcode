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

    maxVals = {"red":12, "green":13, "blue":14}
    goodGames = 0
    gameIndex = 0
    for l in lines.splitlines():
        gameIndex +=1
        gameFailed = False
        games = l.split(":")[1]
        for g in games.split(';'):            
            gameRes = {"red":0, "green":0, "blue":0}
            for p in g.split(','):                                
                count, color = p.strip().split(' ')
                gameRes[color] += int(count)
            for c, maxVal in maxVals.items():
                if gameRes[c] > maxVal:
                    gameFailed = True
        if not gameFailed:
            goodGames += gameIndex
                
    answer = goodGames
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
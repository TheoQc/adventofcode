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

    numCards = [0]  * 200
    for cardId, l in enumerate(lines.splitlines()):

        l= l.split(':')[1]
        numCards[cardId] += 1
        winNums, gameNums = l.split('|')
        print("card %d winnings:%s | gameNums:%s"%(cardId, str(winNums), str(gameNums)))
        winNums = list(int(x) for x in winNums.split(' ') if x.isdigit())
        gameNums = (int(x) for x in gameNums.split(' ') if x.isdigit())
        gamePoints = 0
        print(list(winNums))
        for t in gameNums:
            print(t)
            if t in winNums:
                gamePoints += 1
        for i in range(gamePoints):
            numCards[cardId+i+1] += numCards[cardId]
    

    print(numCards)
    totalCards = sum(numCards)
    answer = totalCards
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
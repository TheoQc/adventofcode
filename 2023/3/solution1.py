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


def GetLength(grid, x, y):
    length = 0
    for t in range(x, len(grid[0])):
        if grid[y][t].isdigit():
            length += 1
        else:
            break
    return length

def IsSymbol(c):
    return c is not '.' and not c.isdigit()

def GetNum(grid, x, y, numLength):
    sum = 0
    for v in range(numLength):        
        sum += (10**v)*int(grid[y][x+numLength-v-1])
    return sum

def EvalNum(grid, x, y, numLength):
    #test above
    found = False
    if y>0:
        for pos in range(max(x-1, 0), min(x+numLength+1, len(grid[0]))):
            if IsSymbol(grid[y-1][pos]):
                found = True
    
    #test left
    if x>0:
        if IsSymbol(grid[y][x-1]):
            found = True
    #test right
    if x+numLength<len(grid[0])-1:
        if IsSymbol(grid[y][x+numLength]):
            found = True
    #test below
    if y<len(grid)-1:
        for pos in range(max(x-1, 0), min(x+numLength+1, len(grid[0]))):
            if IsSymbol(grid[y+1][pos]):
                found = True
    if not found:
        print("not found for "+str(GetNum(grid, x, y, numLength)))
        return 0
    
    print("found for "+str(GetNum(grid, x, y, numLength)))
    
    return GetNum(grid, x, y, numLength)

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

    sumTouching = 0
    
    grid = []

    for y, l in enumerate(lines.splitlines()):
        grid.append([])
        for x, c in enumerate(l):
            grid[-1].append(c)

    width = len(grid[0])
    height = len(grid)
    print('Table is %d X %d' % (width, height))
    for y in range(height):
        x = 0
        while x < width:     
            numLength = 1
            if grid[y][x].isdigit():
                numLength = GetLength(grid, x, y)
                sumTouching += EvalNum(grid, x, y, numLength)
                
            x += numLength
        
            
    

                
    answer = sumTouching
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
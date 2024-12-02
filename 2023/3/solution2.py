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

def Getratios(grid, x, y):
    #test above
    print('testing %d %d'%(x, y))
    touching = []
    if y>0:
        for pos in range(max(x-1, 0), min(x+2, len(grid[0]))):
            print('look %d %d'%(pos, y-1))
            if grid[y-1][pos].isdigit():
                print('found')
                touching.append(int(grid[y-1][pos]))
    
    #test left
    if x>0:
        print('look %d %d'%(x-1, y))
        if grid[y][x-1].isdigit():
            print('found')
            touching.append(int(grid[y][x-1]))
    #test right
    if x<len(grid[0])-1:
        print('look %d %d'%(x+1, y))
        if grid[y][x+1].isdigit():
            print('found')
            touching.append(int(grid[y][x+1]))
    #test below
    if y<len(grid)-1:
        for pos in range(max(x-1, 0), min(x+2, len(grid[0]))):
            print('look %d %d'%(pos, y-1))
            if grid[y+1][pos].isdigit():
                print('found')
                touching.append(int(grid[y+1][pos]))
    if len(touching)==2:
        return touching[0]*touching[1]
    
    return 0

def main():
    Intro()

    # ------------------------------------------------
    testInput = False
    testInput = True
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
        for x in range(width):     
            if grid[y][x] == '*':
                sumTouching += Getratios(grid, x, y)
                
    answer = sumTouching
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
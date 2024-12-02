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

txtDigit = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def GetDigit(part):
    if part[0].isdigit():
        return int(part[0])
    for num, txt in enumerate(txtDigit):        
        if part[:len(txt)]==txt:
            print(str(num+1)+ " "+txt + " "+part[:len(txt)])
            return num+1
    return None

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
    total = 0
    lineNum = 0
    for l in lines.splitlines():
        lineNum +=1
        lineResult = 0
        for b in range(int(len(l))):
            val = GetDigit(l[b:])
            if val :
                lineResult = 10 * val
                #print(lineResult)
                break
        found = False
        for e in range(len(l)-1, -1 , -1):
            val = GetDigit(l[e:])
            if val :
                lineResult += val
                print(str(lineNum) + " : " + str(lineResult))
                total += lineResult
                Found = True
                break
        if not Found: 
            print("Not found : "+str(lineNum))
    answer = total
    # =====================================
    # =====================================
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
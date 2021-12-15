"""
https://adventofcode.com/2021/day/4
"""

from os import linesep
import pathlib
import sys

boardSide = 5
boardIndex = 0


class Board:
    def __init__(self, inputString):
        global boardIndex
        self.boardIndex = boardIndex
        boardIndex = boardIndex + 1
        lines = inputString.split("\n")
        for i in range(len(lines)):
            lines[i] = tuple(int(strVal) for strVal in lines[i].replace("  ", " ").lstrip().split(" "))
        self.lines = tuple(lines)
        self.rowDone = [0 for i in range(5)]
        self.colDone = [0 for i in range(5)]
        self.won = False

    def AddNum(self, number):
        if self.won:
            return False
        for i in range(boardSide):
            for j in range(boardSide):
                if self.lines[i][j] == number:
                    self.rowDone[i] = self.rowDone[i] + 1
                    self.colDone[j] = self.colDone[j] + 1
                    if self.rowDone[i] == boardSide or self.colDone[j] == boardSide:
                        print("board %d WON !!!!" % self.boardIndex)
                        print(self.rowDone)
                        print(self.colDone)
                        print(self)
                        self.won = True

                    # print("number %d found on board %d " % (number, self.boardIndex))
                    return self.won

    def GetScore(self, numSoFar):
        otherNum = [num for line in self.lines for num in line if num not in numSoFar]
        print(otherNum)
        return sum(otherNum)

    def __str__(self) -> str:
        return str("Board %d\nhoriz:%d, vert:%d\n" % (self.boardIndex, max(self.rowDone), max(self.colDone))) + str(
            self.lines
        )


def main():
    path = pathlib.Path(__file__).parent.resolve()
    codeDay = int(path.parts[-1])
    challengeNum = int(__file__[-4:-3])
    print("advent of code 2021 day %d, challenge %d" % (codeDay, challengeNum))
    print("--------------------------------------")

    sequence = []
    boards = []
    content = ""
    with open(path.joinpath(R"input.txt"), "r") as fileContent:
        content = fileContent.read()
    content = content.split("\n\n")
    sequence = tuple([int(strVal) for strVal in content[0].split(",")])
    boards = content[1:]

    # TEST
    # boards = content[1:5]
    # sequence = sequence[:25]

    print("playing with: %d boards and %d inputs" % (len(boards), len(sequence)))

    # print(boards[0])
    boards = [Board(inB) for inB in boards]
    # print(boards[0])
    # print(boards[0].rowDone)

    seqIndex = 0
    boardWin = 0
    for number in sequence:
        seqIndex = seqIndex + 1
        for board in boards:
            if board.AddNum(number):
                boardWin = boardWin + 1
                if boardWin == len(boards):
                    print("boards won", boardWin)
                    print("Game stopped at number %d/%d" % (seqIndex, len(sequence)))
                    numSofar = sequence[:seqIndex]
                    # print(numSofar)
                    boardScore = board.GetScore(numSofar)
                    print("board score:", boardScore)
                    print("last number", numSofar[-1])
                    print("result:", boardScore * numSofar[-1])
                    return None


if __name__ == "__main__":
    main()
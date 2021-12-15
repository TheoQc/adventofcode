"""
https://adventofcode.com/2021/
"""

from os import chdir, linesep
import pathlib
import sys
import pprint
from collections import namedtuple

filepath = pathlib.Path(__file__).parent.resolve()


def Intro():
    codeDay = int(filepath.parts[-1])
    challengeNum = int(__file__[-4:-3])
    print("advent of code 2021 day %d, challenge %d" % (codeDay, challengeNum))
    print("--------------------------------------")


"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


class Digit:
    def __init__(self, string) -> None:
        self.letters = [c for c in string]

    def GetDigit(self):
        if len(self.letters) == 2:
            return 1
        elif len(self.letters) == 3:
            return 7
        elif len(self.letters) == 4:
            return 4
        elif len(self.letters) == 5:
            return (2, 3, 5)
        elif len(self.letters) == 6:
            return (0, 6, 9)
        elif len(self.letters) == 7:
            return 8
        return None

    def __len__(self):
        return len(self.letters)

    def __repr__(self) -> str:
        return str("".join(sorted(self.letters)))

    def RemoveLetters(self, lettersToRemove):
        return tuple([letter for letter in self.letters if letter not in lettersToRemove])

    def GetLastLetter(self, lettersToRemove):
        lastLetter = [letter for letter in self.letters if letter not in lettersToRemove]
        if len(lastLetter) == 1:
            return lastLetter[0]
        return None

    def GetValue(self, cipher):
        decoded = set([cipher[letter] for letter in self.letters])

        print("from:", sorted(self.letters), "to:", sorted(decoded), "compareTo:", sorted(list("abdfge")))

        if decoded == set("cf"):
            return 1
        elif decoded == set("acdeg"):
            return 2
        elif decoded == set("acdfg"):
            return 3
        elif decoded == set("bdcf"):
            return 4
        elif decoded == set("abdfg"):
            return 5
        elif decoded == set("abdfge"):
            return 6
        elif decoded == set("acf"):
            return 7
        elif decoded == set("abcdefg"):
            return 8
        elif decoded == set("abdcfg"):
            return 9
        elif decoded == set("acfgeb"):
            return 0


class Encoded:
    def __init__(self, tup) -> None:
        self.example = [Digit(elem) for elem in tup[0]]
        self.result = [Digit(elem) for elem in tup[1]]

    def __repr__(self) -> str:
        return "from :" + str(self.example) + " to :" + str(self.result)

    def GetOfLength(self, num):
        return tuple([val for val in self.example if len(val) == num])

    def FindRemainingLetter(self, letters):
        for digit in self.GetOfLength(len(letters) + 1):
            remainder = digit.RemoveLetters(letters)
            if len(remainder) == 1:
                return remainder[0]
        return None

    def Solve(self):
        cipher = {}
        # find tup(c,f) (1)
        cf = self.GetOfLength(2)[0].letters
        print("cf:", cf)
        # FIND a (7 - (c,f))
        cipher["a"] = self.GetOfLength(3)[0].RemoveLetters(cf)[0]

        # find tup(b,d)(4) (len4 - (c,f))
        bd = self.GetOfLength(4)[0].RemoveLetters(cf)
        print("bd:", bd)

        # FIND g (len6 contains(abcdf)))
        # cipher['g'] = [letter for letters6 in self.GetOfLength(6) for letter in letters6 if letter
        abcdf = (cipher["a"], *cf, *bd)
        print("abcdf:", abcdf)
        cipher["g"] = self.FindRemainingLetter(abcdf)

        # FIND d (len(5) contains(agcf))
        agcf = (cipher["a"], cipher["g"], *cf)
        cipher["d"] = self.FindRemainingLetter(agcf)

        # FIND b (len(4) - (cfd))
        cfd = (*cf, cipher["d"])
        cipher["b"] = self.FindRemainingLetter(cfd)

        # FIND f (5) len5 contains(abdg)
        abdg = (cipher["a"], cipher["b"], cipher["d"], cipher["g"])
        cipher["f"] = self.FindRemainingLetter(abdg)

        # FIND c (1) len2 - f
        cf.remove(cipher["f"])
        cipher["c"] = cf[0]

        # FIND e last
        cipher["e"] = [letter for letter in ["a", "b", "c", "d", "e", "f", "g"] if letter not in cipher.values()][0]
        self.cipher = {v: k for k, v in cipher.items()}

        print("cipher :", self.cipher)

    def DeCipher(self, index):
        digit = self.result[index]
        # val = [self.cipher[letter] for letter in digit.letters]
        num = digit.GetValue(self.cipher)
        print("decipher from:", digit.letters, "to:", num)

        return num

    def GetResult(self):
        if not self.cipher:
            return None
        # self.DeCipher(1)
        val = 1000 * self.DeCipher(0) + 100 * self.DeCipher(1) + 10 * self.DeCipher(2) + self.DeCipher(3)
        return val


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

    lines = [line.replace("\n", "") for line in lines]
    lines = [line.replace(" | ", "|") for line in lines]
    lines = [line.split("|") for line in lines]
    lines = [((tuple(line[0].split())), tuple(line[1].split())) for line in lines]
    lines = [Encoded(line) for line in lines]

    # print(lines)

    total = 0
    for line in lines:
        print("examples:", line.example)
        line.Solve()
        if line.GetResult():
            total = total + line.GetResult()

    answer = total
    print("Final answer: %d" % (answer))


if __name__ == "__main__":
    main()
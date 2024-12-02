"""
https://adventofcode.com/2022/day/1
"""

import os

print("advent of code 2022 day 1, challenge 2")
print("--------------------------------------")

# need to be logged in to get url, too long from python
# urlContent = urllib.request.urlopen("https://adventofcode.com/2022/day/1/input")

path = os.path.split(__file__)[0] + "\\"
# inputFile = path + "test.txt"
inputFile = path + "input.txt"

lines = None

with open(inputFile) as f:
    lines = [line for line in f]

totals = []
currentVal = 0
for l in lines:
    if l == "\n":
        totals.append(currentVal)
        currentVal = 0
    else:
        currentVal += int(l)
totals.append(currentVal)
totals.sort()
print(sum(totals[-3:]))
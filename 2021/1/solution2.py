"""
https://adventofcode.com/2021/day/1
"""

from itertools import tee, islice, chain


def GetTriplets(iterableObj):
    prevs, items, nexts = tee(iterableObj, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)


print("advent of code 2021 day 1, challenge 2")
print("--------------------------------------")

lines = []
with open(R"E:\Code\adventofcode\2021\1\input.txt", "r") as inDepths:
    lines = inDepths.readlines()

depths = [int(depth.rstrip("\n")) for depth in lines]

# smaller test
# depths = depths[0:10]

prevDepth = -1
deeper = 0
for d1, d2, d3 in GetTriplets(depths):
    if d1 is None or d2 is None or d3 is None:
        continue
    tripletDepth = sum([d1, d2, d3])
    print(d1, " ", d2, " ", d3, " = ", tripletDepth)
    if prevDepth != -1 and tripletDepth > prevDepth:
        deeper += 1
    prevDepth = tripletDepth

print(deeper, " readings were deeper than the previous on a total of ", len(depths), " readings")

"""
https://adventofcode.com/2021/day/1
"""

print("advent of code 2021 day 1, challenge 1")
print("--------------------------------------")

# need to be logged in to get url, too long from python
# urlContent = urllib.request.urlopen("https://adventofcode.com/2021/day/1/input")

lines = []
with open(R"E:\Code\adventofcode\2021\1\input.txt", "r") as inDepths:
    lines = inDepths.readlines()

depths = [int(depth.rstrip("\n")) for depth in lines]

# smaller test
# depths = depths[0:5]

prev = depths[0]
deeper = 0
for depth in depths:
    print(depth)
    if depth > prev:
        deeper += 1
    prev = depth

print(deeper, " readings were deeper than the previous on a total of ", len(depths), " readings")

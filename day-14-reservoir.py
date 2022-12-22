from utils import fetchInput
import re


# page = fetchInput("https://adventofcode.com/2022/day/14/input")
# text_data = page.text

text_data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

text_lines = list(re.split('\n', text_data.strip()))

string_coords = list(map(lambda x: x.split(' -> '), text_lines))
coords = []
minX = float("inf")
minY = float("inf")
maxX = 0
maxY = 0
mapPlot = []

for path in string_coords:
    p = []
    for coord in path:
        nums = list(map(int, coord.split(',')))
        maxX = max(maxX, nums[0])
        maxY = max(maxY, nums[1])
        minX = min(minX, nums[0])
        minY = min(minY, nums[1])
        p.append(nums)
    coords.append(p)


# define sand source
source = [500,0]
maxX = max(source[0], maxX)
minX = min(source[0], minX)
maxY = max(source[1], maxY)
minY = min(source[1], minY)

for row in range(minY, maxY+1):
    newRow = ["."]*(maxX+1 - minX)
    mapPlot.append(newRow)


def setPoint(c, string="#"):
    mapPlot[c[1] - minY][c[0] - minX] = string


def stepForward(point, goal):
    nxt = point
    if point[0] < goal[0]:
        nxt[0] = point[0]+1
    elif point[0] > goal[0]:
        nxt[0] = point[0]-1
    if point[1] < goal[1]:
        nxt[1] = point[1]+1
    elif point[1] > goal[1]:
        nxt[1] = point[1]-1
    return nxt


for path in coords:
    last = []
    for c in path:
        setPoint(c)
        if last:
            step = stepForward(last, c)
            while step != c:
                print(step)
                setPoint(step)
                step = stepForward(step, c)
        last = c

setPoint(source, '+')

for r in mapPlot:
    for c in r:
        print(c, end="")
    print('')

from utils import fetchInput
import re

page = fetchInput("https://adventofcode.com/2022/day/9/input")
text_data = page.text
# test/example
# text_data = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# """
ROPE_LENGTH = 10
text_rows = list(re.split('\n', text_data.strip()))
rope = []
for x in range(10):
    rope.append([0,0])
print(rope)
tail_history = ['0,0']


def moveKnot(knot, x, y, i):
    knot[0] = knot[0] + x
    knot[1] = knot[1] + y
    if i == (len(rope) - 1):
        tail_history.append(','.join(str(n) for n in knot))
    return knot


def updateKnots():
    for i in range(len(rope)-1):
        xDiff = rope[i][0] - rope[i+1][0]
        yDiff = rope[i][1] - rope[i+1][1]
        if (xDiff + yDiff) >= 3:  # NE
            rope[i+1] = moveKnot(rope[i+1], 1, 1, i+1)
        elif (xDiff - yDiff) >= 3:  # SE
            rope[i+1] = moveKnot(rope[i+1], 1, -1, i+1)
        elif (xDiff - yDiff) <= -3:  # NW
            rope[i+1] = moveKnot(rope[i+1], -1, 1, i+1)
        elif (xDiff + yDiff) <= -3:  # SW
            rope[i+1] = moveKnot(rope[i+1], -1, -1, i+1)
        elif xDiff > 1:
            rope[i+1] = moveKnot(rope[i+1], 1, 0, i+1)
        elif xDiff < -1:
            rope[i+1] = moveKnot(rope[i+1], -1, 0, i+1)
        elif yDiff > 1:
            rope[i+1] = moveKnot(rope[i+1], 0, 1, i+1)
        elif yDiff < -1:
            rope[i+1] = moveKnot(rope[i+1], 0, -1, i+1)


# Simulate moves
for step_str in text_rows:
    step = step_str.split()
    transform = [0,0];
    # Parse steps
    if step[0] == 'U':
        transform[1] = int(step[1])
    elif step[0] == 'D':
        transform[1] = int(step[1])*-1
    elif step[0] == 'L':
        transform[0] = int(step[1])*-1
    elif step[0] == 'R':
        transform[0] = int(step[1])
    # Handle x (L-R)
    for move in range(abs(transform[0])):
        rope[0][0] = rope[0][0] + transform[0]/abs(transform[0])
        updateKnots()
    # Handle y (U-D)
    for move in range(abs(transform[1])):
        rope[0][1] = rope[0][1] + transform[1]/abs(transform[1])
        updateKnots()

print(rope)
positions = set(tail_history)
print(f'Unique tail positions: {len(positions)}')

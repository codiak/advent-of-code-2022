from utils import fetchInput
import re
from string import ascii_lowercase
from copy import copy
import sys
import time


text_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

page = fetchInput("https://adventofcode.com/2022/day/12/input")
text_data = page.text


map_rows = list(re.split('\n', text_data.strip()))
map_data = text_data.replace('\n', '')
map_h = len(map_rows)
map_w = len(map_rows[0])
map_points = []
start_i = 0


class Point(object):
    def __init__(self, h, up, down, left, right,
                 is_start=False, is_goal=False):
        self.h = h
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.is_start = is_start
        self.is_goal = is_goal

    def __str__(self):
        return f'<Point> h: {self.h} u:{self.up} d:{self.down} l:{self.left} r:{self.right}'


def get_i(map_w, y, x):
    return (map_w*y) + x


def get_h(map_w, y, x, i):
    letter = map_data[i]
    h = 0
    if letter == 'S':
        h = 0
    elif letter == 'E':
        h = 25
    else:
        h = ascii_lowercase.index(letter)
    return h


def can_go_h(current_h, next_i):
    next_h = get_h(map_w, y, x, next_i)
    if next_h <= (current_h+1):
        return True
    else:
        return False


# build map
for y in range(map_h):
    for x in range(map_w):
        i = get_i(map_w, y, x)
        h = get_h(map_w, y, x, i)
        up = None
        down = None
        left = None
        right = None
        s = (map_data[i] == 'S')
        g = (map_data[i] == 'E')
        if s:
            start_i = i
        if i >= map_w:
            ui = get_i(map_w, y-1, x)
            if can_go_h(h, ui):
                up = ui
        if i+1 <= (map_h-1) * map_w:
            di = get_i(map_w, y+1, x)
            if can_go_h(h, di):
                down = di
        if i % map_w != 0:
            li = i-1
            if can_go_h(h, li):
                left = li
        if (i+1) % map_w != 0 or i==0:
            ri = i+1
            if can_go_h(h, ri):
                right = ri
        map_points.append(Point(h, up, down, left, right, is_start=s, is_goal=g))


def check_next(i, steps_so_far, node_queue, steps_to_i, paths):
    # print(f'checking: {i}')  # debug
    point = map_points[i]

    if point.is_goal:
        print('Found goal!')
        print(len(steps_so_far))
        paths.append(len(steps_so_far))

    if point.up != None:
        steps = copy(steps_so_far)
        steps.append(point.up)
        if point.up not in steps_to_i or len(steps) < steps_to_i[point.up]:
            steps_to_i[point.up] = len(steps)
            node_queue.append((point.up, steps))
    if point.down != None:
        steps = copy(steps_so_far)
        steps.append(point.down)
        if point.down not in steps_to_i or len(steps) < steps_to_i[point.down]:
            steps_to_i[point.down] = len(steps)
            node_queue.append((point.down, steps))
    if point.left != None:
        steps = copy(steps_so_far)
        steps.append(point.left)
        if point.left not in steps_to_i or len(steps) < steps_to_i[point.left]:
            steps_to_i[point.left] = len(steps)
            node_queue.append((point.left, steps))
    if point.right != None:
        steps = copy(steps_so_far)
        steps.append(point.right)
        if point.right not in steps_to_i or len(steps) < steps_to_i[point.right]:
            steps_to_i[point.right] = len(steps)
            node_queue.append((point.right, steps))


def find_shortest_climb(start):
    steps_to_i = {start:0}
    successful_paths = []
    node_queue = [(start, [start])]
    start = time.time()

    while node_queue:
        tuple = node_queue.pop(0)
        check_next(tuple[0], tuple[1], node_queue, steps_to_i, successful_paths)

    print(f'Completed in: {time.time() - start}s')
    if successful_paths:
        return min(successful_paths) - 1
    else:
        print(f'No paths from {start} found!')
        return None

# Part I
shortest = find_shortest_climb(start_i)
print(f'Successful: {shortest}')

# Part II
dists_from_lowest = []
for i, p in enumerate(map_points):
    if p.h == 0:
        dist = find_shortest_climb(i)
        if dist:
            dists_from_lowest.append(dist)
print(f'Shortest from lowest: {min(dists_from_lowest)}')

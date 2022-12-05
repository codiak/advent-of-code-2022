from utils import fetchInput
import re
import queue

page = fetchInput("https://adventofcode.com/2022/day/5/input")
text_data = page.text
text_rows = list(re.split('\n', text_data))

stacks = []
# 9 stacks formatted as:
# ...
# [B] [J] [V] [L] [V] [G] [L] [N] [J]
#  1   2   3   4   5   6   7   8   9
for i in range(9):
    stacks.append(queue.LifoQueue())

# first 8 rows are initial state
for row_i, stack in enumerate(text_rows[0:8][::-1]):
    for i in range(9):
        char_i = (i*4)+1
        if char_i < len(stack):
            ltr = stack[char_i]
            if ltr and ltr != " ":
                stacks[i].put(ltr)

# follow instructions
for step in text_rows[10:-1]:
    parsed = step.split()
    n = int(parsed[1])
    a = int(parsed[3]) - 1
    b = int(parsed[5]) - 1
    # move n from a to b
    for k in range(n):
        if not stacks[a].empty():
            item = stacks[a].get()
            stacks[b].put(item)

# Part 1 solution:
for stack in stacks:
    print(list(stack.queue)[0])

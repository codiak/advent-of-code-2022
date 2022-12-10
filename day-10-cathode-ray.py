from utils import fetchInput
import re

page = fetchInput("https://adventofcode.com/2022/day/10/input")
text_data = page.text
text_rows = list(re.split('\n|\s', text_data.strip()))

cycle = 0
x = 1
add_next = False
strength_hist = []

while text_rows:
    cycle += 1
    inst = text_rows.pop(0)
    # During cycle
    if (cycle + 20) % 40 == 0:
        # signal strength = cycle number * value of the X register
        strength = cycle * x
        strength_hist.append(strength)
    # After cycle
    if inst == 'addx':
        add_next = True
    elif add_next:
        add_next = False
        x += int(inst)

print(strength_hist)
print(sum(strength_hist))

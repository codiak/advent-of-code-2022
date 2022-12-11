from utils import fetchInput
import re


def renderSignal(text_rows):
    cycle = 0
    x = 1
    add_next = False
    strength_hist = []

    print('\n')

    while text_rows:
        cycle += 1
        inst = text_rows.pop(0)
        # During - signal strength
        if (cycle+20) % 40 == 0:
            # Part I
            # signal strength = cycle number * value of the X register
            strength_hist.append(cycle * x)
        # During - render
        pos = (cycle-1) % 40
        if pos-1 <= x and pos+1 >= x:
            # print lit pixel in green
            print('\33[31m#\33[0m', end="")
        else:
            print('.', end="")
        if pos == 39:
            print(' ')
        # After cycle
        if inst == 'addx':
            add_next = True
        elif add_next:
            add_next = False
            x += int(inst)

    print('\n')
    print('Part I:')
    print(strength_hist)
    print(sum(strength_hist))


if __name__ == "__main__":
    page = fetchInput("https://adventofcode.com/2022/day/10/input")
    text_data = page.text
    text_rows = list(re.split('\n|\s', text_data.strip()))
    renderSignal(text_rows)

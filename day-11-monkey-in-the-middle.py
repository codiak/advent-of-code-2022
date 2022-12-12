from utils import fetchInput
import re
from typing import List
import numpy as np
from math import lcm
from copy import copy

page = fetchInput("https://adventofcode.com/2022/day/11/input")
text_data = page.text
text_rows = list(re.split('\n', text_data.strip()))


class Monkey(object):
    def __init__(self, no, items, op, op_val, div_test, true_to, false_to):
        self.no = no
        self._items = items
        self.op_val = op_val
        self.div_test = div_test
        self.true_to = true_to
        self.false_to = false_to
        self.inspect_count = 0
        self.op = None
        if op == 'times':
            self.op = lambda x: np.multiply(x, self.op_val)
        elif op == 'square':
            self.op = lambda x: np.square(x)
        elif op == 'add':
            self.op = lambda x: np.add(x, self.op_val)

    def __str__(self):
        return f'Monkey {self.no}: {self._items}\n Inspected: {self.inspect_count}'

    def get_items(self):
        return self._items

    def pop_item(self):
        self.inspect_count += 1
        return self._items.pop(0)

    def catch_item(self, item):
        self._items.append(item)


monkeys: List[Monkey] = []
monkey_i = 0
monkey_params = []
dividers = []

# set up
for row in text_rows:
    string = row.strip()
    if re.match("^Monkey", string):
        no = string[7:-1]
        monkey_params.append(no)
    elif re.match("^Starting items", string):
        items = string[16:].split(', ')
        monkey_params.append(list(map(int, items)))
    elif re.match("^Operation", string):
        opStr = string[17:]
        op = opStr
        op_val = None
        if re.match("old \* old", opStr):
            op = 'square'
        elif re.match("old \*", opStr):
            op_val = copy(int(opStr[6:]))
            op = 'times'
        elif re.match("old \+", opStr):
            op_val = copy(int(opStr[6:]))
            op = 'add'
        else:
            raise ValueError(f'Unhandled operation {opStr}')
        monkey_params.append(op)
        monkey_params.append(op_val)
    elif re.match("^Test\: divisible", string):
        div_test = int(string[19:])
        dividers.append(div_test)
        monkey_params.append(div_test)
    elif re.match("If true\: throw to monkey", string):
        true_to = int(string[25:])
        monkey_params.append(true_to)
    elif re.match("If false\: throw to monkey", string):
        false_to = int(string[26:])
        monkey_params.append(false_to)
        # Should have all params now!
        monkeys.append(Monkey(*monkey_params))
        monkey_params = []
        monkey_i += 1

least_multiple = lcm(*dividers)


# @profile  # using line_profiler to optimize
def runRounds(n):
    for r in range(n):
        for m in monkeys:
            while m.get_items():
                item = m.pop_item()
                # Inspection
                item = m.op(item)
                # print(type(item))
                # item = math.floor(item/3)  # Part I
                item = item % least_multiple
                # Throw based on worry, run test
                if item % m.div_test:
                    monkeys[m.false_to].catch_item(item)
                else:
                    monkeys[m.true_to].catch_item(item)


runRounds(10000)

inspections = []
for m in monkeys:
    print(m)
    inspections.append(m.inspect_count)
inspections.sort(reverse=True)

print(f'Monkey business: {inspections[0]*inspections[1]}')

from utils import fetchInput
import re
from typing import List
import math
from copy import copy

# page = fetchInput("https://adventofcode.com/2022/day/11/input")
# text_data = page.text

text_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

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
            self.op = lambda x: x*self.op_val
        elif op == 'square':
            self.op = lambda x: x*x
        elif op == 'add':
            self.op = lambda x: x+self.op_val

    def __str__(self):
        return f'Monkey {self.no}: {self._items}\n Inspected: {self.inspect_count}'

    def items(self):
        return self._items

    def get_item(self):
        self.inspect_count += 1
        return self._items.pop(0)

    def catch_item(self, item):
        self._items.append(item)

    # def op(self):
    #     return self._op


monkeys: List[Monkey] = []
monkey_i = 0
monkey_params = []

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
            op_val = int(opStr[6:])
            op = 'times'
        elif re.match("old \+", opStr):
            op_val = int(opStr[6:])
            op = 'add'
        else:
            raise ValueError(f'Unhandled operation {opStr}')
        monkey_params.append(op)
        monkey_params.append(op_val)
    elif re.match("^Test\: divisible", string):
        div_test = int(string[19:])
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


# @profile
def runRounds(n):
    for r in range(n):
        for m in monkeys:
            while m.items():
                old = m.get_item()
                # Inspection
                # run operation on first item
                # eval(m.op) -> lprof: takes 67.5% of runtime
                # new = eval(m.op)
                new = m.op(old)
                print(f'{old} -> {m.no}\'s func = {new}')
                # divide worry by 3 - not damaged!
                # print(f'{old}, {new}')
                new = math.floor(new/3)
                # Throw based on worry
                # run test
                if new % m.div_test:
                    monkeys[m.false_to].catch_item(new)
                else:
                    monkeys[m.true_to].catch_item(new)

runRounds(20)

print(f'\nAfter:')
inspections = []
monkey_business = 1
for m in monkeys:
    print(m)
    inspections.append(m.inspect_count)
    # monkey_business = monkey_business * m.inspect_count
inspections.sort(reverse=True)
print(f'Monkey business: {inspections[0]*inspections[1]}')

op = lambda x: x*x
print(op(10))

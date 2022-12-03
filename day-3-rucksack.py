from utils import fetchInput
import re
from string import ascii_lowercase, ascii_uppercase

# list of all of the items currently in each rucksack
page = fetchInput("https://adventofcode.com/2022/day/3/input")
text_data = page.text
rucksacks = list(filter(None, text_data.split('\n')))
# first half, first compartment...
to_rearrange = []

for rucksack in rucksacks:
    half = len(rucksack)//2
    comp1 = rucksack[0:half]
    comp2 = rucksack[half:len(rucksack)]
    # Find intersection of characters
    to_rearrange.append(re.sub(f'[^{comp1}]', '', comp2))
# print(to_rearrange)

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

priority_str = ascii_lowercase + ascii_uppercase
priority_sum = 0

for item in to_rearrange:
    # score for first, and only, shared letter
    priority_sum = priority_sum + 1 + priority_str.index(item[0])

print(f'Total priority: {priority_sum}')

# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types


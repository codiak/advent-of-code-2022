from utils import fetchInput
import re
from string import ascii_lowercase, ascii_uppercase
from itertools import islice

# list of all of the items currently in each rucksack
page = fetchInput("https://adventofcode.com/2022/day/3/input")
text_data = page.text
rucksacks = list(filter(None, text_data.split('\n')))
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
priority_str = ascii_lowercase + ascii_uppercase
priority_sum = 0

for rucksack in rucksacks:
    # first half, first compartment...
    half = len(rucksack)//2
    comp1 = rucksack[0:half]
    comp2 = rucksack[half:len(rucksack)]
    # Find intersection of characters
    to_rearrange = re.sub(f'[^{comp1}]', '', comp2)[0]
    # Score for first, and only, shared letter
    priority_sum = priority_sum + 1 + priority_str.index(to_rearrange)

print(f'Total priority: {priority_sum}')

# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types
def chunks(iterable, size):
    """Generate adjacent chunks of data"""
    it = iter(iterable)
    return iter(lambda: tuple(islice(it, size)), ())

elf_groups = list(chunks(rucksacks, 3))
group_sum = 0

for sacks in elf_groups:
    # Find first intersection of characters
    inter1 = re.sub(f'[^{sacks[0]}]', '', sacks[1])
    group_priority = re.sub(f'[^{inter1}]', '', sacks[2])[0]
    group_sum = group_sum + 1 + priority_str.index(group_priority)

print(f'Group sum priorities: {group_sum}')

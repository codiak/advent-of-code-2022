from utils import fetchInput
import re
import math

page = fetchInput("https://adventofcode.com/2022/day/4/input")
text_data = page.text

# Elf -> range of ids
# example_txt = """5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""

ranges = list(re.split('\n|,', text_data.strip()))

def stringRangeToTuple(range: str) -> tuple:
    str_arr = range.split('-')
    return (int(str_arr[0]), int(str_arr[1]))

def contains(a, b):
    if a[0] <= b[0] and a[1] >= b[1]:
        return True
    else:
        return False

def overlaps(a, b):
    if a[0] >= b[0] and a[0] <= b[1]:
        return True
    elif a[1] >= b[0] and a[1] <= b[1]:
        return True
    else:
        return False

num_pairs = math.floor(len(ranges)/2)
contained_count = 0
overlap_count = 0

for x in range(num_pairs):
    idx = x*2
    r1 = stringRangeToTuple(ranges[idx])
    r2 = stringRangeToTuple(ranges[idx+1])
    if contains(r1, r2) or contains(r2, r1):
        contained_count = contained_count + 1
    elif overlaps(r1, r2) or overlaps(r2, r1):
        overlap_count = overlap_count + 1
# Include contains in overlap
overlap_count = overlap_count + contained_count

print(f'Contained ranges: {contained_count}')
print(f'Overlapping ranges: {overlap_count}')

from utils import fetchInput
import re
from functools import cmp_to_key

page = fetchInput("https://adventofcode.com/2022/day/13/input")
text_data = page.text

text_lines = list(re.split('\n\n|\n', text_data.strip()))
packets = list(map(eval, text_lines))


def checkPacketsOrder(l, r):
    # if only one value is an integer, convert to list, then compare
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]
    if len(l) == 0 and len(r) > 0:
        # left ran out by being empty
        return 1

    for i, l_item in enumerate(l):
        r_item = 0
        if i == len(r):
            # right ran out
            return -1
        else:
            r_item = r[i]

        if isinstance(l_item, int) and isinstance(r_item, int):
            if l_item != r_item:
                # if integer, L < R
                if l_item < r_item:
                    return 1
                else:
                    return -1
        else:
            inner_check = checkPacketsOrder(l_item, r_item)
            if inner_check in [1,-1]:
                return inner_check

        if i+1 == len(l) and i+1 < len(r):
            # left going to run out
            return 1
    return 0


# Part I
ordered_i_sum = 0
for pair_i in range(0, len(packets)-1, 2):
    left = packets[pair_i]
    right = packets[pair_i+1]
    compare = checkPacketsOrder(left, right)
    packet_i = int((pair_i/2)+1)
    if compare == 1:
        print(f'{packet_i} is ORDERED')
        ordered_i_sum += packet_i
    else:
        print(f'{packet_i} is NOT ORDERED')
print(f'Indices sum: {ordered_i_sum}')

# Part II
packets.extend([[[2]],[[6]]])  # divider packets
sorted_packets = sorted(packets, key=cmp_to_key(checkPacketsOrder), reverse=True)
divOnei = sorted_packets.index([[2]])+1
divTwoi = sorted_packets.index([[6]])+1
print(f'Decoder key: {divOnei * divTwoi}')

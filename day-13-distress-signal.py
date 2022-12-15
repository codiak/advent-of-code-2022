from utils import fetchInput
import re

page = fetchInput("https://adventofcode.com/2022/day/13/input")
text_data = page.text

# text_data = """
# [1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# """

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
        return True

    for i, l_item in enumerate(l):
        r_item = None
        if i == len(r):
            # right ran out
            return False
        else:
            r_item = r[i]

        if isinstance(l_item, int) and isinstance(r_item, int):
            if l_item != r_item:
                # if integer, L < R
                return l_item < r_item
        else:
            inner_check = checkPacketsOrder(l_item, r_item)
            if inner_check != None:
                return inner_check

        if i+1 == len(l) and i+1 < len(r):
            # left going to run out
            return True
    return None


ordered_i_sum = 0
for pair_i in range(0, len(packets)-1, 2):
    left = packets[pair_i]
    right = packets[pair_i+1]
    compare = checkPacketsOrder(left, right)
    packet_i = int((pair_i/2)+1)
    if compare == True:
        print(f'{packet_i} is ORDERED')
        ordered_i_sum += packet_i
    else:
        print(f'{packet_i} is NOT ORDERED')

print(f'Indices sum: {ordered_i_sum}')

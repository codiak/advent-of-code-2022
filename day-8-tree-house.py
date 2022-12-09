from utils import fetchInput
import re
import numpy as np


page = fetchInput("https://adventofcode.com/2022/day/8/input")
text_data = page.text

# Test Data
# text_data = """30373111
# 25512151
# 65332111
# 33549118
# 35390111"""

text_rows = list(re.split('\n', text_data.strip()))
maxYi = len(text_rows) - 1
maxXi = len(text_rows[0]) - 1
visCount = 0

data_arr = np.zeros((maxYi+1, maxXi+1), dtype=np.int8)
view_score = np.zeros((maxYi+1, maxXi+1), dtype=np.int32)

# build 2d array
for x, row in enumerate(text_rows):
    for y, char in enumerate(row):
        data_arr[x, y] = int(char)

print(f'Processing data with shape {data_arr.shape}...')
# iterate over array once
for y, row in enumerate(data_arr):
    for x, tree in enumerate(row):
        maxL = -1; maxR = -1; maxU = -1; maxD = -1
        viewL = 0; viewR = 0; viewU = 0; viewD = 0
        # Skip edges
        if 0 in [x, y] or y == maxYi or x == maxXi:
            visCount += 1
            # view score defaults to zero
            continue
        # Set Up max
        if y == 1:
            maxU = data_arr[:, x][y-1]
            viewU = 1
        else:
            maxU = max(data_arr[:, x][0:y])
            for t in data_arr[:, x][0:y][::-1]:
                viewU += 1
                if t >= tree:
                    break
        # Set Left max
        if x == 1:
            maxL = row[0]
            viewL = 1
        else:
            maxL = max(row[0:x])
            for t in row[0:x][::-1]:
                viewL += 1
                if t >= tree:
                    break
        # Set Down max
        if y+1 == maxYi:
            maxD = data_arr[:, x][y+1]
            viewD = 1
        else:
            maxD = max(data_arr[:, x][y+1:maxYi+1])
            for t in data_arr[:, x][y+1:maxYi+1]:
                viewD += 1
                if t >= tree:
                    break
        # Set Right max
        if x+1 == maxXi:
            maxR = row[x+1]
            viewR = 1
        else:
            maxR = max(row[x+1:maxXi+1])
            for t in row[x+1:maxXi+1]:
                viewR += 1
                if t >= tree:
                    break
        visLR = tree > maxL or tree > maxR
        visUD = tree > maxU or tree > maxD
        if visLR or visUD:
            visCount += 1
        view_score[y][x] = viewU * viewD * viewL * viewR


print(f'Visible trees: {visCount}')
print(f"Best view score: {np.amax(view_score)}")

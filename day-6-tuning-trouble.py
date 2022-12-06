from utils import fetchInput
from string import ascii_lowercase

page = fetchInput("https://adventofcode.com/2022/day/6/input")
text_data = page.text
# text_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # test set
letter_use = [0]*26  # assumes a-z character set
marker = ''
chars_proc = 0

for i, char in enumerate(text_data):
    ltr_i = ascii_lowercase.index(char)
    letter_use[ltr_i] += 1
    if i > 3:
        head_i = ascii_lowercase.index(text_data[i-4])
        letter_use[head_i] -= 1
    # check if any 4 letters used once
    if letter_use.count(1) == 4:
        marker = text_data[i-3:i+1]
        chars_proc = i+1
        break

print(f'First marker: {marker}, {chars_proc}')

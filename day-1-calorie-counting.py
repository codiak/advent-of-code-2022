import requests


URL = "https://adventofcode.com/2022/day/1/input"
headers = {
    'cookie':'session=XXXXX'
}
page = requests.get(URL, headers=headers)
text_data = page.text

by_elf_str = text_data.split('\n\n')


# break apart and parse each elf's calories
def parseAndSplitNumbers(string):
    strArr = filter(None, string.split('\n'))
    intArr = list(map(int, strArr))
    return intArr

by_elf = list(map(parseAndSplitNumbers, by_elf_str))

totals_by_elf = list(map(sum, by_elf))

max_cal = max(totals_by_elf)

print(f'Max calories: {max_cal}, Elf #:{totals_by_elf.index(max_cal)}')

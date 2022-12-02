from utils import fetchInput
import heapq


page = fetchInput("https://adventofcode.com/2022/day/1/input")
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

# using list.sort - -7.39e-5s
# sorted_totals = totals_by_elf.copy()
# sorted_totals.sort(reverse=True)

# using heapq - -3.79e-5s
heap_totals = heapq.nlargest(3, totals_by_elf)

for i, cals in enumerate(heap_totals):
    print(f'Most #{i+1}, Elf #{totals_by_elf.index(cals)}, {cals}cal')

print(f'~~~\nTop 3 total: {sum(heap_totals)}')

from utils import fetchInput


page = fetchInput("https://adventofcode.com/2022/day/2/input")
text_data = page.text
games = list(filter(None, text_data.split('\n')))

# First column, opponent will play: A for Rock, B for Paper, and C for Scissors.
# Second column, what to play: X for Rock, Y for Paper, and Z for Scissors
# Score calculated by:
# (1 for Rock, 2 for Paper, and 3 for Scissors) + (0 if you lost, 3 if the round was a draw, and 6 if you won)
choice_cases = {
    'A X': 1+3, 'A Y': 2+6, 'A Z': 3+0,
    'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
    'C X': 1+6, 'C Y': 2+0, 'C Z': 3+3
}

your_scores = list(map(lambda s: choice_cases[s], games.copy()))

print(f'Assuming choice score: {sum(your_scores)}')

# X means you need to lose, Y means you need to end the round in a draw, Z means you need to win
using_guide_cases = {
    'A X': 3+0, 'A Y': 1+3, 'A Z': 2+6,
    'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
    'C X': 2+0, 'C Y': 3+3, 'C Z': 1+6
}

using_guide_scores = list(map(lambda s: using_guide_cases[s], games.copy()))

print(f'Using guide score: {sum(using_guide_scores)}')

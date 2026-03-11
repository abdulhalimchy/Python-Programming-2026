# Write your solution here
from random import choice

def roll(die: str):
    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
    return choice(dice[die])

def play(die1: str, die2: str, times: int):
    win1 = 0
    win2 = 0
    ties = 0

    for _ in range(times):
        r1 = roll(die1)
        r2 = roll(die2)

        if r1 > r2:
            win1 += 1
        elif r2 > r1:
            win2 += 1
        else:
            ties += 1

    return (win1, win2, ties)
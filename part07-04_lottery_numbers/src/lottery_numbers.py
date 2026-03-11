# Write your solution here

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = sample(range(lower, upper + 1), amount)
    numbers.sort()
    return numbers
# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    part = Fraction(1, amount)
    return [part] * amount
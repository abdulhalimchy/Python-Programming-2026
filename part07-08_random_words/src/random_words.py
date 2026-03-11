# Write your solution here
from random import sample

def words(n: int, beginning: str):
    with open("words.txt") as file:
        all_words = [line.strip() for line in file]

    matching_words = [word for word in all_words if word.startswith(beginning)]

    if len(matching_words) < n:
        raise ValueError("Not enough matching words")

    return sample(matching_words, n)
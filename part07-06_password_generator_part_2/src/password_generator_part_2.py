# Write your solution here
import string
from random import choice, shuffle

def generate_strong_password(length: int, numbers: bool, special: bool):
    password = []

    # at least one lowercase letter
    password.append(choice(string.ascii_lowercase))

    if numbers:
        password.append(choice(string.digits))

    specials = "!?=+-()#"
    if special:
        password.append(choice(specials))

    # character pool
    pool = string.ascii_lowercase
    if numbers:
        pool += string.digits
    if special:
        pool += specials

    # fill the remaining characters
    while len(password) < length:
        password.append(choice(pool))

    shuffle(password)
    return "".join(password)
# Write your solution here
import string
from random import choice

def generate_password(length: int):
    password = ""
    for i in range(length):
        password += choice(string.ascii_lowercase)
    return password
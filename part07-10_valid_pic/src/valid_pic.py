# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    day = pic[0:2]
    month = pic[2:4]
    year = pic[4:6]
    century = pic[6]
    personal = pic[7:10]
    control = pic[10]

    # Check century marker
    if century not in "+-A":
        return False

    # Determine full year
    if century == "+":
        full_year = int("18" + year)
    elif century == "-":
        full_year = int("19" + year)
    else:  # A
        full_year = int("20" + year)

    # Validate date
    try:
        datetime(full_year, int(month), int(day))
    except ValueError:
        return False

    # Calculate control character
    number = int(day + month + year + personal)
    remainder = number % 31
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    return characters[remainder] == control
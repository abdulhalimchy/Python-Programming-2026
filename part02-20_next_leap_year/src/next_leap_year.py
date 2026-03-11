# Write your solution here

current_year = int(input("Year: "))
year = current_year
is_leap_year = False

while True:
    year += 1

    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
    elif year % 4 == 0:
        is_leap_year = True
    
    if is_leap_year:
        break;

print(f"The next leap year after {current_year} is {year}")
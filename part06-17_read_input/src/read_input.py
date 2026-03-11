# Write your solution here
def read_input(prompt: str, lower: int, upper: int):
    while True:
        try:
            value = int(input(prompt))
            if lower <= value <= upper:
                return value
        except ValueError:
            pass

        print(f"You must type in an integer between {lower} and {upper}")
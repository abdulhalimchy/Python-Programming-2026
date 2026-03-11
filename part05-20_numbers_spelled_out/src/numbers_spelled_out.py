# Write your solution here
def dict_of_numbers():
    numbers = {}
    zero_to_20 = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen"
    ]
    
    numbers[20] = "twenty"
    numbers[30] = "thirty"
    numbers[40] = "forty"
    numbers[50] = "fifty"
    numbers[60] = "sixty"
    numbers[70] = "seventy"
    numbers[80] = "eighty"
    numbers[90] = "ninety"
    
    for i in range(100):
        if i in numbers:
            continue
        if i < 20:
            numbers[i] = zero_to_20[i]
        else:
            first = (i // 10) * 10
            last = i % 10
            numbers[i] = f"{numbers[first]}-{numbers[last]}"
            
    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()
    for i in range(100):
        print(f"{i}: {numbers[i]}")

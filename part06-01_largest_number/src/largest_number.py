# write your solution here

def largest():
    largest_number = None

    with open("numbers.txt") as file:
        for line in file:
            number = int(line)
            
            if largest_number is None or number > largest_number:
                largest_number = number

    return largest_number

if __name__ == "__main__":
    print(largest())
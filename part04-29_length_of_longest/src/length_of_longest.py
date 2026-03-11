# Write your solution here

def length_of_longest(my_list: list) -> int:
    longest = 0
    for word in my_list:
        longest = max(longest, len(word))
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    esult = length_of_longest(my_list)
    print(result)
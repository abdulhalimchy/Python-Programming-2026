# Write your solution here
def shortest(my_list: list) -> str:
    ans = my_list[0]

    for word in my_list:
        if len(word) < len(ans):
            ans = word
    return ans


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
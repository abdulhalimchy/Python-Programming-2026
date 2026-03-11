# Write your solution here

def all_the_longest(my_list: list):
    max_len = 0
    for word in my_list:
        max_len = max(max_len, len(word))

    ans = []
    for word in my_list:
        if len(word) == max_len:
            ans.append(word)

    return ans


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']
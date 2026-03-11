# Write your solution here
# You can test your function by calling it within the following block
def range_of_list(mylist: list):
    s_list = sorted(mylist)
    return s_list[-1] - s_list[0]

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
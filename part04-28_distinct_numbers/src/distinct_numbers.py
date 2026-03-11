# Write your solution here
def distinct_numbers(my_list):
    nums = []
    for n in my_list:
        if n not in nums:
            nums.append(n)
    nums.sort()
    return nums

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
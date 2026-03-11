# Write your solution here

def longest_series_of_neighbours(my_list):
    mx = 1
    cnt = 1
    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            cnt += 1
        else:
            cnt = 1
        mx = max(mx, cnt)
    
    return mx


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
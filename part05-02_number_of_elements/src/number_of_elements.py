# Write your solution here

def count_matching_elements(mat, element):
    cnt = 0

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            cnt += int(element == mat[i][j])

    return cnt


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1)) # 3

    m = [[1, 1, 1], [0, 1, 4], [1, 0, 0]] # 5
    print(count_matching_elements(m, 1))

    m = [[1], [0], [1]]
    print(count_matching_elements(m, 1)) # 2
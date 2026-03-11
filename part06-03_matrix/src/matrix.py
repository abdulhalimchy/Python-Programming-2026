# write your solution here
def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            row = [int(x) for x in line.split(",")]
            matrix.append(row)
    return matrix


def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix:
        total += sum(row)
    return total


def matrix_max():
    matrix = read_matrix()
    maximum = matrix[0][0]

    for row in matrix:
        for value in row:
            if value > maximum:
                maximum = value

    return maximum


def row_sums():
    matrix = read_matrix()
    sums = []

    for row in matrix:
        sums.append(sum(row))

    return sums

if __name__ == "__main__":
    print(read_matrix())
    print(matrix_sums())
    print(matrix_max())
    print(row_sums())
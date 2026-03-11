# Write your solution here
def print_sudoku(sudoku: list):
    height = len(sudoku)
    width = len(sudoku[0])
    
    for i in range(height):
        for j in range(width):
            if sudoku[i][j] == 0:
                print("_", end="")
            else:
                print(sudoku[i][j], end="")
            
            # Handle spaces
            if j != width-1:
                print(" ", end="")
            
                if j % 3 == 2:
                    print(" ", end="")
                    
        # Handle new line
        print("")
        if i != height-1 and i % 3 == 2:
            print("")


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])
    
    new_sudoku[row_no][column_no] = number
    return new_sudoku


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
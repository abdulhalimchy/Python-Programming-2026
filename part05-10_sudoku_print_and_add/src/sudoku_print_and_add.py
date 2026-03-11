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


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
    

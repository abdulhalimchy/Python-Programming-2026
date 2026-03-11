# Write your solution here
# Write your solution here

def column_correct(sudoku: list, col_no: int):
    
    seen = []
    
    for i in range(len(sudoku)):
        value = sudoku[i][col_no]
        
        if value == 0:
            continue
        if value in seen:
            return False
        seen.append(value)
        
    return True
        

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
    print(column_correct(sudoku, 2))
    print(column_correct(sudoku, 3))
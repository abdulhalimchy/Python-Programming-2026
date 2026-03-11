# Write your solution here

def transpose(matrix: list):
    new_matrix = []
    
    for c in range(len(matrix)):
        new_row = []
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        
        new_matrix.append(new_row)
        
    for i in range(len(matrix)):
        matrix[i][:] = new_matrix[i]
        

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print("transpose: ", matrix)
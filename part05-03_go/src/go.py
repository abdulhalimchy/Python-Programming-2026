# Write your solution here

def who_won(game_board: list):
    
    p1, p2 = 0, 0
    
    for row in game_board:
        for value in row:
            if value == 1:
                p1 += 1
            elif value == 2:
                p2 += 1
    
    if p1 > p2:
        return 1
    if p2 > p1:
        return 2
    return 0

if __name__ == "__main__":
    game_board = [
        [1, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 2, 2, 0, 2, 0, 0],
        [0, 1, 0, 3, 0, 0, 0, 0, 2],
        [0, 1, 4, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 3, 0, 5, 6, 0],
        [2, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 2, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [1, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(who_won(game_board))
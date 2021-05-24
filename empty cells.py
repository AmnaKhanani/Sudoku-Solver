board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
    ]
"""This iterates through all the columns in the first row, then second
row and so on. Whenever it encounters an emptycell, the function returns
the corresponding indexes. Simple!"""

def find_empty_cell(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == 0:
                return i, j  # row, col

    return -1,-1
print(find_empty_cell(board))

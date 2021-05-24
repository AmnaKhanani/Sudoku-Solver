#making board for sudoku with nested list
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

"""for solving the board created this function"""
def solve(board):
    finds = find_empty_cell(board)#calling find_empty_cell funtion and assigning to a variable
    if not finds:
        return True
    else:
        row, col = finds #assign the values of the finds variable to row, col which represent the row and column index 

    for i in range(1,10):
        if check(board,i, row, col):#calling check function in the if condition
            board[row][col] = i#using the indexex got in find function to update the board

            if solve(board):#calling solve function to solve the matrix again and again
                return True

            board[row][col] = 0#backtracking

    return False #will return false when the whole board is solved


#reference https://levelup.gitconnected.com/sudoku-solver-python-using-backtracking-1aff17a3340
def check(board, i, row, col):
    rows = board[int(row)]
    column = [board[r][col] for r in range(0,9)]
    if i in rows:
        return False
    if i in column:
        return False
    matrix_row = (row // 3)*3
    matrix_column = (col // 3)*3
    square = [board[y][z] for y in range(matrix_row, matrix_row+3) for z in range(matrix_column, matrix_column+3)]
    if i in square:
        return False
    return True


"""To make the board look like the real sudoku with
grid lines below is the code"""

def print_board(board):
    for i in range(len(board)):
        line = "" #keeping this empty so we can work on it later
        if i == 3 or i == 6:
            print("---------------------")
        #nested loop  
        for j in range(len(board)):
            if j == 3 or j == 6:
                line += "| "
            line += str(board[i][j])+" " #saving all the numbers in the line variable to print it next
        print(line)

        
"""This function is going to iterate through every index in
the board and the position where it finds 0 index,then it will
return the row and column index and if 0 is not found at any
index it will return none means loop terminates no more empty
indexes left"""

def find_empty_cell(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == 0: #row and column both should be empty(at 0 index)
                return i, j  # row, col

    return None


#calling functions
print_board(board)
solve(board)
print("_____________________")
print_board(board)


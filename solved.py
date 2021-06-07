#making grid for sudoku with nested list
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

#puzzle solving
def solve(board):
    finds = find_empty_cell(board)#function calling
    if not finds:
        return True
    else:
        row, col = finds #assign the values of the finds variable to row, col which represent the row and column index 

    for i in range(1,10):
        if check(board,i,( row, col)):#calling check function 
            board[row][col] = i#using the indexex got in find_empty function to update the board

            if solve(board):#calling solve function to solve the matrix again and again
                return True

            board[row][col] = 0#backtracking

    return False #will return false when the whole board is solved


#to check the three rules of the game
def check(board, row, col):
   
    # Check row
    for i in range(0,9):
        if board[col[0]][i] == row and col[1] != i:
            return False

    # Check column
    for i in range(0,9):
        if board[i][col[1]] == row and col[0] != i:
            return False

    # Check box
    
    square_row = (col[0] // 3*3)
    square_column = (col[1] // 3*3)

    for i in range(square_row, square_row+ 3):
        for j in range(square_column , square_column + 3):
            if board[i][j] == row and (i,j) != col:
                return False

    return True

"""To make the board look like the real sudoku with
grid lines below is the code"""

def print_board(board):
    for i in range(0,9):
        line = "" #keeping this empty so we can work on it later
        if i == 3 or i == 6:
            print("---------------------")
        #nested loop  
        for j in range(0,9):
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


def check(board, i, row, col):
    rows = board[int(row)]
    column = [board[r][col]
    for r in range(0,9)]
    if i in rows:
        return False
    if i in column:
        return False
    SquareRow = (row // 3)*3
    squareColumn = (col // 3)*3
    Square = [board[y][z]
    for y in range(SquareRow, SquareRow+3)
    for z in range(squareColumn, squareColumn+3)]
    if i in Square:
        return False
    return True

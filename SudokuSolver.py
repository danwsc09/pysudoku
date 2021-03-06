
def can_solve(board, row, col, num):
    # return True if num at (row, col) can result in a correct answer
    # return False otherwise
    

    # Copies the board
    board_copy = []
    for i in range(9):
        board_copy.append([])
        for j in range(9):
            board_copy[i].append(board[i][j])
    board_copy[row][col] = num
    
    if not check_row_col_box(board_copy, row, col, num):
        return False
    # Solve - return True if solution is possible, False otherwise
    # Start from first empty square. For each square, try a number between 1 and 9
    # And backtrack where necessary
    starting_row, starting_col = next_empty_box(board_copy, 0, 0)
    
    return can_solve_helper(board_copy, starting_row, starting_col)

def can_solve_helper(board, row, col):
    if row > 8 or col > 8 or row == -1 or col == -1:
        return True
    
    
    dict_row = {}
    for i in range(9):
        if i == col: continue
        if board[row][i] != 0:
            dict_row[board[row][i]] = 1

    dict_col = {}
    for i in range(9):
        if i == row: continue
        if board[i][col] != 0:
            dict_col[board[i][col]] = 1

    dict_box = {}
    r1 = row % 3
    c1 = col % 3

    for i in range(0 - r1, 3 - r1):
        for j in range(0 - c1, 3 - c1):
            if i == 0 and j == 0: continue
            if board[row+i][col+j] != 0:
                dict_box[board[row+i][col+j]] = 1

    for guess in range(1, 10):
        if guess in dict_row or guess in dict_col or guess in dict_box:
            continue
        
        board[row][col] = guess
        next_empty_row, next_empty_col = next_empty_box(board, row, col)
        if can_solve_helper(board, next_empty_row, next_empty_col):
            return True
    
    board[row][col] = 0
    return False

def solve(board, row, col):
    # Solves the Sudoku puzzle, assuming the puzzle is solve-able
    # print("===\nsolving row {}, col {}".format(row, col))
    if row > 8 or col > 8 or row == -1 or col == -1:
        return True
    
    dict_row = {}
    for i in range(9):
        if i == col: continue
        if board[row][i] != 0:
            dict_row[board[row][i]] = 1
    
    dict_col = {}
    for i in range(9):
        if i == row: continue
        if board[i][col] != 0:
            dict_col[board[i][col]] = 1
    
    dict_box = {}
    r1 = row % 3
    c1 = col % 3

    for i in range(0 - r1, 3 - r1):
        for j in range(0 - c1, 3 - c1):
            if i == 0 and j == 0: continue
            if board[row+i][col+j] != 0:
                        dict_box[board[row+i][col+j]] = 1
    
    # try subbing in 1-9
    for guess in range(1, 10):
        if guess in dict_row or guess in dict_col or guess in dict_box:
            continue
        # Actually try number
        print("trying {} at row {}, col {}".format(guess, row, col))
        board[row][col] = guess
        next_empty_row, next_empty_col = next_empty_box(board, row, col)
        if solve(board, next_empty_row, next_empty_col):
            return True
    board[row][col] = 0
    return False

def next_empty_box(board, cur_row, cur_col):
    if cur_row > 8 or cur_col > 8:
        return -1, -1

    while board[cur_row][cur_col] != 0:
        cur_col += 1
        if cur_col == 9:
            cur_col = 0
            cur_row += 1
            if cur_row == 9:
                return -1, -1

    return cur_row, cur_col
    
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def check_row_col_box(board, row, col, n):
    # return True if board[row][col] = n results in a possible answer
    # return False if its not possible to reach an answer
    if n == 0:
        return False
        
    # if duplicate in row, return False
    dict_row = {}
    for i in range(9):
        if board[row][i] != 0:
            if board[row][i] in dict_row:
                return False
            else:
                dict_row[board[row][i]] = 1
    
    # if duplicate in column, return False
    dict_col = {}
    for i in range(9):
        if board[i][col] != 0:
            if board[i][col] in dict_col:
                return False
            else:
                dict_col[board[i][col]] = 1
    
    # if duplicate in box, return False
    dict_box = {}
    r1 = row % 3
    c1 = col % 3

    for i in range(0 - r1, 3 - r1):
        for j in range(0 - c1, 3 - c1):
            if board[row+i][col+j] != 0:
                if board[row+i][col+j] in dict_box:
                    return False
                else:
                    dict_box[board[row+i][col+j]] = 1
    return True


if __name__ == '__main__':
    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    row, col = next_empty_box(board, 0, 0)
    solve(board, row, col)
    print(board)
    # if can_solve(board, 2, 2, 7):
    #     print("7 is ok at (2, 2)")
    # else:
    #     print("7 is not ok at (2, 2)")
    # if can_solve(board, 2, 2, 1):
    #     print("1 is ok at (2, 2)")
    # else:
    #     print("1 is not ok at (2, 2)")
    
    # if can_solve(board, 6, 0, 5):
    #     print("5 is ok at (0, 6)")
    # else:
    #     print("5 is not ok at (0, 6)")
    # board[6][0] = 5
    # if can_solve(board, 6, 1, 5):
    #     print("5 is ok at (1, 6)")
    # else:
    #     print("5 is not ok at (1, 6)")

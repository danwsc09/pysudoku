import tkinter as tk

class Game:

    def __init__(self, root):
        self._root = root
        self._root.title("Sudoku Puzzle")
        self._root.geometry("600x300")

        self._board = [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0]
        ]
        # used in solve_placeholder to check solution
        self._board_copy = []

        self._can_solve = True
        self._entries = []
        self._textVars = []
        for i in range(9):
            for j in range(9):
                self._entries.append([None]*9)
                self._textVars.append([None]*9)
                self._board_copy.append([0]*9)
        
        # register callback function
        self._reg1 = self._root.register(self.validate_entry)


        # Show grid
        self.init_grid()

        # Show message box
        self.init_msgbox()

        # Show "solve" button
        
        self._solvebutton = tk.Button(self._root, text="Solve", font="Helvetica 12", command=self.show_solve)
        self._solvebutton.grid(column=12, row=2)
        
        self._msgbox = tk.Label(master=self._root, textvariable=self._msgsv,
                    font="Helvetica 14 bold italic")
        self._msgbox.grid(column=12, row=5, columnspan=2, rowspan=3)

        return


    # Shows how the computer solves the puzzle
    # Changes the textVars while trying different numbers
    # The puzzle must be in a "solve-able" state
    def show_solve(self):
        if not self._can_solve:
            return
        
        starting_row, starting_col = self.next_empty_square(self._board, 0, 0)
        print("inside show_solve")
        print("s_row: {}, s_col: {}".format(starting_row, starting_col))
        self.show_solve_helper(starting_row, starting_col)

        self._msgsv.set("Done")
        return
    
    # Helper function called by show_solve
    def show_solve_helper(self, row, col):
        print("inside show_solve_helper")
        print("row: {}, col: {}".format(row, col))
        if row > 8 or col > 8 or row == -1 or col == -1:
            return True
        
        
        dict_row = {}
        for i in range(9):
            if i == col: continue
            if self._board[row][i] != 0:
                dict_row[self._board[row][i]] = 1

        dict_col = {}
        for i in range(9):
            if i == row: continue
            if self._board[i][col] != 0:
                dict_col[self._board[i][col]] = 1

        dict_box = {}
        r1 = row % 3
        c1 = col % 3

        for i in range(0 - r1, 3 - r1):
            for j in range(0 - c1, 3 - c1):
                if i == 0 and j == 0: continue
                if self._board[row+i][col+j] != 0:
                            dict_box[self._board[row+i][col+j]] = 1

        for guess in range(1, 10):
            if guess in dict_row or guess in dict_col or guess in dict_box:
                continue
            print("guess: {}".format(guess))
            self._board[row][col] = guess
            self._textVars[row][col].set(str(guess))
            
            next_empty_row, next_empty_col = self.next_empty_square(self._board, row, col)

            print("next empty row, col: {}, {}".format(next_empty_row, next_empty_col))
            if self.show_solve_helper(next_empty_row, next_empty_col):
                return True
        
        self._board[row][col] = 0
        self._textVars[row][col].set("")
        print("end. row: {}, col: {}".format(row, col))
        return False


    def check_row_col_box(self, row, col, n):
        # return True if board[row][col] = n results in a possible answer
        # return False if its not possible to reach an answer
        
        # if duplicate in row, return False
        dict_row = {}
        for i in range(9):
            if self._board[row][i] != 0:
                if self._board[row][i] in dict_row:
                    return False
                else:
                    dict_row[self._board[row][i]] = 1
        print("dict row: ", dict_row)

        # if duplicate in column, return False
        dict_col = {}
        for i in range(9):
            if self._board[i][col] != 0:
                if self._board[i][col] in dict_col:
                    return False
                else:
                    dict_col[self._board[i][col]] = 1
        print("dict col: ", dict_col)

        # if duplicate in box, return False
        dict_box = {}
        r1 = row % 3
        c1 = col % 3

        for i in range(0 - r1, 3 - r1):
            for j in range(0 - c1, 3 - c1):
                if self._board[row+i][col+j] != 0:
                    if self._board[row+i][col+j] in dict_box:
                        return False
                    else:
                        dict_box[self._board[row+i][col+j]] = 1
        print("dict box: ", dict_box)
        return True

    def change_board(self, row, col):
        # Called when text variable is changed
        # Update the 9x9 board (self._board[i][j]) whenever text is changed
        n = self._textVars[row][col].get()
        if n == "":
            self._can_solve = True
            return
        if not n.isdigit() or int(n) == 0:
            self._board[row][col] = 0
            self._msgsv.set("Invalid input")
            self._can_solve = False
            return
        
        self._msgsv.set("Checking...")
        n = int(n)
        self._board[row][col] = n
        for i in range(9):
            for j in range(9):
                print(self._board[i][j], end=" ")
            print()
        
        
        # Check if duplicate in row/column/box
        if not self.check_row_col_box(row, col, n):
            self._can_solve = False
            self._msgsv.set("{} in row {}, col {} is incorrect".format(n, row+1, col+1))

        # Solve puzzle. If possible solution, return True. Otherwise, return False
        elif not self.solve_placeholder():
            self._can_solve = False
            self._msgsv.set("{} in row {}, col {} is incorrect".format(n, row+1, col+1))
        
        # if correct:
        else: 
            # try to solve - if there is no solution, return False
            self._msgsv.set("Good.")
            self._can_solve = True

    def solve_placeholder(self):
        # Used to solve the puzzle on a copy (._board_copy)
        # Returns True if there is a solution
        # False otherwise

        # copy board
        for i in range(9):
            for j in range(9):
                self._board_copy[i][j] = self._board[i][j]
        
        # Solve - return True if solution is possible, False otherwise
        # Start from first empty square. For each square, try a number between 1 and 9
        # And backtrack where necessary
        starting_row, starting_col = self.next_empty_square(self._board_copy, 0, 0)
        print("starting_row: {}, starting_col: {}".format(starting_row, starting_col))
        return self.solve_helper(starting_row, starting_col)

    # Hlper for solve_placeholder function
    def solve_helper(self, row, col):
        if row > 8 or col > 8 or row == -1 or col == -1:
            return True
        
        
        dict_row = {}
        for i in range(9):
            if i == col: continue
            if self._board_copy[row][i] != 0:
                dict_row[self._board_copy[row][i]] = 1

        dict_col = {}
        for i in range(9):
            if i == row: continue
            if self._board_copy[i][col] != 0:
                dict_col[self._board_copy[i][col]] = 1

        dict_box = {}
        r1 = row % 3
        c1 = col % 3

        for i in range(0 - r1, 3 - r1):
            for j in range(0 - c1, 3 - c1):
                if i == 0 and j == 0: continue
                if self._board_copy[row+i][col+j] != 0:
                            dict_box[self._board_copy[row+i][col+j]] = 1

        for guess in range(1, 10):
            if guess in dict_row or guess in dict_col or guess in dict_box:
                continue
            
            self._board_copy[row][col] = guess
            next_empty_row, next_empty_col = self.next_empty_square(self._board_copy, row, col)
            if self.solve_helper(next_empty_row, next_empty_col):
                return True
        
        self._board_copy[row][col] = 0
        return False

    def next_empty_square(self, board, row, col):
        if row > 8 or col > 8:
            return -1, -1
        
        while board[row][col] != 0:
            col += 1
            if col == 9:
                col = 0
                row += 1
                if row == 9:
                    return -1, -1
        return row, col


    def init_grid(self):
        # Instantiates a 9x9 grid tk.Entry and textVar (tk.StringVar) to keep track of the board
        for i in range(9):
            for j in range(9):
                if self._board[i][j] != 0:
                    self._entries[i][j] = tk.Label(master=self._root, text=str(self._board[i][j]), width=3, font="Helvetica 12 bold italic")
                
                else:
                    self._textVars[i][j] = tk.StringVar(master=self._root)
                    self._textVars[i][j].trace_add("write", lambda var, index, mode, row=i, col=j: self.change_board(row, col))
                    self._entries[i][j] = tk.Entry(master=self._root, width=3, textvariable=self._textVars[i][j])
                    self._entries[i][j].config(validate="key", validatecommand=(self._reg1, '%P'))

                    # font
                    self._entries[i][j].config(font="Arial 12", justify="center")
                
                # display
                self._entries[i][j].grid(row=i, column=j)

                # background color
                if (i // 3 == 0 and j // 3 == 1) or (i // 3 == 1 and (j // 3 == 0 or j // 3 == 2)) or (i // 3 == 2 and j // 3 == 1):
                    self._entries[i][j].config(bg='#f0f2b8')
                else:
                    self._entries[i][j].config(bg='#baddf7')
        
    
    def init_msgbox(self):
        self._msgsv = tk.StringVar()
        self._msgsv.set("Message")
        self._msgbox = tk.Label(master=self._root, textvariable=self._msgsv,
                    font="Helvetica 14 bold italic")
        self._msgbox.grid(column=11, row=5, columnspan=3, rowspan=3)

    def validate_entry(self, input):
        print("inside callback. input: ", input)
        if len(input) > 1:
            self._msgsv.set("One character at a time")
            return False

        return True
        

if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    root.mainloop()



import tkinter as tk

# todo: whenever text is updated, update the 9x9 board

class Game:

    def __init__(self, root):
        self._root = root
        self._root.title("Sudoku Puzzle")
        self._root.geometry("600x600")

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
        self._entries = []
        self._textVars = []
        for i in range(9):
            for j in range(9):
                self._entries.append([None]*9)
                self._textVars.append([None]*9)
        
        # register callback function
        self._reg1 = self._root.register(self.callback_fun)


        # Show grid
        self.init_grid()

        # Show message box
        self.init_msgbox()

    def init_grid(self):
        for i in range(9):
            for j in range(9):
                if self._board[i][j] != 0:
                    self._entries[i][j] = tk.Label(master=self._root, text=str(self._board[i][j]), width=3)
                
                else:
                    self._textVars[i][j] = tk.StringVar(master=self._root)
                    self._entries[i][j] = tk.Entry(master=self._root, width=3, textvariable=self._textVars[i][j])
                    self._entries[i][j].config(validate="key", validatecommand=(self._reg1, '%P'))
                
                # display
                self._entries[i][j].grid(row=i, column=j)

                # font
                self._entries[i][j].config(font="Helvetica 14 bold italic", justify="center")

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
        self._msgbox.grid(column=11, row=5, columnspan=3)

    def callback_fun(self, input):
        print("inside callback. input: ", input)
        if len(input) > 1:
            self._msgsv.set("One character at a time")
            return False
        self._msgsv.set("Message")
        return True
        

if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    root.mainloop()


'''
#textvar = tk.StringVar(master=root)
entry = tk.Entry(master=root, text="", width=3) #textvariable=textvar
entry.grid()
reg = root.register(callback_fun)
entry.config(validate="key", validatecommand=(reg,'%P'))

textvar1 = tk.StringVar(master=root)
label1 = tk.Label(master=root, textvariable=textvar1)
label1.grid()

entry.config(bg='#f0f2b8')
'''
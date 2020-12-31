import tkinter as tk
import time

# sample code: https://stackoverflow.com/questions/4954395/create-board-game-like-grid-in-python

class Game:
    def __init__(self, window):
        self._window = window
        self._board = tk.Canvas(self._window, width=630, height=630, bg="#b8d3f2")
        self._board.grid()
        

        self._label1 = tk.Label(self._window, text="Some text")
        self._label1.grid(row=0, column=1)
        

root = tk.Tk()
game = Game(root)
root.title("SUDOKU")
root.geometry("800x700")
root.mainloop()
# app = App(root)
# root.wm_title("Tkinter clock")
# root.geometry("200x200")
# #root.after(1000, app.update_clock)
# root.mainloop()

import tkinter as tk

window = tk.Tk()    ## frame

window.title("My App!")
window.geometry("800x700")

# initialize
sq_size = 70
num_sq = 9
board = []
for i in range(num_sq):
    board.append([None]*num_sq)
pad_x = 10
pad_y = 10


# canvas
cv = tk.Canvas(window, borderwidth=0, highlightthickness=10, width=631,
                    height=631, background="bisque")

def clicked(event):
    item = cv.find_closest(event.x, event.y)

    current_color = cv.itemcget(item, 'fill')

    cv.itemconfig(item, fill='black')

def focused(event):
    cv.f

for i in range(num_sq):
    for j in range(num_sq):
        # Create tag for each box
        curr_tag = "num"+str(i)+str(j)
        
        # Create each box
        board[i][j] = cv.create_rectangle(pad_x+sq_size*i, pad_y+sq_size*j, 
                        pad_x+sq_size*(i+1), pad_y+sq_size*(j+1), tags=curr_tag)
        
        # bind each box
        cv.bind("<FocusIn>", focused)
        # cv.bind("<Button-1>", clicked)
        


cv.grid(row=0, column=0, padx=pad_x, pady=pad_y)

window.mainloop() ## runs everyhting inside the window



# # LABEL
# title = tk.Label(text="Hello world.\nWelcome to My App!", font=("Times New Roman", 20))
# # stained glass, where should it go?
# title.grid(column=0, row=0)

# # BUTTON
# button1 = tk.Button(text="Click me", bg="red")
# button1.grid(column=0, row=1)

# # ENTRY
# entry_field1 = tk.Entry()
# entry_field1.grid(column=0, row=2)

# # TEXT FIELD
# text_field = tk.Text(master=window, height=10, width=30)
# text_field.grid()

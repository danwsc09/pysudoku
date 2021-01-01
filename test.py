'''
#textvar = tk.StringVar(master=root)
entry = tk.Entry(master=root, text="", width=3) #textvariable=textvar
entry.grid()
reg = root.register(validate_entry)
entry.config(validate="key", validatecommand=(reg,'%P'))

textvar1 = tk.StringVar(master=root)
label1 = tk.Label(master=root, textvariable=textvar1)
label1.grid()

entry.config(bg='#f0f2b8')
'''")
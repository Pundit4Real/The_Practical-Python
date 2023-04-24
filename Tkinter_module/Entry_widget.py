from tkinter import *

window = Tk()

label = Label(text='user name')
entry1 = Entry()

label.pack()
entry1.pack()

# creating the entry widget
entry = Entry(bg='aqua',fg='black', width=40) 
entry.pack()
# main operations that you can perform with Entry widgets.
# 1.Deleting text with the .delete()
# 2.Retrieving text with the .get()
# 3.Inserting text with the .insert()
window.mainloop()
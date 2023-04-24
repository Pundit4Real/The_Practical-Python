from tkinter import *

window = Tk()
# create label widget
label = Label(text='welcome to Pundit Market', bg='pink', fg='blue', width=20, height= 40)
label.pack()
# creating a button label.
button = Button(text='click Here!', width=30, height= 10, bg='blue', fg= 'white')
button.pack()

window.mainloop()
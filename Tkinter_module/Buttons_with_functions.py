from tkinter import *

window = Tk()

# Events handling in gui python

# creating a function

def greeting_message():
    greeting_a = Label(text='What are you doing today?',font='arial 15 italic', fg='white', bg='green')
    greeting_a.pack()
    greeting_b = Label(text='Come let party!!',font='arial 20 italic underline', fg='tomato', bg='blue')
    greeting_b.pack()



btn = Button(text='Click me', font='arial', bg='blue', fg='white',command=greeting_message)
btn.pack()

window.mainloop()
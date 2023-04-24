from tkinter import *
from time import strftime

root = Tk()
root.title('Digital clock')

def time():
    timeFrame = strftime('%H:%M:%S: %p')
    clock.config(text=timeFrame)
    clock.after(1000,time)


clock= Label(root, font='arial 100 bold', pady=30, fg='white', bg='blue', width=20, height=50)
clock.pack(anchor='center')

time()
mainloop()
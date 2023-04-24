# frame widget are used for organizing the layout of our widget in an application.

from tkinter import*

window = Tk()

frame1 = Frame()
label1 = Label(master=frame1, text='Welcome to pundit market',bg='purple')
label1.pack()

frame2 = Frame()
label2 = Label(master=frame2, text='Let learn about forex trading',bg= 'blue')
label2.pack()

# note the order of the frame packing is important.
frame1.pack()
frame2.pack()

window.mainloop()
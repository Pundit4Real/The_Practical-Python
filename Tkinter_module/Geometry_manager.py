# Geometry manager is use in python to manage the layout of applicatiion , we have three main kinds.

# 1. the .pack() manager.
# 2. the .place() manager.
# 3. the .grid() manager

# 1. the .pack() manager.
# the .pack() manager uses a packing algorithm to place widgets in a frame or window in a specified order.         note also that, to give aligment to a widget use the fill(), the side() inside the pack manager.

from tkinter import *

window = Tk()

# frame = Frame(master=window, width=200, height=200)
frame = Frame(master=window, width=200, height=200)
frame.pack()

frame1 = Frame(master=window,width=150, height=150, bg='blue' )
frame1.pack(fill=Y, side='left')

frame2 = Frame(master=window,width=100, height=100, bg='purple' )
frame2.pack()

frame3 = Frame(master=window,width=50, height=50, bg='pink' )
frame3.pack()

# create label widgets
label1 = Label(master=frame, text='I am at (0,0)', bg='green', fg='yellow')
label1.place(x=0, y=0)

label2 = Label(master=frame, text='I am at (50,50)', bg='red')
label2.place(x=50, y=50)

label3 = Label(master=frame, text='I am at (100,125)', bg='red')
label3.place(x=100, y=125)




window.mainloop()


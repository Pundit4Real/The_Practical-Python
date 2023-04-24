# main operations that you can perform with Text widgets.
# 1.Deleting text with the .delete()
# 2.Retrieving text with the .get()
# 3.Inserting text with the .insert()

from tkinter import*

window = Tk()

# creating a text widget
label = Label(text='eassy area',bg= 'white')
text_box = Text(bg= 'magenta', fg='white')
label.pack()
text_box.pack()

window.mainloop()
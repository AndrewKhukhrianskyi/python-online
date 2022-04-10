from tkinter import *

# Task 1 - Open me task
def open_me():
    sub_root = Toplevel()
    sub_root.geometry('200x100')
    sub_root.resizable(False, False)

    label = Label(sub_root,
                 width = 20,
                 height = 1,
                 text = 'Ты меня открыл!')
    
    label.pack(anchor = N)
    
    
root = Tk()

root.geometry('100x100')
root.resizable(False, False)



button = Button(width = 7,
                height = 2,
                text = 'Нажми!',
                command = open_me)

button.pack(anchor = N)

root.mainloop()

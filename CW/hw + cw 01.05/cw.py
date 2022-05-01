from dis import code_info
from tkinter import *

from tkinter import filedialog as fd
from tkinter import messagebox as mb

def file_open():
   filename = fd.askopenfilename()
   with open(filename, 'r', encoding='utf8') as file:
    textfromfile = file.read()
    text_label.insert(0.0, textfromfile)
    file.close()
    
   mb.showinfo('Result', "Done!")

def file_resave():
    tuples = (
        ("Text file", '*txt'),
        ("Doc file", '*docx'),
        ("PDF file", '*pdf')
    )
    result = fd.asksaveasfile(title = 'Save this file!',
                              filetypes = tuples)
    text = text_label.get(0.0, END)
    result.write(text)

    mb.showinfo('Result', 'Saved!')

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)

btn = Button(width = 5,
            height = 1,
            command = file_open,
            text = 'Read')

btn2 = Button(width = 5,
            height = 1,
            command = file_resave,
            text = 'Save')

text_label = Text(width = 40,
                  height = 20)

btn.pack(anchor = N)
btn2.pack(anchor = N)
text_label.pack(anchor = N)

root.mainloop()
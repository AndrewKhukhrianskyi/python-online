from tkinter import *

from config import *

def square_window():
    sub_root = Toplevel()
    sub_root.geometry(f"{WIDTH}x{HEIGHT}")
    sub_root.resizable(False, False)

    square = Canvas(sub_root)
    square.create_rectangle(COORDS)
    square.pack(anchor = N)


def line_window():
    sub_root = Toplevel()
    sub_root.geometry(f"{WIDTH}x{HEIGHT}")
    sub_root.resizable(False, False)

    square = Canvas(sub_root)
    square.create_line(COORDS)
    square.pack(anchor = N)

def curve_window():
    sub_root = Toplevel()
    sub_root.geometry(f"{WIDTH}x{HEIGHT}")
    sub_root.resizable(False, False)

    square = Canvas(sub_root)
    square.create_arc(COORDS)
    square.pack(anchor = N)

def cycle_window():
    sub_root = Toplevel()
    sub_root.geometry(f"{WIDTH}x{HEIGHT}")
    sub_root.resizable(False, False)

    square = Canvas(sub_root)
    square.create_oval(COORDS)
    square.pack(anchor = N)

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

square_btn = Button(width = BUTTON_WIDTH,
                    height = BUTTON_HEIGHT,
                    text = 'Квадрат',
                    command = square_window)

line_btn = Button(width = BUTTON_WIDTH,
                    height = BUTTON_HEIGHT,
                    text = 'Линия',
                    command = line_window)

oval_btn = Button(width = BUTTON_WIDTH,
                    height = BUTTON_HEIGHT,
                    text = 'Круг',
                    command = cycle_window)

curve_btn = Button(width = BUTTON_WIDTH,
                    height = BUTTON_HEIGHT,
                    text = 'Кривая',
                    command = curve_window)

widgets = [square_btn, line_btn,
       oval_btn, curve_btn]

for wdg in widgets:
    wdg.pack(anchor = W)

root.mainloop()
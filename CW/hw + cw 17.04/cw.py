from tkinter import *
from tkinter import messagebox as mb

from random import randint, choice

def randomize():
    mb.showinfo('Рандомизатор', f"Ваше число: {randint(10, 100)}")

def say_hello():
    hellos = ['Привет!', "Алоха!",
              'Hello!', "G'day!",
              'Приветствую тебя!']
    mb.showinfo("Приветствие!", choice(hellos))

def say_bye():
    byes = ['Пока!', "Хорошего дня!",
              'Чао!', "Можешь не приходить :(",
              'Гудбай!']
    mb.showinfo("Приветствие!", choice(byes))


root = Tk()
root.geometry('100x100')

menubutton = Menubutton(text = 'Options', width = 5)
var = IntVar()

menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label = "Рандомизировать", 
                                variable = var,
                                command = randomize)
menubutton.menu.add_checkbutton(label = "Приветстовать", 
                                variable = var,
                                command = say_hello)
menubutton.menu.add_checkbutton(label = "Попрощаться",
                                variable = var,
                                command = say_bye)

menubutton.grid()
menubutton.pack()

root.mainloop()



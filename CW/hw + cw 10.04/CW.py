from tkinter import *
from tkinter import messagebox as mb

'''
from random import choice

def m_box():
    mb.showinfo('Окошко', "Вы нажали на кнопку")

def w_box():
    mb.showwarning('Предупреждение', "Аккуратно - ты нажал на кнопку!")

def err_box():
    mb.showerror('Ошибка', "Ошибочно нажатая кнопка :)")

def yesno_box():
    answer = mb.askyesno("Вопрос", "Ты точно нажал на кнопку?")
    if answer: # answer == True:
        mb.showinfo('Окошко', "Вы нажали на кнопку")
    else:
        mb.showerror('Ошибка', "Обманщик!")


root = Tk()
root.geometry('100x100')
root.resizable(0, 0)
root.title('Название')

mass = [m_box, w_box,
        err_box, yesno_box]

btn = Button(width = 5,
             height = 1,
             text = 'Жмяк!',
             command = choice(mass))

btn.pack(anchor = N)

root.mainloop()
'''

def add():
    num = txt1.get(0.0, END)
    num2 = txt2.get(0.0, END)

    try:
        num = int(num)
        num2 = int(num2)

        res = str(num + num2)
        label['text'] = res
    except:
        mb.showerror('Ошибка', "Введено некорректное значение!")
    
    

root = Tk()
root.geometry('100x200')
root.resizable(False, False)

txt1 = Text(width = 5,
            height = 2)
txt2 = Text(width = 5,
            height = 2)

label = Label(width = 5,
              height = 2)

btn = Button(text = "+",
            command = add)

widgets = [txt1, txt2, label, btn]

for wdg in widgets:
    wdg.pack(anchor = N)

root.mainloop()
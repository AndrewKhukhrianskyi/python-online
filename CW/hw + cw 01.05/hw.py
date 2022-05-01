from tkinter import *
from tkinter import messagebox as mb

from math import pi, sqrt, exp
from random import choice
"""
# Task 1 - Стих

def get_rnd_phrase():
    texts = {'Пушкин': 'У лукоморья дуб зеленый...',
            "Блок" : "Ночь, улица, фонарь, аптека...",
            "Украинка": "Без надії таки сподіваюсь...",
            "Маяковский": "Как говорят – «инцидент исперчен», любовная лодка разбилась о быт...",
            "Белый": "Откос под ногами песчаный, отлогий..."}
    authors = list(texts.keys()) # ['Блок' ... ]


    tplvl = Toplevel()
    tplvl.geometry("600x50")
    tplvl.resizable(False, False)

    text_label = Label(tplvl, 
                       width = 100,
                       height = 1,
                       text = texts[choice(authors)])
    
    text_label.pack(anchor = N)

def pushkin():
    texts = 'Пушкин: У лукоморья дуб зеленый...'
            
    tplvl = Toplevel()
    tplvl.geometry("400x50")
    tplvl.resizable(False, False)

    text_label = Label(tplvl, 
                       width = 50,
                       height = 1,
                       text = texts)
    
    text_label.pack(anchor = N)

def block():
    texts = "Блок: Ночь, улица, фонарь, аптека..."
            
    tplvl = Toplevel()
    tplvl.geometry("400x50")
    tplvl.resizable(False, False)

    text_label = Label(tplvl, 
                       width = 50,
                       height = 1,
                       text = texts)
    
    text_label.pack(anchor = N)

def ukrainka():
    texts = "Украинка: Без надії таки сподіваюсь..."
            
    tplvl = Toplevel()
    tplvl.geometry("400x50")
    tplvl.resizable(False, False)

    text_label = Label(tplvl, 
                       width = 50,
                       height = 1,
                       text = texts)
    
    text_label.pack(anchor = N)



root = Tk()
root.geometry('100x100')
root.resizable(False, False)

btn = Menubutton(text = 'Стих!',
                 width = 5)
var = IntVar()

btn.menu = Menu(btn)
btn["menu"] = btn.menu

btn.menu.add_radiobutton(label = "Случайный стих",
                         variable = var,
                         command = get_rnd_phrase)

btn.menu.add_radiobutton(label = "Пушкин",
                         variable = var,
                         command = pushkin)

btn.menu.add_radiobutton(label = "Українка",
                         variable = var,
                         command = ukrainka)

btn.menu.add_radiobutton(label = "Блок",
                         variable = var,
                         command = block)

btn.grid()
btn.pack(anchor = N)

root.mainloop()

"""
# Task 2 - Smart-кулятор

def add():
    try:
        if field_1.get(0.0, END).find('.') != -1: # 
            elem = float(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem + elem2)
        else:
            elem = int(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem + elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

    
def minus():
    try:
        if field_1.get(0.0, END).find('.') != -1:
            elem = float(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem - elem2)
        else:
            elem = int(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem - elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

def div():
    try:
        if field_1.get(0.0, END).find('.') != -1:
            elem = float(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem / elem2)
        else:
            elem = int(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem / elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')


def multiply():
    try:
        if field_1.get(0.0, END).find('.') != -1:
            elem = float(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem * elem2)
        else:
            elem = int(field_1.get(0.0, END))
            elem2 = int(field_2.get(0.0, END))

            label['text'] = str(elem * elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

def add_pi():
    field_1.insert(0.0, str(pi))

def get_sqrt():
    mb.showinfo('Корень' , f"Результат вычисления корня {field_1.get(0.0, END)}: {sqrt(int(field_1.get(0.0, END)))}")

def get_exp():
    mb.showinfo('Экспонента', f"Экспонента числа {field_1.get(0.0, END)}: {round(exp(int(field_1.get(0.0, END))), 2)}")

def hint():
    mb.showinfo('Подсказка', "Для вычисления корня\экспоненты, запиши число только в одно верхнее поле.")

root = Tk()
root.geometry('300x300')
root.resizable(0, 0)

field_1 = Text(width = 5,
               height = 1)
field_2 = Text(width = 5,
               height = 1)

label = Label(width = 30)

btn = Menubutton(text = 'Спец. операции',
                 width = 20)
var = IntVar()

btn.menu = Menu(btn)
btn["menu"] = btn.menu

btn.menu.add_radiobutton(label = "Число Пи",
                         variable = var,
                         command = add_pi)

btn.menu.add_radiobutton(label = "Корень",
                         variable = var,
                         command = get_sqrt)

btn.menu.add_radiobutton(label = "Экспонента",
                         variable = var,
                         command = get_exp)

btn.menu.add_radiobutton(label = "Подсказка",
                         variable = var,
                         command = hint)
add_btn = Button(width = 5, 
                height = 2,
                command = add,
                text = '+')

div_btn = Button(width = 5, 
                height = 2,
                command = div,
                text = '/')

minus_btn = Button(width = 5, 
                height = 2,
                command = minus,
                text = '-')

multi_btn = Button(width = 5, 
                height = 2,
                command = multiply,
                text = '*')

arr = [field_1, field_2, label, add_btn,
       div_btn, minus_btn, multi_btn]


btn.pack(anchor = NW)

for elem in arr:
    elem.pack(anchor = N)

root.mainloop()


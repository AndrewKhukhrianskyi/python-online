# Task 1 - Калькулятор
from tkinter import *

from tkinter import messagebox as mb
'''
def add():
    try:
        elem = int(field_1.get(0.0, END))
        elem2 = int(field_2.get(0.0, END))

        label['text'] = str(elem + elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

    
def minus():
    try:
        elem = int(field_1.get(0.0, END))
        elem2 = int(field_2.get(0.0, END))

        label['text'] = str(elem - elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

def div():
    try:
        elem = int(field_1.get(0.0, END))
        elem2 = int(field_2.get(0.0, END))

        label['text'] = str(elem // elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

def multiply():
    try:
        elem = int(field_1.get(0.0, END))
        elem2 = int(field_2.get(0.0, END))

        label['text'] = str(elem * elem2)
    except:
        mb.showerror('Ошибка', 'При обработке данных произошла ошибка. Пожалуйста, перепроверьте данные!')

root = Tk()
root.geometry('300x300')
root.resizable(0, 0)

field_1 = Text(width = 5,
               height = 1)
field_2 = Text(width = 5,
               height = 1)

label = Label(width = 5)

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


for elem in arr:
    elem.pack(anchor = N)

root.mainloop()

'''

# Task 2 - login form

# Constants
USER = 'admin'
PWD = 'admin'

def check():
    if user_field.get(0.0, END) == USER and pwd_field.get(0.0, END) == PWD:
        mb.showinfo('Успех!', f"Добро Пожаловать, {USER}!")

    elif user_field.get(0.0, END) != USER and pwd_field.get(0.0, END) == PWD:
        mb.showerror('Провал!', f"Не пущу! Я не знаю тебя, {user_field.get(0.0, END)}")

    elif user_field.get(0.0, END) == USER and pwd_field.get(0.0, END) != PWD:
        mb.showerror('Провал!', f"Неверный пароль, {user_field.get(0.0, END)}!")

    elif user_field.get(0.0, END) == '' and pwd_field.get(0.0, END) != '':
        mb.showerror('Провал!', "Введи что-то!")
    
    else:
        pass


root = Tk()

root.geometry('150x150')
root.resizable(0, 0)

user_label = Label(text = 'Имя пользователя',
                    width = 15,
                    height = 1)
user_field = Text(width = 10,
                  height = 1)

pwd_label = Label(text = 'Пароль',
                    width = 10,
                    height = 1)
pwd_field = Text(width = 10,
                 height = 1,)

login_btn = Button(text = 'Логин!',
                   height = 1,
                   width = 5,
                   command = check)

arr = [user_label, user_field,
       pwd_label, pwd_field,
       login_btn]

for wdg in arr:
    wdg.pack(anchor = N)

root.mainloop()
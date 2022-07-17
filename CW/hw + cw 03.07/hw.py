# Task 1 - +-1

from random import randint
from time import sleep
'''
def rnd_1(func):
    number = func()
    if randint(1,2) == 1:
        print('+1')
        print(f"Before: {number}")
        print(f"After: {number + 1}")
    else:
        print('-1')
        print(f"Before: {number}")
        print(f"After: {number -1}")

@rnd_1
def randomize_number():
    print('Generating number...')
    sleep(2)
    return randint(1, 100)


# Task 2 - Add dot on the end of sentence
def add_dot(sentence):
    text = sentence()
    if text[-1] == '.':
        print("Точка уже есть в конце предложения!")
    else:
        print(f"Полученный текст: {text}")
        print('Вставляем точку в конец предложения...')
        sleep(2)
        print(f'Результат: {text + "."}')

@add_dot
def some_sentence():
    print('Здесь находится текст...')
    return 'Ночь, улица, фонарь, аптека'


# Task 3 - Object replacement 

class Example:
    def __init__(self, variable):
       self.variable = variable

    @property
    def generate_variable(self):
        var = randint(1,10)
        print(f"Новый параметр: {var}")
        return var

    def print_variable(self):
        print(f"Результат: {self.variable}")
    
    @generate_variable.setter
    def print_new_variable(self, var):
        print(f'Начинаем изменять параметр {self.variable}...')
        self.variable = var
        sleep(2)

parameter = Example('Test')
parameter.print_variable()
parameter.variable = parameter.generate_variable
parameter.print_variable()
'''
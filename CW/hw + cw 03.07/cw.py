'''
from random import randint

def appender(arr):
    arr.append(randint(1,10))
    print(arr)
    if len(arr) == 10:
        return arr
    return appender(arr)

parameter = appender([1])
print(parameter)
'''
from multiprocessing.sharedctypes import Value
from random import choice, randint
# Декоратор - это функция, которая меняет поведение другой ф-и, при этом другая функция не меняется сама в себе
def ingredients(func):
    func()
    products = ['сыр', "бастурма", "салатный лист"]
    for ingredient in range(len(products)):
        print(choice(products))
    print("Другой хлебушек")

@ingredients
def bread():
    print('Хлебушек')

# property - это декоратор менеджер, который активирует действия на установку\изъятие и\или иное взаимодействие с объектами
# getter\setter - это декораторы, которые достают (getter) и устанавливают (setter) значения

class Test:
    
    @property
    def value(self):
        return randint(1, 10)

    @value.setter
    def set_value(self, value):
        print(f"До добавления единицы: {value}")
        print(f"До добавления единицы: {value + 1}")
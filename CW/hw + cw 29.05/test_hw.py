# Task 1 - Кошки, собаки
class Animal:   
    def say_voice(self):
        print('Животные издают звуки, да-да.')

class Cat(Animal):
    def say_voice(self):
        print('Мяу!')

class Dog(Animal):
    def say_voice(self):
        print('Гав!')

array = [Animal(), Cat(), Dog()]

# Task 2 - Get access
from random import randint

class User:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename
        self.__pwd = ''
        for elem in range(randint(8, 24)):
            self.__pwd += chr(randint(65,110))
            
    
    def __get_access(self):
        print(f'Name: {self.name}, Surename: {self.surename}, Pwd: {self.__pwd}')

    def return_pwd(self):
        return self.__pwd
# public, private (_), protected (__)

# Task 3 - Mistakes handling
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f"{self.name}s age is {self.age}"


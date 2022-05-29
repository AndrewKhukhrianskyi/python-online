from distutils.log import Log
from random import randint
'''
# Полиморфизм - пример
class Workers:
    def __init__(self):
        self.workers = ['Иван Иванов', 'Игорь Федоров', "Андрей Андропов"]

    def __del__(self):
        print(f"{self.workers.pop(randint(0, len(self.workers) - 1))} уволен!")
        print(f"Осталось сотрудников: {len(self.workers)}")
        print(f"Список сотрудников: {self.workers}")


works = Workers()

del works
'''
# Инкапсуляция - пример
# _ - не рекомендуется изменять эту переменную
# __ - не трогать эту переменную
class LogSystem:
    def __init__(self, userid):
        self.userid = userid
        self.__login = 'admin'
        self.__pwd = 'admin'
        # (self.__login, self.__pwd)

    def __login(self):
        print(f"Добро пожаловать, {self.userid}")

    def check_login(self, log_user, passwd):
        if log_user == self.__login and passwd == self.__pwd:
            print('Welcome!')
        else:
            print('Ошибка! Что-то не так!')
    
log = LogSystem(randint(1000,100000))   
print(LogSystem._LogSystem__login)




# Task 1 - Nikola
class Nikola:
    __slots__ = ['info']
    def __init__(self, info : dict):
        self.info = info
        if self.info['name'] != 'Николай':
            print(f"Я не {self.info['name']}, а Николай")
            self.info['name'] = "Николай"

#nikola = Nikola({'name': "Николай", "surename": "Иванов"})
#maxim = Nikola({'name': "Максим", "surename": "Иванов"})

# maxim.info['age'] = 25

# Task 2 - self

class Test:
    def do_smth():
        print('Hello')

# test = Test()
# test.do_smth() 

class Soda:
    def __init__(self, addings = None):
        self.addings = addings

    def show_my_drink(self):
        if self.addings is not None:  # Если ДОБАВКА не None
            print(f"Газировка и {self.addings}")
        else:
            print('Обычная газировка.')

soda = Soda()
soda_bread = Soda(addings = "Плюшка")


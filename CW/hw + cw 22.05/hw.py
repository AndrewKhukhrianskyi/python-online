from random import choice

'''
# Задачи 1-2 - Герои
class Hero:
    def __init__(self, hp: int, speed: int, damage: int, ability: str):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.ability = ability
    

class Chef(Hero):
    def __init__(self, hp: int, speed: int, damage: int, dishes: list):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.dishes = ['Суши', "Спагетти", "Начос"]
    def cook(self):
        print('Готовим еду...')
        print(f"Повар приготовил {choice(self.dishes)}!")

class Mechanic(Hero):
    def __init__(self, hp: int, speed: int, damage: int):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.cars = ['BMW X5', 'Audi TT', 'ВАЗ 2301']

    def repair(self):
        print('Чиним Машины...')
        print(f"Механик починил {choice(self.cars)}!")

class Gardener(Hero):
    def __init__(self, hp: int, speed: int, damage: int):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.trees = ['Береза', "Дуб", "Клен"]

    def plant(self):
        print('Садим деревья...')
        print(f"Садовник посадил {choice(self.trees)}!")

vintik = Mechanic(100, 100, 10)

gardener = Gardener(100, 100, 10)

for elem in range(3):
    gardener.plant() # садовник.посадить()
'''

# Задача 3 - Солдат

class Soldier:
    def __init__(self, role, action):
        self.role = role
        self.action = action

    def display_info(self):
        print(f"Это - {self.role}")
        print(f"Его действие - {self.action}")

class Marksman(Soldier):
    def shoot(self):
        print('Стреляем...')

class Pointer(Marksman):
    def mark(self):
        print('Ставим метку...')

class Sniper(Pointer):
    def accurate_shoot(self):
        print('Делаем точный выстрел...')

adam = Sniper('Снайпер', "Маскировка")
adam.display_info()
adam.accurate_shoot()
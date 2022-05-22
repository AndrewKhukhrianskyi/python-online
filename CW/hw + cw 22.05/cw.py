'''
class Animal:
    def __init__(self, paws: int):
        self.paws = paws
        self.sound = "Мяу!"
    def voice(self):
        print(self.sound)

class Horse(Animal):
    def eat_apple(self):
        print('Лошадь ест яблоки. Они очень вкусные...')
    
    def voice(self):
        self.sound = "Игого!"
        print(self.sound)

petsy = Horse(4)

petsy.voice()
petsy.eat_apple()
'''

# Pattern - Приемы, которые помогают эффективно решать задачи
# Anti-pattern - Приемы, которые усугбляют работу класса => ухудшают эффективность решения задач
# God Object - антипаттерн, когда класс умеет делать ВСЕ.
from random import choice

class Abilities:
    def __init__(self, abilities: list):
        self.abilities = abilities

    def set_ability(self):
        return choice(self.abilities)

    

class Hero:
    def __init__(self, hp: int, speed: int, damage: int, ability: str):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.ability = ability
    

class Chef(Hero):
    def cook(self):
        print('Готовим вкусную еду!')

class Mechanic(Hero):
    def repair(self):
        print('Чиним Машины')
        # определить список машин, которые может починить наш герой


skill = Abilities(['Золотые руки', "Жирдяй", "Крепкая челюсть", "СДВГ", "Эндоморф", "Хлюпик", "Астматик", "Алкоголик"])

vintik = Mechanic(100, 7, 20, skill.set_ability())

print(vintik.ability)
'''
# ==, <, >, >=, <=, !=
# Boolean, bool, Логический тип данных
# True\False => Истина\Ложь

# print(2 < 3) # True
# print(5 != 5) # False

# AND - И, OR - ИЛИ

hero = int(input('Выбери путь: '))
item = input('Что ты с собой взял? ')
if hero == 1 or item == 'меч':
    print('Cмерть найдешь!')

elif hero == 2 or item == 'кольца':
    print('Женился!')

elif hero == 3 or item == 'мешок': 
    print('Разбогател!')

else:
    print('Сохранил жизнь!')


# Статически типизированные
# Динамически типизированные
print(True + True + True)
print(int(True))

print(False - 2)

fives = []

while True:
    marks = input()
    if marks == '0':
        break
    a = list(map(int, marks.split()))
    for elem in a:
        if a == 5:
            fives.append(elem)
    print(b)
    print(f"Result: {int(len(b) / len(a) * 100)}")
    
from random import randint 

arr = []
even_list = []
# При каждом запуске цикла наши значения будут пополняться в промежутке от 5 до 20 цифр
for elem in range(randint(5, 20)):
    arr.append(randint(10, 100)) # добавляем в список случ число от 1 до 100

# Перебираем список случайных чисел
for even in arr:
    if even % 2 != 0:
        even_list.append(even)

print(f"Случайные числа: {arr}")
print(f"Результат (Нечетные числа): {even_list}")


array = [1, 'a', 'b', 3, 'www', 4, 'hello']
res = []

for elem in array:
    if type(elem) is str: # аналог is not int
        res.append(elem)

print(res)

from random import randint
class Warrior:
    att = 10
    hp = 100

    def get_hit(self, att):
        self.hp -= att
    
    def show_info(self):
        print(f"{self.hp} hit points remain")

h1 = Warrior()
h2 = Warrior()

while h1.hp != 0 and h2.hp != 0:
    if randint(1,2) == 1:
        print('Hero 1 is getting hit.')
        h1.get_hit(h2.att)
        h1.show_info()
    else:
        print('Hero 2 is getting hit.')
        h2.get_hit(h1.att)
        h2.show_info()

if h1.hp == 0:
    print('Hero 2 won')

else:
    print('Hero 1 won!')

from random import choice

class Worker:
    def __init__(self, name, surename, qual = 1):
        self.name = name
        self.surename = surename
        self.qual = qual
    
    def display_info(self):
        print(f"{self.name} {self.surename} - Quality: {self.qual}")

    def __del__(self):
        print(f'Good bye, {self.name} {self.surename}!')


w1 = Worker('Ethan', 'Connor', 5)
w2 = Worker('Bob', 'Rogers', 3)
w3 = Worker('Alan', 'Key', 5)

arr = [w1, w2, w3]

del w2
input()

# Task 1

class Soda:
    def __init__(self, drink = None):
        self.drink = drink
    
    def show_my_drink(self):
        if self.drink is None or not isinstance(self.drink, str):
            print('Обычная газировка')

        else:
            print(f"Газировка с {self.drink}")


# Task 2

class TriangleChecker:
    def __init__(self, sides : list):
        self.sides = sides

    def is_triangle(self):
        for side in self.sides:
            if isinstance(side, str):
                return 'Нужно вводить только числа!'
            elif side == 0:
                return "Треугольник нельзя построить!"
            elif side < 0:
                return "С отрицательными числами ничего не выйдет!"

        return "Ура! Я могу построить треугольник!"

# Task 3
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
    
    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
    

# Task 4
class Nicola:
    __slots__ = ['name', 'age']
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        if self.name != 'Николай':
            print(f'Я не {self.name}, а Николай.')

# Task 5
class Check:
    def __init__(self, *args):
        self.arr = []
        for arg in args:
            self.arr.append(arg)

    def check_word(self):
        for elem in range(len(self.arr)):
            for check_elem in range(len(self.arr)):

                if self.arr[elem] == self.arr[check_elem]:
                    continue
                elif len(self.arr[elem]) < len(self.arr[check_elem]):
                    print(f'Слово {self.arr[elem]} меньше, чем {self.arr[check_elem]} по кол-ву символов')
                elif len(self.arr[elem]) > len(self.arr[check_elem]):
                    print(f'Слово {self.arr[elem]} больше, чем {self.arr[check_elem]} по кол-ву символов')
                else:
                    print(f'Слово {self.arr[elem]} равно слову {self.arr[check_elem]} по кол-ву символов')

p = Check('Apple', 'Tree', 'Bite', 'CD', 'Clearing')
p.check_word()
'''
import pytest
# Pytest tasks
class TestMaths:
    def test_plus(self):
        a = 5
        b = 3
        assert a + b == 8
    
    def test_div(self):
        a = 10
        b = 2
        assert a // b == 5

    def test_multiply(self):
        a = 4
        b = 5
        assert a * b == 20

    def test_minus(self):
        a = 10
        b = 9
        assert a - b == 1

@pytest.mark.parametrize('answer, result', [([1,2,3], list)])
def test_type_list_checking(answer, result):
    answer = tuple(answer)
    assert isinstance(answer, result)

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
'''

from random import choice

members = ['Глеб', "Женя", "Александр"]
projects = ['Блокнот', "Калькулятор", "Шифратор (ROT)", "Викторина", "Органайзер"]

for member in members:
    reults = choice(projects)
    print(member, reults)


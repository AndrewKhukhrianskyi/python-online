# Синтаксический сахар - приемы, которые упрощают написание кода

'''
# 1 - создание переменной (input())
# Плохая практика
number = input('Введи число: ')
number = int(number)
# Хорошая практика
number = int(input('Введи число: '))

# 2 - Форматирование строк
from random import randint
# Плохая практика
print('Ваше число: ' + str(randint(1, 100)))
# Хорошая практика
print(f'Ваше число: {randint(1, 100)}')
'''

# 3 - Генераторы списков (List comprehension)
# Плохая практика
from random import randint
arr = []
for elem in range(randint(5, 20)):
    arr.append(randint(10, 1000))
# Хорошая практика
arr2 = [randint(10, 1000) for elem in range(randint(5, 20))]
#print(arr2)

# print([x * 2 + 4 for x in range(10)])

#[переменная for значение для цикла in range(...)]

# 4 - Тернарный оператор (Выражения) (if + else)
# Плохая практика
'''
if True:
    print(True)

else:
    print(False)
'''
# Хорошая практика
#print(1 if True else 2)

# действие если True иначе действие2
number = randint(1, 10)
#print(f'Четное число {number}' if number % 2 == 0 else f'Нечетное число {number}')

# Лямбда-выражения (анонимные функции)
# Плохая практика
def func(a, b):
    return a + b

# Хорошая практика (?) - Для маленьких выражений - ок, для больших - не очень
# add_2 = lambda arr: [arr[elem] for elem in range(len(arr))] if arr[elem] % 2 == 0 else False # add_2 теперь ф-я
# Лямбда выражение (анонимная функция) - это функция которая выполняется в одну строку и возвращает значение

# Генератор
# Итератор - это переборщик
# Итерируемый объект - перебираемый (списки, словари, кортежи, строки)
text = 'hello'


def fibonacci(n):
    fib_1, fib_2 = 1, 1
    for elem in range(n - 2):
        fib_1, fib_2 = fib_1 + fib_2, fib_1
    print(fib_1)

fibonacci(100000)
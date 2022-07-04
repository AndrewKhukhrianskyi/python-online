# Task 1
'''
numbers = iter(range(1, 1000001))
print(numbers)
# range - это "ленивый" итерируемый объект
# Ленивость объекта заключается в том, что он не сразу отображает все данные, сохраняет их под капотом, пока не произойдет вызов
# Решение 
print(next(numbers))
'''
# Task 2
from itertools import cycle

def infinite(lst, tries):
    result = ''
    iter_list = cycle(lst)
    if lst:
        for symbol in range(tries):
            result += str(next(iter_list))
    return result

# Task 3

def show_letters(some_str):
    clean_str = ''.join([letter for letter in some_str if letter.isalpha()])
    for symbol in clean_str:
        yield symbol

# yield from конструкция позволяет создать генератор через другой генератор, что по сути позволяет взаимодействовать с объектами
# как через цикл, так и иным способом. Их можно вкладывать сколько угодно раз.

def show_letters_v2(some_str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])

string = 'abcd'
show_str = show_letters_v2(string)
for elem in range(len(string)):
    print(next(show_str))

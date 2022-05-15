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
    '''

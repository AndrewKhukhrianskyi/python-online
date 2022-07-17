from random import randint

entry = input('В какую комнату нужно войти? ')
power = randint(0, 1)

if power == 1:
    print("Статус света: Включен")
    print(f'Выйти из комнаты #{entry}')
else:
    print("Статус света: Выключен")
    print('Ищем выключатель...')
    status = int(input('Дотягиваемся? (1 - Да, 0 - Нет): '))
    if status == 1:
        print('Включить свет')
        print(f'Выйти из комнаты #{entry}')
    elif status == 0:
        print('Нужно сделать шаг!')
    else:
        print("Ошибка!")
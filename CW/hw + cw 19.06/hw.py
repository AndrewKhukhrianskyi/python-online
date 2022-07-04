# Task 1 - Улучшить код. Часть 1
def test1():
    arr = []
    for elem in range(5):
        arr.append(elem * 4)
    print(arr)

    # Правильное решение
    arr1 = [elem * 4 for elem in range(5)]
    print(arr1)

# Task 2 - Улучшить код. Часть 2
name = 'Иван'
surname = 'Пупкин'
age = 30
status = 'Женат'

print(f"Имя: {name},\n Фамилия: {surname},\n Возраст: {age},\n Семейное положение: {status}")
"""
pytest - это модуль (библиотека) который позволяет проводить тестирование кода программы
UNIT-тестирование - это тесты, которые проверяют функциональность кода программы
"""
import pytest
import logging 
# assert - это команда которая позволяет проверять истинность результата
# assert True -> Все окей
# assert False -> Программа завершает работу с ошибкой

# Если вы пользуетесь pytest, то в начале имени файла, функции, Класса и тд должно фигурировать название test
#def test_odd_even1(num):
#    return num % 2

# Pytest декораторы - это наборы сущностей, которые оборачивают функцию для ее тестирования.
# @pytest.mark
# @pytest.fixture
# @pytest.mark - это декораторы, которые занимаются координированием теста
# @pytest.mark.parametrize - это декоратор, который повторяет запуск теста с новым значением

@pytest.mark.parametrize('num', ([2, 4, 6, 1, 6, 7, 9, 10, 11, 22, 0, 44, 57]))
def test_odd_even2(num):
    logging.info(f'Check {num}')
    if num % 2 == 0:
        assert num % 2 == 0
    elif num % 2 == 1:
        assert num % 2 == 1
    else:
        assert False

@pytest.mark.parametrize('word', (['Hello', 'Bob', '123421', 'ddd']))
def test_is_word(word):
    assert type(word) is str

@pytest.mark.parametrize('num', ([1, 1.0, 2, 3.25, 4]))
def test_is_number(num):
    assert type(num) is int or type(num) is float 

# Если мы хотим запускать отдельную функцию или класс, то нужно прописать в командной строке (cmd)
# pytest название файла::название функции или класса
# Название классов должно начинатся с большой буквы и названия Test
# Пример: TestClass
@pytest.mark.parametrize('num,num2,operation', ([1, 2 '+']))
def test_calculator(num, num2, operation):
    ...
 
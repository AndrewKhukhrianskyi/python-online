import pytest

from random import randint 

def test_true(before_test): # Чтобы фикстура заработала, нужно указать ее имя перед запуском теста
    num = before_test # Сохранили сюда двойку
    assert num == 2

#@pytest.mark.parametrize('number', [randint(1, 10) for elem in range(5)])
#@pytest.mark.parametrize('number2', [randint(1, 10) for elem in range(5)])
def func(number, number2):
    return number + number2 

# Bad practice
for elem in range(3):
    assert func(1, elem) > 0

# Test class
class TestClass: # Test suite
    @pytest.fixture(scope='class')
    def return_number(class_fixture):
        number = class_fixture
        return number + 1

    def test_number(self, return_number):
        number = return_number
        assert number == 6


def test_main(module_fixture):
    def test_1():
        assert module_fixture + 1 == 2  
    def test_2():
        assert module_fixture + 2 == 3

# module == package
def test_main(package_fixture):
    def test_1():
        assert package_fixture + 1 == 2  
    def test_2():
        assert package_fixture + 2 == 3
    
def test_files(session_fixture):
    assert session_fixture == 2

def test_files2(session_fixture):
    assert session_fixture == 2
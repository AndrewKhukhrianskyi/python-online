import pytest
# Task 1 - Calculator
def test_runner(send_numbers):
    number = send_numbers[0] # Тут число 4
    number2 = send_numbers[1] # Тут число 2
    def calculator(number, number2, oper):
        if oper == '+':
            return number + number2
        elif oper == '-':
            return number - number2
        elif oper == '*':
            return number * number2
        elif oper == '/':
            return number / number2
        else:
            return False
    operations = ['+', '-', '*', '/']
    for operation in operations:
        if operation == '+':
            # Case 1
            assert calculator(number, number2, '+') == 6
        elif operation == '-':
            # Case 2
            assert calculator(number, number2, '-') == 2
        elif operation == '*':
            # Case 3
            assert calculator(number, number2, '*') == 8
        elif operation == '/':
            # Case 4 
            assert calculator(number, number2, '/') == 2.0

# Task 2 - Check pwd
@pytest.mark.parametrize('pwd', (['admin', 'морковка', 'число', 'Неправильный_пароль', 'admin111']))
def test_pwd(check_pwd, pwd):
    pwds = check_pwd
    assert pwd in pwds
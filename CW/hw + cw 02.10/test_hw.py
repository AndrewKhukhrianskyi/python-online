# Task 1 - Калькулятор
import pytest
import os
# Practice-like
@pytest.mark.parametrize('number',([12]))
@pytest.mark.parametrize('number2',([4]))
def test_runner(number,number2):
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
            assert calculator(number, number2, '+') == 16
        elif operation == '-':
            # Case 2
            assert calculator(number, number2, '-') == 8
        elif operation == '*':
            # Case 3
            assert calculator(number, number2, '*') == 48
        elif operation == '/':
            # Case 4 
            assert calculator(number, number2, '/') == 3.0

    # Negative case
    assert calculator(number, number2, '46326435432frsdfs') == False

# Task 2 - Test file works
@pytest.mark.parametrize('file_name',(['test.txt']))
@pytest.mark.parametrize('text',(['Hello!']))
def test_file(file_name, text):
    file = open(file_name, 'w')
    # Check that file was created
    assert os.path.exists(file_name)
    file.write(text)
    file.close()
    file = open(file_name, 'r')
    file_text = str(file.readline())
    # Check that data was written to the file
    assert text in file_text  
    file.close()
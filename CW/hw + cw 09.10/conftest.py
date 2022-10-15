import pytest
# Фикстуры могут запускаться из другого файла. Для этого его нужно назвать как conftest.py
# scope = function (по умолчанию)
@pytest.fixture() 
def before_test():
    number = 2
    return number

# scope = class
@pytest.fixture(scope='class')
def class_fixture():
    return 5

# scope = module
@pytest.fixture(scope='module')
def module_fixture():
    return 1

# package = module
@pytest.fixture(scope='package')
def package_fixture():
    return 1

# package = session
@pytest.fixture(scope='session')
def session_fixture():
    return 2
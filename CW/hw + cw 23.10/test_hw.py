from operator import add
from selenium.webdriver.common.by import By # По какой характеристике ищем 

import pytest

# Test Case 1 - Check Address
def test_check_address(open_browser):
    browser = open_browser
    # Проверить, что адрес отображается на странице
    expected_text = 'Днепр, пр. Правды, 143'
    # Есть ли блок
    address = browser.find_element(by = By.XPATH, value = '//div[@class="company-contacts"]/div[2]')
    assert address.is_displayed
    # Правильный ли в нем текст? (Тут мы находим баг)
    actual_text = address.text
    assert expected_text == actual_text
    browser.close()

# Test Case 2 - Check Switch Language (UA)
@pytest.mark.selenium_bug
def test_check_language(open_browser):
    browser = open_browser
    language_block_text = browser.find_element(by = By.XPATH, value = "//div[@class='top-language']/a")
    # Есть ли блок 
    assert language_block_text.is_displayed
    ukrainian = language_block_text.text
    # Нажимаем на неe
    language_block_text.click()
    another_language = language_block_text.text
    # Проверяем, что название кнопки изменилось после переключения
    assert ukrainian != another_language
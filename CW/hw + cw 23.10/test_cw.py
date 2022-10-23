
import pytest

from selenium.webdriver.common.by import By # По какой характеристике ищем 

from browser import open_browser

def test_check_company_name():
    browser = open_browser()
    company_name_block = browser.find_element(by = By.CLASS_NAME, value = 'company-name')
    # Проверка 1
    # Проверить, что блок с названием компании отображается
    assert company_name_block.is_displayed() # is_displayed() - отображается ли панель
    browser.close()

def test_check_text():
    browser = open_browser()
    expected_result = 'Пятый элемент-Днепр'
    company_name = browser.find_element_by_xpath("//div[@class='company-name']/div[@class='c-name']/h1")
    actual_result = company_name.text # .text() - вытаскивает текстовую информацию из блока
    # Проверка 2
    # Проверить, что текст не совпадает с ожидаемым текстом (По сути: Баг)
    expected_result is not actual_result
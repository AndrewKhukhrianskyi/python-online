from browser import open_browser

from selenium.webdriver.common.by import By # По какой характеристике ищем 

def test_check_text():
    browser = open_browser()
    expected_result = 'Пятый элемент-Днепр'
    company_name = browser.find_element(by = By.XPATH, value = "//div[@class='company-name']/div[@class='c-name']/h1")
    actual_result = company_name.text # .text - вытаскивает текстовую информацию из блока
    # Проверка 2
    # Проверить, что текст совпадает с ожидаемым текстом
    print(expected_result != actual_result)

test_check_text()
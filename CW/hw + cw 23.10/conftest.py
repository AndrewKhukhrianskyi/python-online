from selenium import webdriver

import pytest

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome()
    browser.get("https://5element-dnepr.promobud.ua/") # меняем название сайта на который будем заходить
    return browser


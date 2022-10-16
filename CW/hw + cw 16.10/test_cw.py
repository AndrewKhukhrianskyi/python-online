import pytest
from selenium import webdriver

from browser import open_browser
# Проверить, что пользователь зашел на сайт 5element
def test_open_link():
    browser = open_browser()
    assert browser.current_url == "https://5element-dnepr.promobud.ua/"
    browser.quit()
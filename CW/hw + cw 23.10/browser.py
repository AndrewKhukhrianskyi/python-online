from selenium import webdriver


def open_browser():
    browser = webdriver.Chrome()
    browser.get("https://5element-dnepr.promobud.ua/") # меняем название сайта на который будем заходить
    return browser
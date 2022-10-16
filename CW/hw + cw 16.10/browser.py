import pytest
from selenium import webdriver
from time import sleep

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://5element-dnepr.promobud.ua/") # меняем название сайта на который будем заходить
    return driver
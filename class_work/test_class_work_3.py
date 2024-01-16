from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check
import time, allure, pytest


@allure.suite('testsuite')
@allure.title('testtitle')
def test_classwork_5():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://demoqa.com/")

    elements1 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[1]//h5")
    elements2 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[2]//h5")
    elements3 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[3]//h5")
    elements4 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[4]//h5")
    elements5 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[5]//h5")

    # check.equal(elements1, '1234', 'Ошибка теста или текст неверный')
    # check.equal(elements2, '2342', 'Ошибка теста или текст неверный')
    # check.equal(elements3, '4334', 'Ошибка теста или текст неверный')
    # check.equal(elements4, '3433', 'Ошибка теста или текст неверный')
    # check.equal(elements5, '43334', 'Ошибка теста или текст неверный')

    elements = [
        (elements1.text, 'Elements', 'Неверный текст первого элемента'),
        (elements2.text, 'Forms', 'Неверный текст второго элемента'),
        (elements3.text, 'Alerts, Frame & Windows', 'Неверный текст третьего элемента'),
        (elements4.text, 'Widgetss', 'Неверный текст четвертого элемента'),
        (elements5.text, 'Interactions', 'Неверный текст пятого элемента')
    ]

    for pervu, vtoroi, treti in elements:
        check.equal(pervu, vtoroi, treti)

#
# def test_classwork_55():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     driver.get("https://demoqa.com/")
#
#     elements1 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[1]//h5").is_displayed()
#     elements2 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[2]//h5").is_displayed()
#     elements3 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[3]//h5").is_displayed()
#     elements4 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[4]//h5").is_displayed()
#     elements5 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[5]//h5").is_displayed()
#
#     elements = [
#         (elements1, 'Неверный текст первого элемента'),
#         (elements2, 'Неверный текст второго элемента'),
#         (elements3, 'Неверный текст третьего элемента'),
#         (elements4, 'Неверный текст четвертого элемента'),
#         (elements5, 'Неверный текст пятого элемента')
#     ]
#
#     for pervu, vtoroi in elements:
#         check.is_true(pervu, vtoroi)
#
#
# def test_classwork_555():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     driver.get("https://demoqa.com/")
#
#     elements1 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[1]//h5")
#     elements2 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[2]//h5")
#     elements3 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[3]//h5")
#     elements4 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[4]//h5")
#     elements5 = driver.find_element(By.XPATH, " (//div[@class='card mt-4 top-card'])[5]//h5")
#
#     elements = [
#         (elements1, 'Elements', 'Неверный текст первого элемента'),
#         (elements2, 'Forms', 'Неверный текст второго элемента'),
#         (elements3, 'Alerts, Frame & Windows', 'Неверный текст третьего элемента'),
#         (elements4, 'Widgets', 'Неверный текст четвертого элемента'),
#         (elements5, 'Interactions', 'Неверный текст пятого элемента')
#     ]
#
#     for pervu, vtoroi, treti in elements:
#         if check.is_true(pervu.is_displayed(), vtoroi):
#             check.equal(pervu.text, vtoroi, treti)

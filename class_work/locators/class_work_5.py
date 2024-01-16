import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tatyana_Malahova.class_work.locators.locators_page_elements import LocatorsForms
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from Tatyana_Malahova.diploma.pages.base_page import BasePage
from Tatyana_Malahova.diploma.pages.locators import autorization_page_locators
import allure


def test_classwork_111():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.zalando.pl/kobiety-home/")

    def go_to_login_screen(self):
        with allure.step("Нажать кнопку войти на главном экране"):
            time.sleep(5)
            menu = self.find_element(autorization_page_locators.picture_autorization)
            ActionChains(self.driver).move_to_element(menu).click(autorization_page_locators.log_in_in_window).perform()
            time.sleep(5)

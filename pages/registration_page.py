import time

import allure

from pages.base_page import BasePage

from pages.locators import autorization_page_locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_item_in_cart(self):
        with allure.step("Проверка регистрации"):
            menu = self.find_element(autorization_page_locators.picture_autorization)
            ActionChains(self.driver).move_to_element(menu).click(autorization_page_locators.log_in_in_window).perform()

    def add_first_client(self):
        self.find_element(autorization_page_locators.name).click()
        self.find_element(autorization_page_locators.name).send_keys('Tatyana')
        time.sleep(1)
        self.find_element(autorization_page_locators.surname).click()
        self.find_element(autorization_page_locators.surname).send_keys('Malahova')
        time.sleep(1)
        self.find_element(autorization_page_locators.e_mail_address_first).click()
        self.find_element(autorization_page_locators.e_mail_address_first).send_keys(
            'gykivtujnbgakokaun@cazlq.com')
        time.sleep(1)
        self.find_element(autorization_page_locators.password_first).click()
        self.find_element(autorization_page_locators.password_first).send_keys('qwertyui1278')
        time.sleep(1)
        self.find_element(autorization_page_locators.agree_rules).click()
        time.sleep(1)
        self.find_element(autorization_page_locators.button_register).click()
        time.sleep(1)

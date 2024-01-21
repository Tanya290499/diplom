import time

from selenium.common import NoSuchElementException

import allure

from pages.base_page import BasePage
from pages.locators import cart_page_locators, clothes_page_locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_item_was_added_to_cart(self, title):
        with allure.step("Проверка наличия выбранных товаров"):
            item_in_cart_title = \
                self.find_element(cart_page_locators.first_element_title_in_cart).text
            assert title == item_in_cart_title

    def remove_item_from_cart(self):
        with allure.step("Нажать на кнопку удалить"):
            self.find_element(cart_page_locators.remove_from_cart_button).click()
            time.sleep(3)

    def check_is_items_in_cart(self, quantity='1'):
        with allure.step("Проверка наличия выбранных товаров"):
            try:
                items_in_cart = \
                    self.find_element(clothes_page_locators.cart_quantity_badge)
                assert items_in_cart.text == quantity
            except NoSuchElementException:
                if quantity == '0':
                    assert True
                else:
                    assert False

    def select_multiple_items_in_cart(self):
        with allure.step("Выбрать несколько товаров"):
            self.find_element(cart_page_locators.select_multiple_items).click()
            self.find_element(cart_page_locators.select_option_2).click()
            time.sleep(1)

    def get_item_price(self):
        with allure.step("Получить цену"):
            price = self.find_element(cart_page_locators.first_element_price).text
            return self.convert_price_text_to_number(price)

    def check_price_has_increased(self, initial_price, multiplier):
        final_price = self.get_item_price()
        with allure.step("Проверка увеличения цены"):
            assert final_price == initial_price * multiplier

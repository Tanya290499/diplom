import time

# from selenium.webdriver import ActionChains

from pages.base_page import BasePage
import allure
from selenium.webdriver.common.action_chains import ActionChains

from pages.locators import clothes_page_locators, autorization_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://www.zalando.pl/kobiety-home/')
            time.sleep(5)
            self.accept_cookies()

    def go_to_login_window(self):
        with allure.step("Нажать кнопку войти на главном экране"):
            actions = ActionChains(self.driver)
            time.sleep(1)
            login_icon = self.find_element(autorization_page_locators.picture_autorization)
            actions.move_to_element(login_icon).perform()
            time.sleep(1)

    def go_to_login_screen(self):
        with allure.step("Перейти на страницу авторизации"):
            self.go_to_login_window()
            self.find_element(autorization_page_locators.picture_autorization).click()
            time.sleep(1)

    def go_to_registration_screen(self):
        with allure.step("Перейти на страницу регистрации"):
            self.go_to_login_window()
            self.find_element(autorization_page_locators.log_in_in_window).click()
            time.sleep(1)

    def fill_login_inputs_valid_data_and_submit(self):
        with allure.step("Заполнить поле логин"):
            self.find_element(autorization_page_locators.e_mail_address_second) \
                .send_keys("gykivtujnbgakokaun@cazlq.com")
            time.sleep(2)
        with allure.step("Заполнить поле пароль"):
            self.find_element(autorization_page_locators.password_second).send_keys("qwertyui1278")
            time.sleep(2)
        with allure.step("Нажать кнопку войти"):
            self.find_element(autorization_page_locators.log_in).click()

    def go_to_favourites(self):
        with allure.step("Нажать кнопку избранных товаров"):
            self.find_element(autorization_page_locators.button_favorites).click()
        with allure.step("Нажать кнопку всех избранных товаров"):
            self.find_element(autorization_page_locators.all_favorites).click()

    def check_is_in_favourites(self, item_that_was_added_title, item_that_was_added_description):
        with allure.step("Проверка наличия выбранных товаров"):
            item_in_favourites_title = \
                self.find_element(clothes_page_locators.first_element_title)
            item_in_favourites_description = \
                self.find_element(clothes_page_locators.first_element_title)

            assert item_that_was_added_title == item_in_favourites_title.text
            assert item_that_was_added_description == item_in_favourites_description.text

    def add_items_to_cart(self):
        time.sleep(2)
        with allure.step("Нажать кнопку товара из раздела спорт"):
            button_sport_all = self.find_element(autorization_page_locators.button_sport_all_things)
            ActionChains(self.driver).move_to_element(button_sport_all) \
                .click(autorization_page_locators.button_sport_all_things).perform()
        item_that_was_added_title = self.find_element(
            clothes_page_locators.first_element_title
        )
        item_that_was_added_description = \
            self.find_element(clothes_page_locators.first_element_description)
        with allure.step("Нажать кнопку 'like' первого товара"):
            self.find_element(clothes_page_locators.like_first_element).click()
        self.go_to_favourites()
        self.check_is_in_favourites(
            item_that_was_added_title.text,
            item_that_was_added_description.text
        )

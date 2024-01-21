import allure

from pages.locators import autorization_page_locators
from pages.base_page import BasePage


class FeedbackPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_name_input(self):
        with allure.step("Заполнить поле 'Имя'"):
            self.find_element(autorization_page_locators.name).send_keys("Tatyana")

    def fill_last_name_input(self):
        with allure.step("Заполнить поле 'Фамилия'"):
            self.find_element(autorization_page_locators.surname).send_keys("Malahova")

    def fill_email_input(self):
        with allure.step("Заполнить поле 'Почта'"):
            self.find_element(autorization_page_locators.e_mail_address_first).send_keys("something_email@mail.com")

    def fill_password_input(self):
        with allure.step("Заполнить поле 'Пароль'"):
            self.find_element(autorization_page_locators.password_first).send_keys("qwertyui1278")

    def click_fashion_category(self):
        with allure.step("Нажать кнопку 'Нет предпочтений'"):
            self.find_element(autorization_page_locators.no_preference).click()

    def click_approval_checkbox(self):
        with allure.step("Нажать кнопку 'Да, я хочу получать рассылку об интересных предложениях'"):
            self.find_element(autorization_page_locators.agree_rules).click()

    def click_submit_button(self):
        with allure.step("Подтвердить отправку формы"):
            self.find_element(autorization_page_locators.button_register).click()

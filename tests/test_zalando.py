import pytest

# from class_work.diplom.pages.profile_page import ProfilePage
import allure
from pages.registration_page import RegistrationPage
from pages.home_page import HomePage


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Регистрация")
@allure.title("Регистрация пользователя")
def test_register(driver):
    home_page = HomePage(driver)
    registration_page = RegistrationPage(driver)
    home_page.open()
    home_page.go_to_registration_screen()
    registration_page.add_first_client()


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Авторизация")
@allure.title("Авторизация пользователя с валидными данными")
def test_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_login_screen()
    home_page.fill_login_inputs_valid_data_and_submit()


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Избранное")
@allure.title("Добавление товара в избранное")
def test_favourites(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_login_screen()
    home_page.fill_login_inputs_valid_data_and_submit()
    home_page.add_items_to_cart()

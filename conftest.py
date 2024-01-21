import pytest, requests, logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fp.fp import FreeProxy


@pytest.fixture()
def driver():
    credentials = {
        "firstName": 'John',
        "lastName": 'Doe',
        "email": 'zyt15524@zbockeer.com',
        "password": '12223fret4t5g555'
    }

    options = Options()
    proxy = FreeProxy(country_id='PL', timeout=0.3, rand=True).get()
    pro = '209.121.164.50'
    options.add_argument("--proxy-server=%s" % pro)
    options.add_argument("lang=pl-PL")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    driver.credentials = credentials

    yield driver
    driver.quit()

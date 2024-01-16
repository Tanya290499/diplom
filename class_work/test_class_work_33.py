import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tatyana_Malahova.class_work.locators.locators_page_elements import LocatorsForms


def test_classwork_111():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/")

    driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[text()='Text Box']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, LocatorsForms.full_name).send_keys('Tatyana Malahova')
    time.sleep(1)
    driver.find_element(By.XPATH, LocatorsForms.email).send_keys('something_email@mail.com')
    time.sleep(1)
    driver.find_element(By.XPATH, LocatorsForms.currentAddress) \
        .send_keys('Minsk,Independence Avenue, 123, 67')
    time.sleep(1)
    driver.find_element(By.XPATH, LocatorsForms.permanentAddress) \
        .send_keys('Minsk,Independence Avenue, 123, 67')
    time.sleep(1)
    driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(2)

    elements = driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']").is_displayed()
    print(elements)
    driver.close()
    driver.quit()

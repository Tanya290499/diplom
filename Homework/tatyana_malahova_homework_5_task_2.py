import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")

driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//li[@class='btn btn-light ' and @id='item-2'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "(//div[@class='custom-control custom-radio custom-control-inline'])[1]") \
    .click()
time.sleep(5)
element = driver.find_element(By.XPATH, "//p[@class='mt-3']").is_displayed()
assert element is True
time.sleep(3)

driver.close()
driver.quit()

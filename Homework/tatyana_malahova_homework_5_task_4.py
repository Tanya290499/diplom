import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")

driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
time.sleep(3)
driver.find_element(By.XPATH, "(//li[@class='btn btn-light '])[5]").click()
time.sleep(3)
element = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action = ActionChains(driver)
action.double_click(element)
action.perform()
time.sleep(3)
element = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(element).perform()
time.sleep(3)
driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()
time.sleep(3)

driver.close()
driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")

driver.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//li[@class='btn btn-light '])[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='rct-option rct-option-expand-all']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//label[@for='tree-node-desktop']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//label[@for='tree-node-workspace']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
time.sleep(3)
driver.find_element(By.XPATH, "//label[@for='tree-node-office']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//label[@for='tree-node-downloads']").click()
time.sleep(3)

driver.close()
driver.quit()

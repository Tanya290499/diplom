import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# option = Options()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://hoster.by/")

# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//input[@class='m-input m-b1']").click()
# driver.implicitly_wait(5)


driver.find_element(By.XPATH, "//input[@class='m-input m-b1']").send_keys('vjgvv')
time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='search-button-text m-font-l1']").click()

time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='accept']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='domain_бел']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='domain_monster']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='domain_best']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='domain_online']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='domain_com']").click()
time.sleep(1)
# driver.find_element(By.XPATH, "(//input[@class='auth-input auth-input_primary auth-input_base auth-form__input auth-form__input_width_full'])[1]").clear()
# driver.implicitly_wait(5)
# element = driver.find_element(By.XPATH, "//span[@class='search-button-text m-font-l1']").get_attribute('placeholder')


element = driver.find_element(By.XPATH, "//button[@id='domain']").is_displayed()
assert element == True
print(element)

# driver.execute_script("""window.open('https://yandex.by/')""")
# time.sleep(2)


driver.close()
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#option = Options()
#option.add_argument("--window-size=1200,800")
driver = webdriver.Chrome()
driver.maximize_window()

#driver.get("https://www.onliner.by/")
#driver.get("https://hoster.by/")
#driver.get("https://www.tesla.com/")
driver.get("https://5element.by/")

#element = driver.find_element(By.XPATH, "//header[@class='b-main-page-blocks-header-2 cfix']//a[@href='https://money.onliner.by']").text
#element = driver.find_element(By.XPATH, "//h1[@class='intro-title m-font-hl1']").text
#element = driver.find_element(By.XPATH, "(//h1[@class='tcl-homepage-hero__heading tds-colorscheme--dark'])[1]").text
element = driver.find_element(By.XPATH, "(//div[@class='section-heading__title'])[1]").text
time.sleep(5)

print(element)

print(driver.title)
#print(driver.current_url)
#print(driver.page_source)


driver.close()
driver.quit()

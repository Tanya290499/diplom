import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
driver = webdriver.Chrome()
driver.maximize_window()


def print_webpage_data(url: str, locator: str):
    try:
        driver.get(url)
        element = driver.find_element(By.XPATH, locator).text
        print(element)
        print(driver.title)
        print(driver.current_url)
        # print(driver.page_source)
    except NoSuchElementException:
        print("NoSuchElementDetected on link:", url)
    finally:
        time.sleep(1)


GOOGLE_URL = "https://www.google.com/"
GOOGLE_LOCATOR = "//div[@id='SIvCob']"
print_webpage_data(GOOGLE_URL, GOOGLE_LOCATOR)

YOUTUBE_URL = "https://www.youtube.com/"
YOUTUBE_LOCATOR = "(//yt-formatted-string[@id='video-title'])[1]"
print_webpage_data(YOUTUBE_URL, YOUTUBE_LOCATOR)

FACEBOOK_URL = "https://www.facebook.com/"
FACEBOOK_LOCATOR = "//h2[@class='_8eso']"
print_webpage_data(FACEBOOK_URL, FACEBOOK_LOCATOR)

INSTAGRAM_URL = "https://www.instagram.com/"
INSTAGRAM_LOCATOR = "//*[text()='У вас ещё нет аккаунта? ']"
print_webpage_data(INSTAGRAM_URL, INSTAGRAM_LOCATOR)

TWITTER_URL = "https://twitter.com/"
TWITTER_LOCATOR = "(//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'])[2]"
print_webpage_data(TWITTER_URL, TWITTER_LOCATOR)

BAIDU_URL = "https://www.baidu.com/"
BAIDU_LOCATOR = "(//span[@class='title-content-title'])[3]"
print_webpage_data(BAIDU_URL, BAIDU_LOCATOR)

WIKIPEDIA_URL = "https://www.wikipedia.org/"
WIKIPEDIA_LOCATOR = "//strong[@class='jsl10n localized-slogan']"
print_webpage_data(WIKIPEDIA_URL, WIKIPEDIA_LOCATOR)

YAHOO_URL = "https://www.yahoo.com/?guccounter=1"
YAHOO_LOCATOR = "//a[@class='_yb_io0r2 _yb_1hru9 _yb_1jh73 _yb_1gfxm']"
print_webpage_data(YAHOO_URL, YAHOO_LOCATOR)

DZEN_URL = "https://dzen.ru/?yredirect=true"
DZEN_LOCATOR = "(//span[@class='card-news-story__text-3F'])[1]"
print_webpage_data(DZEN_URL, DZEN_LOCATOR)

WHATSAPP_URL = "https://www.whatsapp.com/"
WHATSAPP_LOCATOR = "(//div[@class='_8l_f'])[6]"
print_webpage_data(WHATSAPP_URL, WHATSAPP_LOCATOR)

AMAZON_URL = "https://www.amazon.com/"
AMAZON_LOCATOR = "(//a[@class='nav-a  '])[2]"
print_webpage_data(AMAZON_URL, AMAZON_LOCATOR)

TIKTOK_URL = "https://www.tiktok.com/explore"
TIKTOK_LOCATOR = "//h2[@id='login-modal-title']"
print_webpage_data(TIKTOK_URL, TIKTOK_LOCATOR)

driver.close()
driver.quit()

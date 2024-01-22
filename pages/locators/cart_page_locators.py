from selenium.webdriver.common.by import By

log_in = (By.XPATH, "//a[@data-id='login-button']")
continue_shopping_button = (By.XPATH, "//a[@data-id='continue-shopping-button']")
first_element_price = (
    By.XPATH, "//span[@class='z-2-text z-coast-base__price-current z-2-text-body-small-bold z-2-text-black']"
)
first_element_title_in_cart = (
    By.XPATH, "//h3[@class='z-2-text z-coast-base__article__brand z-2-text-body-small-regular z-2-text-black']"
)
remove_from_cart_button = (
    By.XPATH, "//button[@data-id='article-remove']"
)
select_multiple_items = (
    By.XPATH, "//select[@class='z-2-dropdown__control']"
)
select_option_2 = (
    By.XPATH, "//option[@value='2']"
)

from selenium.webdriver.common.by import By

header_search_input = (By.XPATH, "//input[@id='header-search-input']")

first_element_card = (
    By.XPATH, "(//a[@class='_LM JT3_zV CKDt_l CKDt_l LyRfpJ'])[1]")
first_element_title = (
    By.XPATH, "(//h3[@class='FtrEr_ lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'])[1]")
item_select_size = (
    By.XPATH, "//button[@data-testid='pdp-size-picker-trigger']"
)
item_select_first_size = (
    By.XPATH, "(//label[@data-testid='pdp-stockAvailable-label'])[1]"
)
add_to_cart_button = (
    By.XPATH, "(//div[@data-testid='pdp-add-to-cart']//button)[1]"
)
cart_popup_icon = (
    By.XPATH, "//a[@data-testid='cart-link']"
)
cart_popup_button = (
    By.XPATH, "//a[@href='/cart']"
)
cart_quantity_badge = (
    By.XPATH, "//div[@data-testid='shopping-bag-badge']//span"
)

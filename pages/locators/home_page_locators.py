from selenium.webdriver.common.by import By

female_fashion = (
    By.XPATH, "(//label[@class='sjPORp KxHAYs _2kjxJ6 FxZV-M JT3_zV _5Yd-hZ _4F506m RKlRH1'])[1]"
)
male_fashion = (
    By.XPATH, "(//label[@class='sjPORp KxHAYs _2kjxJ6 FxZV-M JT3_zV _5Yd-hZ _4F506m RKlRH1'])[2]")
no_preference = (
    By.XPATH, "(//label[@class='sjPORp KxHAYs _2kjxJ6 FxZV-M JT3_zV _5Yd-hZ _4F506m RKlRH1'])[3]"
)
button_register = (
    By.XPATH, "//button[@data-name='sso_register_register']"
)
agree_rules = (
    By.XPATH, "//label[@class='RyEgWR KxHAYs _2kjxJ6 FxZV-M r1svAh JT3_zV _5Yd-hZ _4F506m IxoCOT']"
)
cookies_accept_button = (By.XPATH, "//button[@id='uc-btn-accept-banner']")
button_sport_all = (By.XPATH, "//a[@href='https://www.zalando.pl/sport-kobiety/']")
button_favorites = (By.XPATH, "//div[@class='egPhqr navToolItem-wishlist']")
all_favorites = (By.XPATH, "(//span[@class='sDq_FX _2kjxJ6 FxZV-M Yb63TQ SpRgR2 r9BRio'])[1]")
picture_first = (
    By.XPATH, "(//img[@class='sDq_FX lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy'])[1]"
)
picture_second = (
    By.XPATH, "(//img[@class='sDq_FX lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy'])[2]"
)
search_input = (By.XPATH, "//input[@id='header-search-input']")
search_input_clear_button = (By.XPATH, "//button[@class='w5w9i_ l_QGWg']")

top_button = (
    By.XPATH,
    "//button[@class='uyF88V _4nHCvm jUq7Qy KbWDUM Rt7sMf _6-WsK3 Md_Vex Nk_Omi _MmCDa h14nQ_ _5PMpaO _9bYLON']")

newsletter = (By.XPATH, "//div[@class='CKDt_l']")
newsletter_email_input = (By.XPATH, "//input[@id='email-input']")
newsletter_women_category = (By.XPATH, "//label[@for='category-1']")
newsletter_submit = (By.XPATH, "//button[@type='submit']")
newsletter_error_no_email = (By.XPATH, "//*[contains(text(), 'Podaj poprawny adres e-mail')]")
newsletter_error_no_category = (By.XPATH, "//*[contains(text(), 'Wybierz jedną z opcji')]")
newsletter_success = (By.XPATH, "(//h4[@class='sDq_FX jeeWRj FxZV-M HlZ_Tf'])[2]")

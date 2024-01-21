from selenium.webdriver.common.by import By

picture_autorization = (
    By.XPATH, '(//*[@id="header-user-actions-container"]//div[@role="presentation" and @aria-haspopup="true"])[1]')
log_in_in_window = (By.XPATH, "//span[@class='_ZDS_REF_SCOPE_ smZi2j']")
new_client_in_window = (By.XPATH, "//span[@class='_ZDS_REF_SCOPE_ smZi2j']")
text_welcome = (By.XPATH, "//div[@class='Wn-EjT']")
e_mail_address_second = (By.XPATH, "//input[@id='login.email']")
password_second = (By.XPATH, "//input[@id='login.secret']")
log_in = (By.XPATH, "//button[@data-testid='login_button']")
forgot_password = (By.XPATH, "//span[@class='KxHAYs _2kjxJ6 dgII7d sxs3x9']")
register = (By.XPATH, "//button[@data-testid='toggle_register_button']")
text_first_time_here = (By.XPATH, "(//h3[@class='KxHAYs gr9aYh FxZV-M _4F506m'])[2]")
text_privacy_policy = (By.XPATH, "//li[@data-testid='footer_privacy_policy']")
text_reglament = (By.XPATH, "//li[@data-testid='terms_of_use']")
text_company_data = (By.XPATH, "//li[@data-testid='footer_legal_notice']")
name = (By.XPATH, "//input[@name='register.first_name']")
surname = (By.XPATH, "//input[@name='register.last_name']")
e_mail_address_first = (By.XPATH, "//input[@name='register.email']")
password_first = (By.XPATH, "//input[@name='register.secret']")
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
button_sport_all_things = (By.XPATH, "//*[@id='navigation-overlay-main-container']")
button_favorites = (By.XPATH, "//div[@class='egPhqr navToolItem-wishlist']")
all_favorites = (By.XPATH, "(//span[@class='sDq_FX _2kjxJ6 FxZV-M Yb63TQ SpRgR2 r9BRio'])[1]")
picture_first = (
    By.XPATH, "(//img[@class='sDq_FX lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy'])[1]"
)
picture_second = (
    By.XPATH, "(//img[@class='sDq_FX lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy'])[2]"
)

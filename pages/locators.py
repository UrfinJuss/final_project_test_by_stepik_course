from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login_url = "http://selenium1py.pythonanywhere.com/"
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg")
    PRICE_BOOK = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner > p > strong")
    NAME_BOOK = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner > strong")
    book = (By.CSS_SELECTOR, ".product_main > h1")
    price = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_see_as_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
               "Basket is not empty"

    def should_be_an_empty_cart_message(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        message = message.split(".")[0]
        print(message)
        assert message == "Your basket is empty", "no message about empty basket"

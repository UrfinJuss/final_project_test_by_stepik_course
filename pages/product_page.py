from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
    def guest_should_see_name_book(self):
        assert self.is_element_present(*ProductPageLocators.name_book_form), "Name book incorrect"
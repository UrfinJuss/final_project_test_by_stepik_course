from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
    def assert_price_book(self):
        price_book_alert = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        book_price = self.browser.find_element(*ProductPageLocators.price).text
        assert price_book_alert == book_price, "price book incorrect"
        
    def assert_name_book(self):
        name_book_alert = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        book_name = self.browser.find_element(*ProductPageLocators.book).text
        assert name_book_alert == book_name, "name book incorrect"    
     

from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()


    def is_basket_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY), "Basket is not empty"

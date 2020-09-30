from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY), "Basket is not empty"

    def should_be_not_products_in_cart(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_BASKET), "Basket is not empty"

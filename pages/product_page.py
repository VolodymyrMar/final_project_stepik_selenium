from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def compare_product_name_in_basket(self):
        alert_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME)[0].text
        name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        return alert_name == name

    def compare_product_price_in_basket(self):
        alert_price = self.browser.find_elements(*ProductPageLocators.PRODUCT_PRICE)[0].text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text
        return alert_price == price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

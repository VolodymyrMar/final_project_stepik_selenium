from .base_page import BasePage
from .locators import BasketLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*BasketLocators.BASKET_BUTTON).click()

    def compare_product_name_in_basket(self):
        alert_name = self.browser.find_elements(*BasketLocators.PRODUCT_NAME)[0].text
        name = self.browser.find_element(*BasketLocators.SUCCESS_MESSAGES).text
        return alert_name == name

    def compare_product_price_in_basket(self):
        alert_price = self.browser.find_elements(*BasketLocators.PRODUCT_PRICE).text
        price = self.browser.find_element(*BasketLocators.PRODUCT_DESCRIPTION).text
        return alert_price == price
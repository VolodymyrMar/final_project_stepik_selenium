from .base_page import BasePage
from .locators import MainLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        return self.is_element_present(*MainLocators.LOGIN_LINK)

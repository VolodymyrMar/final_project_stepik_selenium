from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url in "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            "Login link is not presented"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*BasePageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*BasePageLocators.BUTTON_REGISTRATION).click()

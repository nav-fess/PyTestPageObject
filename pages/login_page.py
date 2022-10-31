from .base_page import BasePage
from .locators import LoginPageLocators
import time 


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.input_registered_user_email(email)
        self.input_registered_user_pass(password)
        self.input_repeat_registered_user_pass(password)
        self.click_button_registration()


    def input_registered_user_email(self, email):
        self.wait_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)


    def input_registered_user_pass(self, password):
        self.wait_element(*LoginPageLocators.PASS_REGISTRATION).send_keys(password)


    def input_repeat_registered_user_pass(self, password):
        self.wait_element(*LoginPageLocators.PASS_REGISTRATION_REPEAT).send_keys(password)


    def click_button_registration(self):
        self.wait_element(*LoginPageLocators.BUTTON_REGISTRATION).click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "link doesn`t contain 'login'"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is missing"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "Registration form is missing"

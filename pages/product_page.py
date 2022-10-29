import pytest
from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def click_to_button_busket(self):
        button = self.wait_element(*ProductPageLocators.FORM_BASKET) 
        button.click()

    def text_product_name_and_prise(self, number_attribute):
        text_name_and_prise = self.wait_element(*ProductPageLocators.PRODUCT_NAME).text
        attribute_value = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_START)[number_attribute].text
            
        return (attribute_value, text_name_and_prise)

 
    def compare_product_name(self):
        number_name = 0
        name, all_text = self.text_product_name_and_prise(number_name)
        assert name in all_text, "name not consist in rezult text"

    def compare_product_prise(self):
        number_prise = 2
        prise, all_text = self.text_product_name_and_prise(number_prise)
        assert prise in all_text, "name not consist in rezult text"


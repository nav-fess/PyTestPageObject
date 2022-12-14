import pytest
import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def compare_product_name(self):
        number_name = 0
        name, all_text = self.text_product_name_and_prise(number_name)
        assert name in all_text, "name not consist in rezult text"


    def compare_product_prise(self):
        number_prise = 2
        prise, all_text = self.text_product_name_and_prise(number_prise)
        assert prise in all_text, "name not consist in rezult text"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"


    def should_is_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"

    
    def text_product_name_and_prise(self, number_attribute):
        text_name_and_prise = self.wait_element(*ProductPageLocators.PRODUCT_NAME).text
        attribute_value = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_START)[number_attribute].text
            
        return (attribute_value, text_name_and_prise)
      

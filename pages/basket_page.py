from .locators import MainPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def not_items_in_basket(self):
       assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), "Items are in the basket"


    def text_void_basket(self):
        text_void_baket = self.wait_element(*MainPageLocators.VOID_BASKET).text
        assert"Your basket is empty." in text_void_baket, "Baket is not void"


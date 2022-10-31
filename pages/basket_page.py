from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import MainPageLocators
from .base_page import BasePage
import time


class BasketPage(BasePage):
    def not_items_in_basket(self):
       assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), "Items are in the basket"


    def text_void_basket(self):
        text_void_baket = self.wait_element(*MainPageLocators.VOID_BASKET).text
        assert"Your basket is empty." in text_void_baket, "Baket is not void"


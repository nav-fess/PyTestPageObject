import pytest
from selenium import webdriver
from pages.product_page import ProductPage


@pytest.mark.parametrize('part_address', list(range(10)))
def test_guest_can_add_product_to_basket(browser, part_address): 
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_address}" 
    page = ProductPage(browser, link)    
    page.open()
    page.click_to_button_busket()
    page.solve_quiz_and_get_code()
    page.compare_product_name()
    page.compare_product_prise()		
    

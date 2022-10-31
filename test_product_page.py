import pytest
from selenium import webdriver
from pages.product_page import ProductPage
from pages.basket_page import  BasketPage


@pytest.mark.parametrize('part_address', list(range(10)))
def test_guest_can_add_product_to_basket(browser, part_address): 
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_address}" 
    page = ProductPage(browser, link)    
    page.open()
    page.click_to_button_busket()
    page.solve_quiz_and_get_code()
    page.compare_product_name()
    page.compare_product_prise()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" 
    page = ProductPage(browser) 
    page.open()
    page.click_to_button_busket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)    
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)    
    page.open()
    page.click_to_button_busket()
    page.solve_quiz_and_get_code()
    page.should_is_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()	
    page.click_to_view_busket()
    basket_page = BasketPage(browser, browser.current_url)	
    basket_page.not_items_in_basket()
    basket_page.text_void_basket()	


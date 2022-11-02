import time
import pytest
from selenium import webdriver
from pages.product_page import ProductPage
from pages.basket_page import  BasketPage
from pages.login_page import  LoginPage


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(f'pocht{time.time()}@yandex.ru','passwordpas{time.time()}')
        login_page.should_be_authorized_user()
         
       
    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)    
        page.open()
        page.should_not_be_success_message()


    @pytest.mark.need_review	
    @pytest.mark.parametrize('part_address', list(range(10)))
    def test_user_can_add_product_to_basket(self, browser, part_address): 
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_address}" 
        page = ProductPage(browser, link)    
        page.open()
        page.click_to_button_busket()
        page.solve_quiz_and_get_code()
        page.compare_product_name()
        page.compare_product_prise()


@pytest.mark.need_review
@pytest.mark.xfail
@pytest.mark.parametrize('part_address', list(range(10)))
def test_guest_can_add_product_to_basket(browser, part_address): 
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_address}" 
    page = ProductPage(browser, link)    
    page.open()
    page.click_to_button_busket()
    page.solve_quiz_and_get_code()
    page.compare_product_name()
    page.compare_product_prise()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" 
    page = ProductPage(browser) 
    page.open()
    page.click_to_button_busket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.xfail
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)

    page.open()	
    page.click_to_view_busket()
    basket_page = BasketPage(browser, browser.current_url)	
    basket_page.not_items_in_basket()
    basket_page.text_void_basket()	


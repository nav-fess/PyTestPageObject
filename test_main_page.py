import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.main_page MainPage
import time


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(2)
    page.should_be_login_link()
    time.sleep(1)


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    


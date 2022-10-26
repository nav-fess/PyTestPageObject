from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    FORM_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket") 
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6.product_main")	
    PRODUCT_NAME_START = (By.CSS_SELECTOR,".alertinner strong")
  

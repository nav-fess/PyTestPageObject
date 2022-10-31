from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")	    


class MainPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")	
    VOID_BASKET = (By.CSS_SELECTOR, "#content_inner")  
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a") 	 


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_REGISTRATION_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "button[value='Register']")

class ProductPageLocators():
    FORM_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket") 
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6.product_main")	
    PRODUCT_NAME_START = (By.CSS_SELECTOR,".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alertinner")


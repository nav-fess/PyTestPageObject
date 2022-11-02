from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import MainPageLocators
import time
import math

class BasePage():
    def __init__(self, browser, url, timeout=7):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def click_to_button_busket(self):
        click = self.wait_element(*ProductPageLocators.FORM_BASKET).click()
        assert click == None , "not click on link"
	
   		    
    def click_to_view_busket(self):
        click = self.wait_element(*MainPageLocators.VIEW_BASKET).click()
        assert click == None , "not click on button busket"
	

    def go_to_login_page(self):
        click = self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        assert click == None , "not click on button login"


    def is_element_present(self, *param):	
        try:
            self.wait_element(*param)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present(self, *param, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((param[0],param[1])))
        except TimeoutException:
            return True

        return False

        
    def is_disappeared(self, *param, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((param[0],param[1])))
        except TimeoutException:
            return False


    def open(self):
        self.browser.get(self.url)
        time.sleep(3)


    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))        
        alert.send_keys(answer)
        alert.accept()
        '''try:
            WebDriverWait(self.browser, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear') 				
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(1)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")'''
        

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"  

 
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "not register user"	


    def wait_element(self, *param, pause = 2):
        time.sleep(int(pause))
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((param[0],param[1])))
        
        return True

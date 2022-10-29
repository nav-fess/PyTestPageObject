from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)
        time.sleep(3)


    def is_element_present(self, how, what):	
        try:
            self.wait_element(how, what)
        except NoSuchElementException:
            return False
        return True
     

    def wait_element(self, *param, pause = 2):
        time.sleep(pause)
        return self.browser.find_element(*param)
        
   
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))        
        alert.send_keys(answer)
        alert.accept()
        '''try:
            time.sleep(1)
            WebDriverWait(self.browser, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear') 				
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(1)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")'''


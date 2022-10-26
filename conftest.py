import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):

    '''language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(options = options)'''
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages', 'en') 
    profile.update_preferences()
    browser = webdriver.Firefox(profile)
   
    yield browser

    print("\nquit browser..")
    browser.quit()

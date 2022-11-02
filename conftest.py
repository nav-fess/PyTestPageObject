import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose browser: chrome or firefox")
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name") 
    browser = None
    options = None

    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument(f"--lang={language}")
        browser = webdriver.Chrome(options = options)
    elif browser_name == 'firefox':
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", language)
        firefox_profile.update_preferences()
        browser = webdriver.Firefox(firefox_profile)
   
    yield browser

    print("\nquit browser..")
    browser.quit()

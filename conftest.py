import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from config import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--guest")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1280, 1024)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_as(driver):
    def _login_as(user):
        page = LoginPage(driver, user)
        page.open(BASE_URL)
        page.fill_in_login_form()
        return page

    return _login_as

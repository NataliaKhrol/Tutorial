import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from config import BASE_URL
from pages.login_page import LoginPage


# 1. Добавляем возможность принимать параметр --browser из консоли
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер: chrome или firefox"
    )


@pytest.fixture(scope='function')
def driver(request):
    # Получаем значение браузера из командной строки
    browser = request.config.getoption("browser").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--guest")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        # Для Firefox аналог --guest часто не требуется в чистом профиле,
        # но можно добавить специфичные настройки если нужно
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise pytest.UsageError(f"--browser должен быть 'chrome' или 'firefox'. Передано: {browser}")

    driver.set_window_size(1280, 1024)
    allure.dynamic.parameter("browser", browser)

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


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# from config import BASE_URL
# from pages.login_page import LoginPage
#
#
# @pytest.fixture(scope='function')
# def driver():
#     options = Options()
#     options.add_argument("--guest")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.set_window_size(1280, 1024)
#     # driver.maximize_window()
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture
# def login_as(driver):
#     def _login_as(user):
#         page = LoginPage(driver, user)
#         page.open(BASE_URL)
#         page.fill_in_login_form()
#         return page
#
#     return _login_as

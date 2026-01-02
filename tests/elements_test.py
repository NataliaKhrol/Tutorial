import time

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestLoginPage:

    def test_correct_login(self, driver):
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        login_page.open("https://www.saucedemo.com/")
        time.sleep(3)
        login_page.fill_in_login_form()
        time.sleep(5)

        assert products_page.page_is_open() == True
        assert products_page.check_title() == "Products"

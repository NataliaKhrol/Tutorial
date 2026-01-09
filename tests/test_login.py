import time

import pytest

from conftest import login_as
from data.user_factory import UserFactory
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestLoginPage:

    def test_correct_login(self, driver, login_as):
        user = UserFactory.admin()
        products_page = ProductsPage(driver, user)
        login_as(user)
        time.sleep(5)

        assert products_page.page_is_open() == True
        assert products_page.check_title() == "Products"

    @pytest.mark.parametrize(
        "user, error_message",
        [
            (UserFactory.locked(), "Epic sadface: Sorry, this user has been locked out."),
            (UserFactory.empty_username(), "Epic sadface: Username is required"),
            (UserFactory.empty_password(), "Epic sadface: Password is required"),
            (UserFactory.wrong_username(),
                    "Epic sadface: Username and password do not match any user in this service"
            )
        ]
    )

    def test_incorrect_login(self, driver, login_as, user, error_message):
        login_page: LoginPage = login_as(user)
        time.sleep(5)

        assert login_page.is_error_message_appear(), "Сообщение об ошибке не появилось для заблокированного юзера"

        assert login_page.get_error_message() == error_message, "Сообщение об ошибке не верное"

    # def test_empty_user_login(self, driver):
    #     user = UserFactory.empty_username()
    #     login_page = LoginPage(driver, user)
    #     login_page.open("https://www.saucedemo.com/")
    #     time.sleep(3)
    #     login_page.fill_in_login_form()
    #     time.sleep(5)
    #
    #     assert login_page.is_error_message_appear(), "Сообщение об ошибке не появилось для заблокированного юзера"
    #
    #     assert login_page.get_error_message() == "Epic sadface: Username is required", \
    #         "Сообщение об ошибке не верное"
    #
    # def test_empty_password_login(self, driver):
    #     user = UserFactory.empty_password()
    #     login_page = LoginPage(driver, user)
    #     login_page.open("https://www.saucedemo.com/")
    #     time.sleep(3)
    #     login_page.fill_in_login_form()
    #     time.sleep(5)
    #
    #     assert login_page.is_error_message_appear(), "Сообщение об ошибке не появилось для заблокированного юзера"
    #
    #     assert login_page.get_error_message() == "Epic sadface: Password is required", \
    #             "Сообщение об ошибке не верное"
    #
    # def test_non_match_login(self, driver):
    #     user = UserFactory.wrong_username()
    #     login_page = LoginPage(driver, user)
    #     login_page.open("https://www.saucedemo.com/")
    #     time.sleep(3)
    #     login_page.fill_in_login_form()
    #     time.sleep(5)
    #
    #     assert login_page.is_error_message_appear(), "Сообщение об ошибке не появилось для заблокированного юзера"
    #
    #     assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service", \
    #             "Сообщение об ошибке не верное"
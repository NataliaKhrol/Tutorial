import time

from selenium.webdriver import Keys

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()


    def fill_in_login_form(self):
        self.element_is_visible(self.locators.USER_INPUT).send_keys("standard_user")
        self.element_is_visible(self.locators.USER_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.USER_INPUT).send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        self.element_is_visible(self.locators.USER_INPUT).send_keys("standard_user")
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys("secret_sauce")
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)

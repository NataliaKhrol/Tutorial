import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def fill_in_login_form(self):
        self.element_is_visible(self.locators.USER_INPUT).send_keys(self.user.username)
        self.element_is_visible(self.locators.USER_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.USER_INPUT).send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        self.element_is_visible(self.locators.USER_INPUT).send_keys(self.user.username)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(self.user.password)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)

    def is_error_message_appear(self) -> bool:
        try:
            return bool(self.element_is_visible(self.locators.ERROR_MESSAGE, timeout=3))
        except TimeoutException:
            return False

    def get_error_message(self) -> str:
        return self.element_is_visible(self.locators.ERROR_MESSAGE).text

import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step("Заполнить форму логина")
    def fill_in_login_form(self):
        self.element_is_visible(self.locators.USER_INPUT).send_keys(self.user.username)
        self.element_is_visible(self.locators.USER_INPUT).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.USER_INPUT).send_keys(Keys.BACK_SPACE)
        # self.element_is_visible(self.locators.USER_INPUT).clear()
        time.sleep(3)
        self.element_is_visible(self.locators.USER_INPUT).send_keys(self.user.username)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(self.user.password)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)

    @allure.step("Проверка появления сообщения об ошибке")
    def is_error_message_appear(self) -> bool:
        try:
            return bool(self.element_is_visible(self.locators.ERROR_MESSAGE, timeout=3))
        except TimeoutException:
            return False

    @allure.step("Получение текста сообщения об ошибке")
    def get_error_message(self) -> str:
        text = self.element_is_visible(self.locators.ERROR_MESSAGE).text
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!! доп шаг ниже для отчета Прикрепляем сам текст ошибки в отчет для удобства анализа
        allure.attach(text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
        return text

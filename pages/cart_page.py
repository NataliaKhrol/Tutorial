import allure

from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    locators = CartPageLocators()

    @allure.step("Проверка заголовка страницы корзины")
    def check_title(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

    @allure.step("Получение списка названий товаров в корзине")
    def get_products_names(self) -> list[str]:
        elements = self.elements_are_visible(self.locators.PRODUCTS_NAMES)
        return [product.text for product in elements]

import allure

from locators.products_page_locators import ProductsPageLocators
from pages.base_page import BasePage


class ProductsPage(BasePage):
    locators = ProductsPageLocators()

    @allure.step("Проверка: страница открыта")
    def page_is_open(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).is_displayed()

    @allure.step("Получение заголовка страницы")
    def check_title(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

    @allure.step("Добавление товара '{product}' в корзину по названию")
    def add_goods_to_cart_by_name(self, product):
        by, pattern = self.locators.ADD_TO_CART_BUTTON_PATTERN
        locator = (by, pattern.format(product))
        self.element_is_visible(locator).click()

    @allure.step("Проверка количества товаров в корзине (на иконке)")
    def check_goods_quantity(self) -> str:
        return self.element_is_visible(self.locators.CART_BADGE).text

    @allure.step("Добавление товара с индексом {product_index} в корзину")
    def add_goods_to_cart_by_index(self, product_index):
        buttons = self.elements_are_visible(self.locators.ADD_TO_CART_BUTTON)
        buttons[product_index].click()

    @allure.step("Переход в корзину (клик по иконке)")
    def switch_to_cart(self):
        self.element_is_visible(self.locators.CART_LINK).click()

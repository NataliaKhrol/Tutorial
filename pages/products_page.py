from locators.products_page_locators import ProductsPageLocators
from pages.base_page import BasePage


class ProductsPage(BasePage):
    locators = ProductsPageLocators()

    def page_is_open(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).is_displayed()

    def check_title(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

    def add_goods_to_cart_by_name(self, product):
        by, pattern = self.locators.ADD_TO_CART_BUTTON_PATTERN
        locator = (by, pattern.format(product))
        self.element_is_visible(locator).click()

    def check_goods_quantity(self) -> str:
        return self.element_is_visible(self.locators.CART_BADGE).text

    def add_goods_to_cart_by_index(self, product_index):
        buttons = self.elements_are_visible(self.locators.ADD_TO_CART_BUTTON)
        buttons[product_index].click()

    def switch_to_cart(self):
        self.element_is_visible(self.locators.CART_LINK).click()
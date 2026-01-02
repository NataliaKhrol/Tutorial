from locators.products_page_locators import ProductsPageLocators
from pages.base_page import BasePage


class ProductsPage(BasePage):
    locators = ProductsPageLocators()

    def page_is_open(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).is_displayed()

    def check_title(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

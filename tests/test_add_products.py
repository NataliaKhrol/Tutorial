import time

import allure

from data.user_factory import UserFactory
from pages.products_page import ProductsPage

@allure.epic("Магазин Sauce Demo")
@allure.feature("Витрина товаров")
class TestProductsPage:

    @allure.title("Добавление товара в корзину через карточку товара")
    @allure.description("Тест проверяет, что при нажатии кнопки 'Add to cart' товар появляется в корзине")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.issue("https://jira.example.com/browse/BUG-123", "Баг с отображением счетчика")  # Ссылка на задачу/баг
    @allure.testcase("https://tms.yourcompany.com/case/123", "ТК-123: Проверка добавления в корзину")
    def test_goods_added_by_name(self, driver, login_as):
        user = UserFactory.admin()
        products_page = ProductsPage(driver, user)
        login_as(user)
        time.sleep(5)
        assert products_page.page_is_open() == True
        products_page.add_goods_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        time.sleep(5)

        assert products_page.check_goods_quantity() == "1"
        assert int(products_page.check_goods_quantity()) == 1

    def test_goods_added_by_index(self, driver, login_as):
        user = UserFactory.admin()
        products_page = ProductsPage(driver, user)
        login_as(user)
        time.sleep(5)
        assert products_page.page_is_open() == True
        products_page.add_goods_to_cart_by_index(0)
        time.sleep(5)

        assert int(products_page.check_goods_quantity()) == 1

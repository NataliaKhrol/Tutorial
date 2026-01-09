import time

from data.user_factory import UserFactory
from pages.cart_page import CartPage
from pages.products_page import ProductsPage


class TestCartPage:
    def test_check_goods_in_cart(self, driver, login_as):
        user = UserFactory.admin()
        cart_page = CartPage(driver, user)
        login_as(user)
        time.sleep(5)
        products_page = ProductsPage(driver, user)
        products_page.add_goods_to_cart_by_index(1)
        products_page.switch_to_cart()

        assert cart_page.check_title() == "Your Cart"
        products = cart_page.get_products_names()

        print(products, "!!!!!!!!!!!!!!!!!!!!!!")

        assert len(products) == 1
        assert products  # список не пустой
        assert "Sauce Labs Bike Light" in products

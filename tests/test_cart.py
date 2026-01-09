import time

from data.user_factory import UserFactory
from enums.page_titles import PageTitle
from pages.cart_page import CartPage
from pages.products_page import ProductsPage


class TestCartPage:
    def test_check_goods_in_cart(self, driver, login_as):
        user = UserFactory.admin()
        cart_page = CartPage(driver, user)
        login_as(user)
        time.sleep(5)
        products_page = ProductsPage(driver, user)
        products_page.add_goods_to_cart_by_name("Sauce Labs Bike Light")
        products_page.add_goods_to_cart_by_index(1)
        products_page.switch_to_cart()

        assert cart_page.check_title() == PageTitle.CART.value
        products = cart_page.get_products_names()

        print(products, "!!!!!!!!!!!!!!!!!!!!!!")

        assert len(products) == 2
        assert products  # список не пустой
        assert "Sauce Labs Bike Light" in products


    # def test_check_goods_in_cart(self, driver, login_as):
    #     user = UserFactory.admin()
    #     login_as(user)
    #
    #     products_page = ProductsPage(driver, user)
    #     cart_page = CartPage(driver, user)
    #
    #     products_to_add = [
    #         "Sauce Labs Backpack",
    #         "Sauce Labs Bike Light",
    #         "Sauce Labs Bolt T-Shirt"
    #     ]
    #
    #     for product in products_to_add:
    #         products_page.add_goods_to_cart_by_name(product)
    #
    #     products_page.switch_to_cart()
    #
    #     assert cart_page.check_title() == "Your Cart"
    #
    #     products_in_cart = cart_page.get_products_names()
    #
    #     assert len(products_in_cart) == len(products_to_add)
    #     print(products_in_cart, " @@@@@@@@@@@@@@@@@@@@@@")
    #     for product in products_to_add:
    #         assert product in products_in_cart

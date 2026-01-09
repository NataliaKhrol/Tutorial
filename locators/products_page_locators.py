from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PAGE_TITLE = (By.XPATH, "//*[@data-test='title']")
    # ADD_TO_CART_BUTTON_PATTERN = (
    #     "//div[text()='%s']//ancestor::div[@class='inventory_item']//button"
    # )
    ADD_TO_CART_BUTTON_PATTERN = (By.XPATH,"//div[text()='{}']//ancestor::div[@class='inventory_item']//button")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    DATA_TEST_PATTERN = "[data-test='%s']"
    CART_BADGE = (By.XPATH, "//*[@data-test='shopping-cart-badge']")
    CART_LINK = (By.XPATH, "//*[@data-test='shopping-cart-link']")


from selenium.webdriver.common.by import By


class CartPageLocators:
    PAGE_TITLE = (By.XPATH, "//*[@data-test='title']")
    PRODUCTS_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

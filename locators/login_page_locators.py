from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "*[data-test='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//*[@data-test='error']")

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, user):
        self.driver = driver
        self.user = user

    def open(self, url):
        self.driver.get(url)

    def element_is_visible(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_not_visible(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=3):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

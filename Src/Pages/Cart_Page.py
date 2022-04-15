from selenium.webdriver.common.by import By
from Src.Locators import Locator


class Cart(object):

    def __init__(self, driver):
        self.driver = driver
        self.cart_go_to_checkout = Locator.cart_go_to_checkout
        self.cart_guest = Locator.cart_guest
        self.cart_price_cart = Locator.cart_price_cart
        self.cart_price_summary = Locator.cart_price_summary
        self.cart_name = Locator.cart_name

    def proceed_to_checkout(self):

        self.driver.find_element(
            By.XPATH, self.cart_go_to_checkout).click()

        self.driver.find_element(
            By.XPATH, self.cart_guest).click()

    def get_price_cart(self) -> float:

        price_str = self.driver.find_element(
            By.XPATH, self.cart_price_cart).text
        return float(price_str.strip(' zł').replace(',', '.'))

    def get_price_summary(self) -> float:

        price_str = self.driver.find_element(
            By.XPATH, self.cart_price_summary).text
        return float(price_str.strip(' zł').replace(',', '.'))

    def get_name(self) -> str:
        return self.driver.find_element(By.XPATH, self.cart_name).get_attribute("title")

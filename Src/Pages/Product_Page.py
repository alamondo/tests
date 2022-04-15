from selenium.webdriver.common.by import By
from Src.Locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product(object):

    def __init__(self, driver):
        self.driver = driver
        self.product_add_to_cart = Locator.product_add_to_cart
        self.product_size = Locator.product_size
        self.product_confirm = Locator.product_confirm
        self.product_price = Locator.product_price
        self.product_name = Locator.product_name

    def add_to_cart_and_proceed_to_checkout(self, size: int):
        self.driver.find_element(By.XPATH, self.product_add_to_cart).click()
        self.driver.find_element(
            By.XPATH, self.product_size.format(size)).click()
        self.driver.find_element(By.XPATH, self.product_confirm).click()

    def get_price(self) -> float:
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, self.product_price)))
        price_str = self.driver.find_element(By.XPATH, self.product_price).text
        return float(price_str.strip(' zł').replace(',', '.'))

    def get_name(self) -> str:
        return self.driver.find_element(By.XPATH, self.product_name).text

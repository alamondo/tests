from selenium.webdriver.common.by import By
from Src.Locators import Locator


class Billing(object):

    def __init__(self, driver):

        self.driver = driver
        self.billing_email = Locator.billing_email
        self.billing_telephone = Locator.billing_telephone
        self.billing_firstname = Locator.billing_firstname
        self.billing_lastname = Locator.billing_lastname
        self.billing_street_0 = Locator.billing_street_0
        self.billing_street_1 = Locator.billing_street_1
        self.billing_postcode = Locator.billing_postcode
        self.billing_city = Locator.billing_city
        self.billing_dhl = Locator.billing_dhl
        self.billing_payu = Locator.billing_payu
        self.billing_check_all = Locator.billing_check_all
        self.billing_proceed = Locator.billing_proceed
        self.billing_product_name = Locator.billing_product_name
        self.billing_product_price = Locator.billing_product_price

    def getInputEmail(self):
        return self.driver.find_element(By.XPATH, self.billing_email)

    def getInputTelephone(self):
        return self.driver.find_element(By.XPATH, self.billing_telephone)

    def getInputFirstname(self):
        return self.driver.find_element(By.XPATH, self.billing_firstname)

    def getInputLastname(self):
        return self.driver.find_element(By.XPATH, self.billing_lastname)

    def getInputStreet0(self):
        return self.driver.find_element(By.XPATH, self.billing_street_0)

    def getInputStreet1(self):
        return self.driver.find_element(By.XPATH, self.billing_street_1)

    def getInputPostcode(self):
        return self.driver.find_element(By.XPATH, self.billing_postcode)

    def getInputCity(self):
        return self.driver.find_element(By.XPATH, self.billing_city)

    def getButtonDHL(self):
        return self.driver.find_element(By.XPATH, self.billing_dhl)

    def getButtonPayU(self):
        return self.driver.find_element(By.XPATH, self.billing_payu)

    def getButtonCheckAll(self):
        return self.driver.find_element(By.XPATH, self.billing_check_all)

    def getButtonProceed(self):
        return self.driver.find_element(By.XPATH, self.billing_proceed)

    def get_price(self) -> float:
        price_str = self.driver.find_element(
            By.XPATH, self.billing_product_price).text
        return float(price_str.strip(' zł').replace(',', '.'))

    def get_name(self) -> str:
        return self.driver.find_element(By.XPATH, self.billing_product_name).get_attribute("title")

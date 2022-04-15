from selenium.webdriver.common.by import By
from Src.Locators import Locator


class PaymentMethodPage(object):

    def __init__(self, driver):

        self.driver = driver
        self.locator_payment_method_card = Locator.payment_method_card
        self.locator_payment_method_card_details = Locator.payment_method_card_details
        self.locator_payment_method_price = Locator.payment_method_price

    def getButtonCard(self):
        return self.driver.find_element(By.XPATH, self.locator_payment_method_card)

    def getButtonCardDetails(self):
        return self.driver.find_element(By.XPATH, self.locator_payment_method_card_details)

    def get_price(self) -> float:
        price_str = self.driver.find_element(
            By.XPATH, self.locator_payment_method_price).text
        return float(price_str.strip(' zł').replace(',', '.'))


class PaymentDetailsPage(object):

    def __init__(self, driver):

        self.driver = driver
        self.payment_details_card_number = Locator.payment_details_card_number
        self.payment_details_card_date = Locator.payment_details_card_date
        self.payment_details_card_ccv = Locator.payment_details_card_ccv
        self.payment_details_submit_btn = Locator.payment_details_submit_btn
        self.payment_details_close_btn = Locator.payment_details_close_btn

    def getInputCardNumber(self):
        return self.driver.find_element(By.XPATH, self.payment_details_card_number)

    def getInputCardDate(self):
        return self.driver.find_element(By.XPATH, self.payment_details_card_date)

    def getInputCardCCV(self):
        return self.driver.find_element(By.XPATH, self.payment_details_card_ccv)

    def getButtonSubmit(self):
        return self.driver.find_element(By.XPATH, self.payment_details_submit_btn)

    def getButtonClose(self):
        return self.driver.find_element(By.XPATH, self.payment_details_close_btn)

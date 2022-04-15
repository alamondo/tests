from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Src.Locators import Locator

class Urls(object):
    
    test_1 = "https://modivo.pl/c/kobiety/odziez/bluzki-i-koszule/oferta:nowosc/rozmiar:gorne_czesci_garderoby_2:m:38_1"
    transaction_success = "https://modivo.pl/checkout/success"


class Loader(object):

    def __init__(self, browser) -> None:
        self.browser = browser


    def wait(self):

        wait = WebDriverWait(self.browser, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, Locator.loader)))
            wait.until_not(EC.visibility_of_element_located((By.XPATH, Locator.loader)))
        except TimeoutException:
            pass

class Marketing(object):

    def __init__(self) -> None:
        pass
        
    def wait(self, browser):
        wait = WebDriverWait(browser, 15)
        wait.until(EC.visibility_of_element_located((By.ID, Locator.marketing_id)))
        browser.find_element(By.XPATH, Locator.marketing_close).click()
        
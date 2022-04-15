import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Src.Pages.Billing_Page import Billing
from Src.Pages.Cart_Page import Cart
from Src.Pages.Payment_Page import PaymentDetailsPage, PaymentMethodPage
from Src.Pages.Product_Page import Product
from Src.Utils.Utils import Urls, Marketing, Loader


@pytest.fixture
def browser():

    service = Service("C:/Users/Jakub/Documents/sel/chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--start-maximized")

    driver = Chrome(service=service, options=chrome_options)

    driver.get(Urls.test_1)
    driver.implicitly_wait(10)
    driver.set_window_size(1700, 1024)
    yield driver

    driver.close()


def test_elems(browser):

    wait = WebDriverWait(browser, 15)

    marketing = Marketing()
    marketing.wait(browser)

    browser.find_element(By.XPATH, '//div[@class="content"]/a').click()

    product_page = Product(browser)

    price = product_page.get_price()
    name = product_page.get_name()

    product_page.add_to_cart_and_proceed_to_checkout(size=38)

    cart_page = Cart(browser)

    price_cart_0 = cart_page.get_price_cart()
    price_cart_1 = cart_page.get_price_summary()
    name_cart = cart_page.get_name()

    assert price == price_cart_0 == price_cart_1
    assert name == name_cart

    cart_page.proceed_to_checkout()

    billing_page = Billing(browser)

    price_billing = billing_page.get_price()
    name_billing = billing_page.get_name()

    assert price == price_billing
    assert name == name_billing

    billing_page.getInputEmail().send_keys("temp@te.mp")
    billing_page.getInputTelephone().send_keys("+4812 345 67 89")
    billing_page.getInputFirstname().send_keys("aaaa")
    billing_page.getInputLastname().send_keys("bbbbbb")
    billing_page.getInputStreet0().send_keys("cccccc")
    billing_page.getInputStreet1().send_keys("aaaa")
    billing_page.getInputPostcode().send_keys("11-111")
    billing_page.getInputCity().send_keys("Miasto")
    billing_page.getButtonDHL().click()

    loader = Loader(browser)
    loader.wait()

    billing_page.getButtonPayU().click()

    loader.wait()

    billing_page.getButtonCheckAll().click()
    billing_page.getButtonProceed().click()

    payment_method = PaymentMethodPage(browser)

    price_payment = payment_method.get_price()

    assert price == price_payment

    payment_method.getButtonCard().click()
    payment_method.getButtonCardDetails().click()

    payment_details = PaymentDetailsPage(browser)

    payment_details.getInputCardNumber().send_keys("4111 1111 1111 1111")
    payment_details.getInputCardDate().send_keys("0330")
    payment_details.getInputCardCCV().send_keys("111")
    payment_details.getButtonSubmit().click()
    payment_details.getButtonClose().click()

    wait.until(EC.url_to_be(Urls.transaction_success))

    assert browser.find_element(
        By.XPATH,  '//div[@class="order-repayment-panel"]')
    assert browser.find_element(
        By.XPATH,  '//button[contains(@class, "repay-btn")]')

from itertools import product


class Locator(object):

    billing_email = '//input[@data-test-id="billing__email"]'
    billing_telephone = '//input[@data-test-id="billing__telephone"]'
    billing_firstname = '//input[@data-test-id="billing__firstname"]'
    billing_lastname = '//input[@data-test-id="billing__lastname"]'
    billing_street_0 = '//input[@data-test-id="billing__street-0"]'
    billing_street_1 = '//input[@data-test-id="billing__street-1"]'
    billing_postcode = '//input[@data-test-id="billing__postcode"]'
    billing_city = '//input[@data-test-id="billing__city"]'
    billing_dhl = '//div[./input[@data-test-id="custom02"]]'
    billing_payu = '//div[./input[@data-test-id="payu_gateway"]]'
    billing_check_all = '//div[./input[@data-test-id="check-all"]]/label'
    billing_proceed = '//button[@data-test-id="agreements-button"]'
    billing_product_name = '//a[@class="text-link name"]'
    billing_product_price = '//div[contains(@class, "summary-row")]//div[@class="price"]'

    payment_method_card = '//a[@title="Płatność kartą"]'
    payment_method_card_details = '//a[@title="Podaj dane karty"]'
    payment_method_price = '//em/div[2]'

    payment_details_card_number = '//input[@id="card-number"]'
    payment_details_card_date = '//input[@id="card-date"]'
    payment_details_card_ccv = '//input[@id="card-cvv"]'
    payment_details_submit_btn = '//input[@name="submit"]'
    payment_details_close_btn = '//a[@class="buttonlike action-button secondary"]'

    loader = '//div[div[@id="code-loader"]]'

    marketing_id = 'marketing-approvals'
    marketing_close = '//button[@class="button-icon button-icon"]'

    product_add_to_cart = '//button[@data-test-id="add-to-cart-button"]'
    product_size = '//tr[@data-test-id="product-size"][@data-test-value="{}"]'
    product_confirm = '//button[@data-test-id="added-to-cart-go-to-cart-button"]'
    product_price = '//div[contains(@class, "final-price-wrapper")]//div[@class="price"]'
    product_name = '//span[@class="breadcrumb-name"]'

    cart_go_to_checkout = '//button[@data-test-id="cart-proceed-to-checkout"]'
    cart_guest = '//button[@data-test-id="continue-as-guest"]'
    cart_price_cart = '//div[contains(@class, "item-block-container")]//div[contains(@class, "final-price-wrapper")]//div[@class="price"]'
    cart_price_summary = '//div[contains(@class, "summary-block")]//div[@class="price"]'
    cart_name = '//a[@class="text-link name"]'

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")

    # ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    # PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    # PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    # BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    # BASKET_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

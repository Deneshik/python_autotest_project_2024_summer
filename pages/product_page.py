# from selenium.common import NoAlertPresentException
# import math
# from selenium.webdriver.common.by import By
# from .login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, product_name):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in success_message, f"Expected '{product_name}' to be in '{success_message}'"

    def should_be_correct_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total is not presented"
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    # def should_be_correct_basket_total(self, product_price):
    #     # Ожидание, пока элемент станет видимым
    #     basket_total_element = WebDriverWait(self.browser, 10).until(
    #         EC.visibility_of_element_located((ProductPageLocators.BASKET_TOTAL))
    #     )
    #     basket_total = basket_total_element.text
    #     print(f"Product price: {product_price}")
    #     print(f"Basket total: {basket_total}")
    #     # Удаляем лишние символы и пробелы
    #     product_price = product_price.replace('£', '').strip()
    #     basket_total = basket_total.replace('£', '').strip()
    #     assert product_price == basket_total, f"Basket total is not correct: {basket_total} != {product_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should have"






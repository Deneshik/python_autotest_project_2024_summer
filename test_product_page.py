import time
import math
import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["?promo=newYear0", "?promo=newYear1"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_added_to_basket()
    page.check_basket_total_matches_product_price()






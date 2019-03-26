# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.tests import run_testcase
from oct.browsers import Chrome
from oct.pages.product_page import ProductPage


class AddingProductToCart(Testcase):
    @test
    def test_adding_to_cart(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        product_page = ProductPage(chrome, "41", "iMac")
        product_page.open()
        product_page.loaded()
        product_page.information_block().add_to_cart()
        assert product_page.messages().has_cart_message()


if __name__ == "__main__":
    run_testcase()

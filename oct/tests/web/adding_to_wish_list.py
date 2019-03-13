# pylint: disable=no-self-use # pyATS-related exclusion
from selenium.webdriver import Remote
from pyats.aetest import Testcase, test
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.product_page import ProductPage


class AddingProductToWishList(Testcase):
    @test
    def test_adding_to_wish_list(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        product_page = ProductPage(chrome, "41", "iMac")
        product_page.open()
        product_page.loaded()
        product_page.information_block().add_to_wish_list()
        assert product_page.messages().has_wish_list_message()


if __name__ == "__main__":
    run_testcase()

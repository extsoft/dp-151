# pylint: disable=no-self-use # pyATS-related exclusion

from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.product_page import ProductPage


class OpeningProdImg(Testcase):
    @test
    def test(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        product_page = ProductPage(chrome, "41", "iMac")
        product_page.open()
        product_page.open_product_image()
        assert product_page.is_open_image()


if __name__ == "__main__":
    run_testcase()

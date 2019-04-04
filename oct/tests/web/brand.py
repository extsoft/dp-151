# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.brand import BrandPage
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.product_page import ProductPage


class OpenBrand(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        product_page = ProductPage(chrome, "41", "IMac")
        product_page.open(device)
        product_page.information_block().open_brand_page()
        assert BrandPage(chrome, "8", "Apple").loaded()


if __name__ == "__main__":
    run_testcase()

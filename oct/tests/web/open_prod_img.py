# pylint: disable=no-self-use # pyATS-related exclusion

from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.pages.product_page import ProductPage
from oct.tests import run_testcase


class OpeningProdImg(Testcase):
    @test
    def test(self, device: Device) -> None:
        chrome: Remote = Chrome()
        product_page = ProductPage(chrome, "41", "iMac")
        product_page.open(device)
        product_page.open_product_image()
        assert product_page.is_open_image()


if __name__ == "__main__":
    run_testcase()

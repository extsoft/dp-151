# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.product_page import ProductPage
from oct.browsers import Chrome
from oct.tests import run_testcase


class AddingProductToCart(Testcase):
    @test
    def test_adding_to_cart(self, device: Device) -> None:
        chrome: Remote = Chrome()
        product_page = ProductPage(chrome, "41", "iMac")
        product_page.load(device)
        product_page.available()
        product_page.information_block().add_to_cart()
        assert product_page.messages().has_cart_message()


if __name__ == "__main__":
    run_testcase()

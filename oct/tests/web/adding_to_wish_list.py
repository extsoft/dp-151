# pylint: disable=no-self-use # pyATS-related exclusion
from selenium.webdriver import Remote
from pyats.topology import Device
from pyats.aetest import Testcase, test
from oct.browsers import Chrome
from oct.pages.product_page import ProductPage
from oct.tests import run_testcase


class AddingProductToWishList(Testcase):
    @test
    def test_adding_to_wish_list(self, device: Device) -> None:
        chrome: Remote = Chrome()
        product_page = ProductPage(chrome, "41", "iMac")
        product_page.open(device)
        product_page.loaded()
        product_page.information_block().add_to_wish_list()
        assert product_page.messages().has_wish_list_message()


if __name__ == "__main__":
    run_testcase()

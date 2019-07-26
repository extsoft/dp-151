# pylint: disable=no-self-use # pyATS-related exclusion


from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.share import ShareWindow
from oct.pages.product_page import ProductPage


class SharePopup(Testcase):
    @test
    def test(self, device: Device) -> None:
        chrome: Remote = Chrome()
        product_page = ProductPage(chrome, "34", "iPod Shuffle")
        product_page.load(device)
        product_page.information_block().open_share_link()
        share_page = ShareWindow(chrome)
        assert share_page.is_open_popup_share()


if __name__ == "__main__":
    run_testcase()

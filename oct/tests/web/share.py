# pylint: disable=no-self-use # pyATS-related exclusion


from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.share import ShareWindow
from oct.pages.product_page import ProductPage


class SharePopup(Testcase):
    @test
    def test(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        product_page = ProductPage(chrome, "34", "iPod Shuffle")
        product_page.open()
        product_page.information_block().open_share_link()
        share_page = ShareWindow(chrome)
        assert share_page.is_open_popup_share()


if __name__ == "__main__":
    run_testcase()

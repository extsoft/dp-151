# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.returns import ReturnsPage, ReturnsSuccessPage


class Returns(Testcase):
    @test
    def test(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        returns = ReturnsPage(chrome)
        returns.open()
        returns.fill_personal_details("Alex", "Alekseev", "didilov.al@gmail.com", "123456")
        returns.fill_order_details("214", "12-03-2019")
        returns.fill_product_details("iMac", "892123", "1", "New item has some scratches")
        returns.choose_reason_and_condition("1", "1")
        returns.press_submit()
        assert ReturnsSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

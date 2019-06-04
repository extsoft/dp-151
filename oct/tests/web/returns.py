# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.returns import ReturnsPage, ReturnsSuccessPage, Reason, Condition
from oct.browsers import Chrome
from oct.tests import run_testcase


class Returns(Testcase):
    @test
    def test(self, device: Device) -> None:
        chrome: Remote = Chrome()
        returns = ReturnsPage(chrome)
        returns.open(device)
        returns.fill_personal_details("Alex", "Alekseev", "didilov.al@gmail.com", "123456")
        returns.fill_order_details("214", "12-03-2019")
        returns.fill_product_details("iMac", "892123", "1", "New item has some scratches")
        returns.choose_reason_and_condition(Reason.FAULTY, Condition.NEW)
        returns.press_submit()
        assert ReturnsSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

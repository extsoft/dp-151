# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.returns import ReturnsPage, ReturnsSuccessPage, Reason, Condition
from oct.browsers import Chrome
from oct.tests import run_testcase


class Returns(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        generator = Person()
        returns = ReturnsPage(chrome)
        returns.load(device)
        returns.fill_personal_details(
            generator.name(), generator.last_name(), generator.email(), generator.password()
        )
        returns.fill_order_details("214", "12-03-2019")
        returns.fill_product_details("iMac", "892123", "1", "New item has some scratches")
        returns.choose_reason_and_condition(Reason.FAULTY, Condition.NEW)
        returns.press_submit()
        assert ReturnsSuccessPage(chrome).available()


if __name__ == "__main__":
    run_testcase()

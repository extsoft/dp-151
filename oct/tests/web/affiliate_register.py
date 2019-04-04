# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.topology import Device
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.tests import run_testcase
from oct.browsers import Chrome
from oct.pages.affiliate_register import RegisterAffiliatePage
from oct.pages.affiliate_register import RegAffiliateSuccessPage


class RegistrationAffiliate(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        registration = RegisterAffiliatePage(chrome)
        registration.open(device)
        registration.fill_personal_details("Jon", "Doe", "test10@gmail.com", "123456112")
        registration.press_pay_method()
        registration.fill_information(
            "one company", "www.website.com", "2332153467", "test10@gmail.com"
        )
        registration.fill_password("54321qwertyui")
        registration.press_continue()
        assert RegAffiliateSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

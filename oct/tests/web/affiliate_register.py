# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
from pyats.topology import Device
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.tests import run_testcase
from oct.browsers import Chrome
from oct.pages.affiliate_register import RegisterAffiliatePage
from oct.pages.affiliate_register import RegAffiliateSuccessPage


class RegistrationAffiliate(Testcase):
    @test
    def test(self, device: Device) -> None:
        chrome: Remote = Chrome()
        registration = RegisterAffiliatePage(chrome)
        generator = Person()
        registration.open(device)
        registration.fill_personal_details(
            generator.name(), generator.last_name(), generator.email(), generator.telephone()
        )
        registration.press_pay_method()
        registration.fill_information(
            generator.full_name(),
            f"www.{generator.username()}.com",
            "2332153467",
            generator.email(),
        )
        registration.fill_password(generator.password())
        registration.press_continue()
        assert RegAffiliateSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

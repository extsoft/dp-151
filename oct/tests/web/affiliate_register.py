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
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        registration = RegisterAffiliatePage(chrome)
        person = Person()
        registration.load(device)
        registration.fill_personal_details(
            person.name(), person.last_name(), person.email(), person.telephone()
        )
        registration.press_pay_method()
        registration.fill_information(
            person.full_name(), f"www.{person.username()}.com", "2332153467", person.email()
        )
        registration.fill_password(person.password())
        registration.press_continue()
        assert RegAffiliateSuccessPage(chrome).available()


if __name__ == "__main__":
    run_testcase()

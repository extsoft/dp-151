# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from mimesis import Person
from oct.pages.registration import RegisterAccountPage, RegistrationSuccessPage
from oct.browsers import Chrome
from oct.tests import run_testcase


class Registration(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        registration = RegisterAccountPage(chrome)
        registration.open(device)
        generator = Person()
        registration.fill_personal_details(
            generator.name(), generator.last_name(), generator.email(), generator.telephone()
        )
        registration.fill_password(generator.password())
        registration.press_continue()
        assert RegistrationSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

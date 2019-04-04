# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.registration import RegisterAccountPage, RegistrationSuccessPage
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.tests.web.creating_emails import EmailsGeneration


class Registration(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        registration = RegisterAccountPage(chrome)
        random_email = EmailsGeneration()
        registration.open(device)
        registration.fill_personal_details(
            "Jon", "Doe", random_email.creating_full_email(), "123456"
        )
        registration.fill_password("supersecret")
        registration.press_continue()
        assert RegistrationSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

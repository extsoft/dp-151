# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test

from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.registration import RegisterAccountPage, RegistrationSuccessPage
from selenium.webdriver import Remote


class Registration(Testcase):
    @test
    def test(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        registration = RegisterAccountPage(chrome)
        registration.open()
        registration.fill_personal_details("Jon", "Doe", "jb@jd.com", "123456")
        registration.fill_password("supersecret")
        registration.press_continue()
        assert RegistrationSuccessPage().loaded()


if __name__ == "__main__":
    run_testcase()

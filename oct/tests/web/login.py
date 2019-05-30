# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
from pyats.aetest import Testcase, test, setup
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.login import LoginPage
from oct.pages.account import AccountPage
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials


class Login(Testcase):
    generator = Person()
    email = generator.email()
    password = "987651"

    @setup
    def create_account(self, device: Device) -> None:
        assert "success" in UserRegistration(
            Identity(Person().email(), Person().email(), Person().telephone()),
            Credentials(self.email, self.password, "0"),
        ).registration_response(device)

    @test
    def login_exists_credentials(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open(device)
        login.fill_credentials(self.email, self.password)
        login.press_login_button()
        assert AccountPage(chrome).loaded()

    @test
    def login_nonexistent_email(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open(device)
        login.fill_credentials("Er12asd@mailinator.com", self.password)
        login.press_login_button()
        assert not AccountPage(chrome).loaded()

    @test
    def login_nonexistent_password(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open(device)
        login.fill_credentials(self.email, "12345789")
        login.press_login_button()
        assert not AccountPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

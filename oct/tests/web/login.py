# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test, setup
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.login import LoginPage
from oct.pages.account import AccountPage
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials
from oct.tests.web.creating_emails import EmailsGeneration


class Login(Testcase):
    email = EmailsGeneration().creating_full_email()
    password = "12345678"

    @setup
    def create_account(self) -> None:
        assert "success" in UserRegistration(
            Identity("Alex", "Ivanov", "+38090890812"), Credentials(self.email, self.password, "0")
        ).registration_response("localhost")

    @test
    def login_exists_credentials(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open()
        login.fill_credentials(self.email, self.password)
        login.press_login_button()
        assert AccountPage(chrome).loaded()

    @test
    def login_nonexistent_email(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open()
        login.fill_credentials("Er12asd@mailinator.com", self.password)
        login.press_login_button()
        assert not AccountPage(chrome).loaded()

    @test
    def login_nonexistent_password(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open()
        login.fill_credentials(self.email, "12345789")
        login.press_login_button()
        assert not AccountPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

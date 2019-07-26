# pylint: disable=no-self-use # pyATS-related exclusion
from selenium.webdriver import Remote
from pyats.topology import Device
from pyats.aetest import Testcase, test, setup
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.forgot_password import ForgotPasswordPage, ConfirmationMessage
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials
from oct.tests.web.creating_emails import EmailsGeneration


class ForgotPassword(Testcase):
    email = EmailsGeneration().creating_full_email()
    password = "12345wer8"

    @setup
    def create_account(self, device: Device) -> None:
        assert "success" in UserRegistration(
            Identity("Test", "test", "+38090890812"), Credentials(self.email, self.password, "0")
        ).registration_response(device)

    @test
    def test_forgot_password(self, device: Device) -> None:
        chrome: Remote = Chrome()
        forgot_password = ForgotPasswordPage(chrome)
        forgot_password.load(device)
        forgot_password.fill_email(self.email)
        forgot_password.press_continue_button()
        assert ConfirmationMessage(chrome).available()

    @test
    def test_forgot_password_with_not_existing_email(self, device: Device) -> None:
        chrome: Remote = Chrome()
        forgot_password = ForgotPasswordPage(chrome)
        forgot_password.load(device)
        forgot_password.fill_email("testerwom777@gmail.com")
        forgot_password.press_continue_button()
        assert not ConfirmationMessage(chrome).available()


if __name__ == "__main__":
    run_testcase()

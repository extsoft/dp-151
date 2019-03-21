# pylint: disable=no-self-use # pyATS-related exclusion
from selenium.webdriver import Remote
from pyats.aetest import Testcase, test
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.forgot_password import ForgotPasswordPage, ConfirmationMessage


class ForgotPassword(Testcase):
    @test
    def test_forgot_password(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        forgot_password = ForgotPasswordPage(chrome)
        forgot_password.open()
        forgot_password.fill_email("testerwom@gmail.com")
        forgot_password.press_continue_button()
        assert ConfirmationMessage(chrome).loaded()

    @test
    def test_forgot_password_with_not_existing_email(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        forgot_password = ForgotPasswordPage(chrome)
        forgot_password.open()
        forgot_password.fill_email("testerwom777@gmail.com")
        forgot_password.press_continue_button()
        assert not ConfirmationMessage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

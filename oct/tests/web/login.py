# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.login import LoginPage
from oct.pages.account import AccountPage


class Login(Testcase):
    @test
    def login_exists_credentials(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        login = LoginPage(chrome)
        login.open()
        login.fill_credentials("didilov.aleksey@gmail.com", "12345678")
        login.press_login_button()
        assert AccountPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

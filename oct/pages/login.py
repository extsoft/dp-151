from selenium.webdriver import Remote
from oct.pages.base import Page
from oct.pages.registration import PersonalDetails, Password


class LoginPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)
        self._email = PersonalDetails(browser)
        self._password = Password(browser)

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/login")

    def loaded(self) -> bool:
        return "Account Login" in self._browser.title

    def fill_credentials(self, email_address: str, password: str) -> None:
        self._email.type_email(email_address)
        self._password.type_password(password)

    def press_login_button(self) -> None:
        self._browser.find_element_by_xpath('//input[@value="Login"]').click()

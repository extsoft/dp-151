from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote
from oct.pages.base import Page
from oct.pages.registration import PersonalDetails


class ForgotPasswordPage:
    def __init__(self, browser: Remote):
        self._browser = browser
        self._users_email = PersonalDetails(browser)

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/forgotten")

    def loaded(self) -> bool:
        return "Forgot Your Password?" in self._browser.title

    def fill_email(self, email: str) -> None:
        self._users_email.type_email(email)

    def press_continue_button(self) -> None:
        self._browser.find_element_by_xpath("//*[@id='content']/form/div/div[2]/input").click()


class ConfirmationMessage(Page):
    def __init__(self, browser: Remote):
        self._browser = browser

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/account")

    def loaded(self) -> bool:
        try:
            self._browser.find_element_by_css_selector("div.alert.alert-success.alert-dismissible")
            return True
        except NoSuchElementException:
            return False

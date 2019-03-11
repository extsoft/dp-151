from selenium.webdriver import Remote
from oct.pages.base import Page


class AccountPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/account")

    def loaded(self) -> bool:
        return "My Account" in self._browser.title

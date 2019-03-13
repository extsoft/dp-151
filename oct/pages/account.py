from selenium.webdriver import Remote
from oct.pages.base import Page


class AccountPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/account")

    def loaded(self) -> bool:
        return "My Account" in self._browser.title

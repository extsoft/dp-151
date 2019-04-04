from selenium.webdriver import Remote
from pyats.topology import Device
from oct.pages.base import Page


class AccountPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def open(self, device: Device) -> None:
        self._browser.get(f"https://{device.connections.main.ip}/index.php?route=account/account")

    def loaded(self) -> bool:
        return "My Account" in self._browser.title

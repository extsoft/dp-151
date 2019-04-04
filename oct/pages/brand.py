from selenium.webdriver import Remote
from pyats.topology import Device
from oct.pages.base import Page


class BrandPage(Page):
    def __init__(self, browser: Remote, brand_id: str, brand_name: str):
        self._browser = browser
        self._brand_id = brand_id
        self._brand_name = brand_name

    def open(self, device: Device) -> None:
        self._browser.get(
            f"https://{device.connections.main.ip}"
            f"/index.php?route=product/manufacturer/info&manufacturer_"
            f"id={self._brand_id}"
        )

    def loaded(self) -> bool:
        return self._brand_name in self._browser.title

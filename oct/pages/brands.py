from enum import Enum
from selenium.webdriver import Remote
from pyats.topology import Device
from oct.pages.base import Page


class BrandList(Enum):

    APPLE = 1
    CANON = 2
    HEWLETTPACKARD = 3
    PALM = 4
    SONY = 5


class BrandsPage(Page):
    def __init__(self, browser: Remote):
        self._browser = browser

    def open(self, device: Device) -> None:
        self._browser.get(
            f"https://{device.connections.main.ip}/index.php?route=product/manufacturer"
        )

    def loaded(self) -> bool:
        return "Find Your Favorite Brand" in self._browser.title

    def click_brand_name(self, brand: BrandList) -> None:
        self._browser.find_element_by_xpath(f"//*[@id='content']/div[{brand.value}]/div/a").click()

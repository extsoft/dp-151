from selenium.webdriver import Remote
from oct.pages.base import Page


class BrandPage(Page):
    def __init__(self, browser: Remote, brand_id: str, brand_name: str):
        self._browser = browser
        self._brand_id = brand_id
        self._brand_name = brand_name

    def open(self) -> None:
        self._browser.get(
            f"http://localhost/index.php?route=product/manufacturer/info&manufacturer_"
            f"id={self._brand_id}"
        )

    def loaded(self) -> bool:
        return self._brand_name in self._browser.title

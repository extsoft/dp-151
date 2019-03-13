from selenium.webdriver import Remote
from oct.pages.base import Page


class AllBrandsPage(Page):
    def __init__(self, browser: Remote):
        self._browser = browser
        self._browser.implicitly_wait(5)

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=product/manufacturer")

    def loaded(self) -> bool:
        return "Find Your Favorite Brand" in self._browser.title

    def click_apple_brand(self) -> None:
        self._browser.find_element_by_xpath("//*[@id='content']/div[1]/div/a").click()

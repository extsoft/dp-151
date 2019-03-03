from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from oct.pages.base import Page


class ProductPage(Page):
    def __init__(self, browser: Remote, product_id: str, product_name: str):
        self._browser = browser
        self._product_id = product_id
        self._product_name = product_name
        self._browser.implicitly_wait(5)

    def open(self) -> None:
        self._browser.get(
            f"http://localhost/index.php?route=product/product&path=20_27&product_"
            f"id={self._product_id}"
        )

    def loaded(self) -> bool:
        return self._product_name in self._browser.title

    def open_brand_page(self) -> None:
        brand_name = self._browser.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[2]/ul[1]/li[1]/a'
        )
        brand_name.click()

    def press_add_to_cart(self) -> None:
        self._browser.find_element_by_id("button-cart").click()

    def successful_adding_to_cart(self) -> bool:
        try:
            self._browser.find_element_by_xpath('//*[@id="product-product"]/div[1]')
            return True
        except NoSuchElementException:
            return False

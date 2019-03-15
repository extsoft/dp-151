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

    def open_review_link(self) -> None:
        self._browser.find_element_by_xpath(
            '// * [ @ id = "content"] / div / div[1] / ul[2] / li[2] / a'
        ).click()

    def open_share_link(self) -> None:
        self._browser.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div[3]/div/a[4]/a[1]'
        ).click()

    def open_product_image(self) -> None:
        product_img = self._browser.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[1]/ul[1]/li[2]/a/img'
        )
        product_img.click()

    def is_open_image(self) -> bool:
        try:
            self._browser.find_element_by_class_name("mfp-img")
            return True
        except NoSuchElementException:
            return False

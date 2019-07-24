from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from pyats.topology import Device
from oct.pages.base import Page


class InformationBlock:
    def __init__(self, browser: Remote):
        self._browser = browser

    def open_brand_page(self) -> None:
        brand_name = self._browser.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[2]/ul[1]/li[1]/a'
        )
        brand_name.click()

    def open_share_link(self) -> None:
        self._browser.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div[3]/div/a[4]/a[1]'
        ).click()

    def add_to_wish_list(self) -> None:
        self._browser.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[2]/div[1]/button[1]'
        ).click()

    def add_to_cart(self) -> None:
        self._browser.find_element_by_id("button-cart").click()


class MessageBlock:
    def __init__(self, browser: Remote):
        self._browser = browser

    def has_wish_list_message(self) -> bool:
        try:
            self._browser.find_element_by_css_selector(
                "#product-product > div.alert.alert-success.alert-dismissible"
            )
            return True
        except NoSuchElementException:
            return False

    def has_cart_message(self) -> bool:
        try:
            self._browser.find_element_by_xpath('//*[@id="product-product"]/div[1]')
            return True
        except NoSuchElementException:
            return False


class ProductPage(Page):
    def __init__(self, browser: Remote, product_id: str, product_name: str):
        self._browser = browser
        self._product_id = product_id
        self._product_name = product_name
        self._info_block = InformationBlock(browser)
        self._message_block = MessageBlock(browser)

    def load(self, device: Device) -> None:
        self._browser.get(
            f"https://{device.connections.main.ip}/"
            f"index.php?route=product/product&path=20_27&product_"
            f"id={self._product_id}"
        )

    def available(self) -> bool:
        return self._product_name in self._browser.title

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

    def open_review_link(self) -> None:
        self._browser.find_element_by_xpath(
            '// * [ @ id = "content"] / div / div[1] / ul[2] / li[2] / a'
        ).click()

    def information_block(self) -> InformationBlock:
        return self._info_block

    def messages(self) -> MessageBlock:
        return self._message_block

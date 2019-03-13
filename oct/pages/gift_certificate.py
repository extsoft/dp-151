from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote
from oct.pages.base import Page


class GiftCertificate(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/voucher")

    def loaded(self) -> bool:
        return "Purchase a Gift Certificate" in self._browser.title

    def fill_certificate_data(
        self, recipient_name: str, recipient_email: str, gifter_name: str, gifter_email: str
    ) -> None:
        recipient_name_field = self._browser.find_element_by_id("input-to-name")
        recipient_name_field.click()
        recipient_name_field.send_keys(recipient_name)
        recipient_email_field = self._browser.find_element_by_id("input-to-email")
        recipient_email_field.click()
        recipient_email_field.send_keys(recipient_email)
        gifter_name_field = self._browser.find_element_by_id("input-from-name")
        gifter_name_field.click()
        gifter_name_field.send_keys(gifter_name)
        gifter_email_field = self._browser.find_element_by_id("input-from-email")
        gifter_email_field.click()
        gifter_email_field.send_keys(gifter_email)

    def chose_certificate_theme(self) -> None:
        self._browser.find_element_by_xpath("//input[@value='7']").click()

    def click_gift_checkbox(self) -> None:
        self._browser.find_element_by_xpath("//input[@name='agree']").click()

    def click_continue(self) -> None:
        self._browser.find_element_by_xpath("//input[@value = 'Continue']").click()


class PurchaseSuccessful(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def open(self) -> None:
        raise RuntimeError("This page can't be received via URL")

    def loaded(self) -> bool:
        try:
            self._browser.find_element_by_xpath(
                "//p[contains(text(), " "'Thank you for purchasing a gift certificate!')]"
            )
            return True
        except NoSuchElementException:
            return False

from enum import Enum
from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException
from oct.pages.base import Page
from oct.pages.registration import PersonalDetails


class Reason(Enum):
    BROKEN = 1
    FAULTY = 2
    ORDER_ERROR = 3
    OTHER = 4
    WRONG_ITEM = 5


class Condition(Enum):
    NEW = 0
    USED = 1


class OrderDetails:
    def __init__(self, browser: Remote):
        self._browser = browser

    def type_order_id(self, order_id: str) -> None:
        order_id_field = self._browser.find_element_by_id("input-order-id")
        order_id_field.click()
        order_id_field.send_keys(order_id)

    def type_order_date(self, order_date: str) -> None:
        order_date_field = self._browser.find_element_by_id("input-date-ordered")
        order_date_field.click()
        order_date_field.send_keys(order_date)


class ProductDetails:
    def __init__(self, browser: Remote):
        self._browser = browser

    def type_product_name(self, product_name: str) -> None:
        product_name_field = self._browser.find_element_by_id("input-product")
        product_name_field.click()
        product_name_field.send_keys(product_name)

    def type_product_code(self, product_code: str) -> None:
        product_code_field = self._browser.find_element_by_id("input-model")
        product_code_field.click()
        product_code_field.send_keys(product_code)

    def type_quantity(self, quantity: str) -> None:
        quantity_field = self._browser.find_element_by_id("input-quantity")
        quantity_field.click()
        quantity_field.clear()
        quantity_field.send_keys(quantity)

    def type_faulty(self, faulty: str) -> None:
        faulty_name_field = self._browser.find_element_by_id("input-comment")
        faulty_name_field.click()
        faulty_name_field.send_keys(faulty)


class ReturnsPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self.personal_details = PersonalDetails(browser)
        self._order_details = OrderDetails(browser)
        self._product_details = ProductDetails(browser)

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=account/return/add")

    def loaded(self) -> bool:
        return "Account Login" in self._browser.title

    def fill_personal_details(
        self, first_name: str, last_name: str, email: str, telephone: str
    ) -> None:
        self.personal_details.type_first_name(first_name)
        self.personal_details.type_last_name(last_name)
        self.personal_details.type_email(email)
        self.personal_details.type_telephone(telephone)

    def fill_order_details(self, order_id: str, order_date: str) -> None:
        self._order_details.type_order_id(order_id)
        self._order_details.type_order_date(order_date)

    def fill_product_details(
        self, product_name: str, product_code: str, quantity: str, faulty: str
    ) -> None:
        self._product_details.type_product_name(product_name)
        self._product_details.type_product_code(product_code)
        self._product_details.type_quantity(quantity)
        self._product_details.type_faulty(faulty)

    def choose_reason_and_condition(self, reason: Reason, product_condition: Condition) -> None:
        self._browser.find_element_by_xpath(
            f"//*[contains(@name, 'return_reason_id') and contains(@value, {reason.value})]"
        ).click()
        self._browser.find_element_by_xpath(
            f"//*[contains(@name, 'opened') and contains(@value, {product_condition.value})]"
        ).click()

    def press_submit(self) -> None:
        self._browser.find_element_by_xpath("//input[@value='Submit']").click()


class ReturnsSuccessPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def open(self) -> None:
        raise RuntimeError("This page is not available for open through an URL")

    def loaded(self) -> bool:
        try:
            return self._browser.find_element_by_xpath(
                "//p[contains(text(), ' You will be notified via e-mail"
                " as to the status of your request.')]"
            )
        except NoSuchElementException:
            return False

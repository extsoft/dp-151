from enum import Enum
from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException


class Rating(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class Review:
    def __init__(self, browser: Remote):
        self._browser = browser
        self._browser.implicitly_wait(5)

    def type_name(self, name: str) -> None:
        name_field = self._browser.find_element_by_id("input-name")
        name_field.click()
        name_field.send_keys(name)

    def type_review(self, review: str) -> None:
        review_field = self._browser.find_element_by_id("input-review")
        review_field.click()
        review_field.send_keys(review)

    def choose_rating(self, rating: Rating) -> None:
        rating_s = self._browser.find_element_by_xpath(
            f'//*[@id="form-review"]/div[4]/div/input' f"[{rating.value}]"
        )
        rating_s.click()
        rating_s.send_keys(rating.value)

    def press_continue(self) -> None:
        self._browser.find_element_by_class_name("btn-primary").click()

    def successfully_added(self) -> bool:
        try:
            self._browser.find_element_by_class_name("alert-success")
            return True
        except NoSuchElementException:
            return False

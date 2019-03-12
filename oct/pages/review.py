from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException


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

    def choose_rating_from_1_to_5(self, rating: int) -> None:
        rating_s = self._browser.find_element_by_xpath(
            f'//*[@id="form-review"]/div[4]/div/input' f"[{rating}]"
        )
        rating_s.click()
        rating_s.send_keys(rating)

    def press_continue(self) -> None:
        self._browser.find_element_by_class_name("btn-primary").click()

    def successfully_added(self) -> bool:
        try:
            self._browser.find_element_by_class_name("alert-success")
            return True
        except NoSuchElementException:
            return False

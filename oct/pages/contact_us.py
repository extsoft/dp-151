from selenium.webdriver import Remote
from oct.pages.base import Page
from oct.pages.registration import PersonalDetails


class ContactDetails:
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)

    def type_your_name(self, your_name: str) -> None:
        your_name_field = self._browser.find_element_by_id("input-name")
        your_name_field.click()
        your_name_field.send_keys(your_name)

    def type_enquiry(self, enquiry: str) -> None:
        enquiry_field = self._browser.find_element_by_id("input-enquiry")
        enquiry_field.click()
        enquiry_field.send_keys(enquiry)


class ContactUsPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)
        self._details = ContactDetails(browser)
        self._email = PersonalDetails(browser)

    def open(self) -> None:
        self._browser.get("http://localhost/index.php?route=information/contact")

    def loaded(self) -> bool:
        return "Contact Us" in self._browser.title

    def fill_contact_details(self, your_name: str, email: str, enquiry: str) -> None:
        self._details.type_your_name(your_name)
        self._email.type_email(email)
        self._details.type_enquiry(enquiry)

    def press_submit(self) -> None:
        self._browser.find_element_by_css_selector("input.btn").click()


class ContactUsSuccessPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)

    def open(self) -> None:
        raise RuntimeError("This page couldn't be open through an URL")

    def loaded(self) -> bool:
        return (
            "http://localhost/index.php?route=" "information/contact/success"
        ) in self._browser.current_url

from oct.pages import not_implemented
from oct.pages.base import Page
from selenium.webdriver import Remote


class PersonalDetails:
    def type_first_name(self, first_name: str) -> None:
        not_implemented(self)

    def type_last_name(self, last_name: str) -> None:
        not_implemented(self)

    def type_email(self, email: str) -> None:
        not_implemented(self)

    def type_telephone(self, telephone: str) -> None:
        not_implemented(self)


class Password:
    def type_password(self, password: str) -> None:
        not_implemented(self)

    def confirm_password(self, password: str) -> None:
        not_implemented(self)


class RegisterAccountPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._details = PersonalDetails()
        self._password = Password()

    def open(self) -> None:
        not_implemented(self)

    def loaded(self) -> bool:
        not_implemented(self)

    def fill_personal_details(
        self, first_name: str, last_name: str, email: str, telephone: str
    ) -> None:
        self._details.type_first_name(first_name)
        self._details.type_last_name(last_name)
        self._details.type_email(email)
        self._details.type_telephone(telephone)

    def fill_password(self, password: str) -> None:
        self._password.type_password(password)
        self._password.confirm_password(password)

    def press_continue(self) -> None:
        # check Privacy and press a button
        not_implemented(self)


class RegistrationSuccessPage(Page):
    def open(self) -> None:
        raise RuntimeError("This page can't be open through an URL")

    def loaded(self) -> bool:
        not_implemented(self)

from selenium.webdriver import Remote
from oct.pages.base import Page
from oct.pages.registration import PersonalDetails
from oct.pages.registration import Password
from oct.pages.registration import RegistrationSuccessPage
from oct.pages.registration import RegisterAccountPage


class AffiliateInformation:
    def __init__(self, browser: Remote):
        self._browser = browser
        self._browser.implicitly_wait(5)

    def type_company(self, company: str) -> None:
        company_field = self._browser.find_element_by_id("input-company")
        company_field.click()
        company_field.send_keys(company)

    def type_website(self, website: str) -> None:
        website_field = self._browser.find_element_by_id("input-website")
        website_field.click()
        website_field.send_keys(website)

    def type_tax(self, tax: str) -> None:
        web_site_field = self._browser.find_element_by_id("input-tax")
        web_site_field.click()
        web_site_field.send_keys(tax)

    def type_paypal(self, paypal: str) -> None:
        paypal_field = self._browser.find_element_by_id("input-paypal")
        paypal_field.click()
        paypal_field.send_keys(paypal)


class RegisterAffiliatePage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)
        self._personal_details = PersonalDetails(browser)
        self._information = AffiliateInformation(browser)
        self._password = Password(browser)
        self._press_continue = RegisterAccountPage(browser)

    def open(self) -> None:
        self._browser.get("https://localhost/index.php?route=affiliate/register")

    def loaded(self) -> bool:
        return "Affiliate Program" in self._browser.title

    def fill_personal_details(
        self, first_name: str, last_name: str, email: str, telephone: str
    ) -> None:
        self._personal_details.type_first_name(first_name)
        self._personal_details.type_last_name(last_name)
        self._personal_details.type_email(email)
        self._personal_details.type_telephone(telephone)

    def press_pay_method(self) -> None:
        self._browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/form/fieldset[2]/div[4]/div/div[2]/label/input"
        ).click()

    def fill_information(self, company: str, website: str, tax: str, paypal: str) -> None:
        self._information.type_company(company)
        self._information.type_website(website)
        self._information.type_tax(tax)
        self._information.type_paypal(paypal)

    def fill_password(self, passwords: str) -> None:
        self._password.type_password(passwords)
        self._password.confirm_password(passwords)

    def press_continue(self) -> None:
        self._press_continue.press_continue()


class RegAffiliateSuccessPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser
        self._browser.implicitly_wait(5)
        self._open = RegistrationSuccessPage(browser)

    def open(self) -> None:
        self._open.open()

    def loaded(self) -> bool:
        return "Your Affiliate Account Has Been Created!" in self._browser.title

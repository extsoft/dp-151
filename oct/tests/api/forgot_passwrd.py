# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
import urllib3
from pyats.aetest import Testcase, test, setup
from pyats.topology import Device
import requests
from oct.tests import run_testcase
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials


class ForgotPassword(Testcase):
    email = Person().email()
    password = "12345678"

    @setup
    def creating_account(self, device: Device) -> None:
        assert "success" in UserRegistration(
            Identity("Test", "Test", "+380957772255"), Credentials(self.email, self.password, "0")
        ).registration_response(device)

    @test
    def test_forgot_password_for_known_user(self, device: Device) -> None:
        parameters = {"email": self.email}
        urllib3.disable_warnings()
        request = requests.post(
            f"https://{device.connections.main.ip}/index.php?route=account/forgotten",
            parameters,
            verify=False,
        )
        assert "An email with a confirmation link has been sent your email address." in request.text

    @test
    def test_forgot_password_for_unknown_user(self, device: Device) -> None:
        parameters = {"email": "someemailll@gmail.com"}
        urllib3.disable_warnings()
        request = requests.post(
            f"https://{device.connections.main.ip}/index.php?route=account/forgotten",
            parameters,
            verify=False,
        )
        assert "The E-Mail Address was not found in our records, please try again!" in request.text


if __name__ == "__main__":
    run_testcase()

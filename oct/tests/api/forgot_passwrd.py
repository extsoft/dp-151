# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
import urllib3
from oct.tests import run_testcase


class ForgotPassword(Testcase):
    @test
    def test_forgot_password_for_known_user(self) -> None:
        parameters = {"email": "testerwom@gmail.com"}
        urllib3.disable_warnings()
        request = requests.post(
            "https://localhost/index.php?route=account/forgotten", parameters, verify=False
        )
        assert "An email with a confirmation link has been sent your email address." in request.text

    @test
    def test_forgot_password_for_unknown_user(self) -> None:
        parameters = {"email": "someemailll@gmail.com"}
        urllib3.disable_warnings()
        request = requests.post(
            "https://localhost/index.php?route=account/forgotten", parameters, verify=False
        )
        assert "The E-Mail Address was not found in our records, please try again!" in request.text


if __name__ == "__main__":
    run_testcase()

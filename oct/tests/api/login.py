# pylint: disable=no-self-use # pyATS-related exclusion
import requests
from pyats.aetest import Testcase, test, setup
from oct.tests import run_testcase
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials
from oct.tests.web.creating_emails import EmailsGeneration


class Login(Testcase):
    email = EmailsGeneration().creating_full_email()
    password = "12345638"

    @setup
    def create_account(self) -> None:
        assert "success" in UserRegistration(
            Identity("Alex", "Ivanov", "+38090890812"), Credentials(self.email, self.password, "0")
        ).registration_response("192.168.195.143")

    @test
    def login_exists_credentials(self) -> None:
        assert (
            "Edit Account"
            in requests.post(
                "https://192.168.195.143/index.php?route=account/login",
                {"email": self.email, "password": self.password},
                verify=False,
            ).text
        )

    @test
    def login_empty_email_parameter(self) -> None:
        assert (
            "Edit Account"
            not in requests.post(
                "https://192.168.195.143/index.php?route=account/login",
                {"email": "", "password": self.password},
                verify=False,
            ).text
        )

    @test
    def login_empty_password_parameter(self) -> None:
        assert (
            "Edit Account"
            not in requests.post(
                "https://192.168.195.143/index.php?route=account/login",
                {"email": self.email, "password": ""},
                verify=False,
            ).text
        )


if __name__ == "__main__":
    run_testcase()

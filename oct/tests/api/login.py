# pylint: disable=no-self-use # pyATS-related exclusion
import requests
from pyats.aetest import Testcase, test, setup
from pyats.topology import Device
from mimesis import Person
from oct.tests import run_testcase
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials


class Login(Testcase):
    person = Person()
    email = person.email()
    password = person.password()

    @setup
    def create_account(self, device: Device) -> None:
        assert "success" in UserRegistration(
            Identity(self.person.name(), self.person.last_name(), self.person.telephone()),
            Credentials(self.email, self.password, "0"),
        ).registration_response(device)

    @test
    def login_exists_credentials(self, device: Device) -> None:
        assert (
            "Edit Account"
            in requests.post(
                f"https://{device.connections.main.ip}/index.php?route=account/login",
                {"email": self.email, "password": self.password},
                verify=False,
            ).text
        )

    @test
    def login_empty_email_parameter(self, device: Device) -> None:
        assert (
            "Edit Account"
            not in requests.post(
                f"https://{device.connections.main.ip}/index.php?route=account/login",
                {"email": "", "password": self.password},
                verify=False,
            ).text
        )

    @test
    def login_empty_password_parameter(self, device: Device) -> None:
        assert (
            "Edit Account"
            not in requests.post(
                f"https://{device.connections.main.ip}/index.php?route=account/login",
                {"email": self.email, "password": ""},
                verify=False,
            ).text
        )


if __name__ == "__main__":
    run_testcase()

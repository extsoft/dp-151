# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from oct.tests import run_testcase
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials
from oct.tests.web.creating_emails import EmailsGeneration


class Registration(Testcase):
    @test
    def registration_positive_test(self, device: Device) -> None:
        assert "success" in UserRegistration(
            Identity("Alex", "Ivanov", "+38090890812"),
            Credentials(EmailsGeneration().creating_full_email(), "12345678", "0"),
        ).registration_response(device)


if __name__ == "__main__":
    run_testcase()

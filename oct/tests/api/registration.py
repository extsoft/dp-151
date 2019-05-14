# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from mimesis import Person
from oct.tests import run_testcase
from oct.tests.api.registration_pattern import UserRegistration, Identity, Credentials


class Registration(Testcase):
    @test
    def registration_positive_test(self, device: Device) -> None:
        generator = Person()
        assert "success" in UserRegistration(
            Identity(generator.name(), generator.last_name(), generator.telephone()),
            Credentials(generator.email(), generator.password(), "0"),
        ).registration_response(device)


if __name__ == "__main__":
    run_testcase()

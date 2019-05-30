# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
import urllib3
from pyats.topology import Device
from pyats.aetest import Testcase, test
import requests
from oct.tests import run_testcase


class ContactUs(Testcase):
    @test
    def test_contact_us(self, device: Device) -> None:
        urllib3.disable_warnings()
        generator = Person()
        assert "success" in requests.post(
            f"https://{device.connections.main.ip}/index.php?route=information/contact",
            {
                "name": generator.name(),
                "email": generator.email(),
                "enquiry": "test data test data",
            },
            verify=False,
        )


if __name__ == "__main__":
    run_testcase()

# pylint: disable=no-self-use # pyATS-related exclusion
import urllib3
from pyats.topology import Device
from pyats.aetest import Testcase, test
import requests
from oct.tests import run_testcase


class ContactUs(Testcase):
    @test
    def test_contact_us(self, device: Device) -> None:
        parameters = {"name": "Alex", "email": "test@gmail.com", "enquiry": "test data test data"}
        urllib3.disable_warnings()
        request = requests.post(
            f"https://{device.connections.main.ip}/index.php?route=information/contact",
            parameters,
            verify=False,
        )
        assert "success" in request.url


if __name__ == "__main__":
    run_testcase()

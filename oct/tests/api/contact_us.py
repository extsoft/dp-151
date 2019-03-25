# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
import urllib3
from oct.tests import run_testcase


class ContactUs(Testcase):
    @test
    def test_contact_us(self) -> None:
        parameters = {"name": "Alex", "email": "test@gmail.com", "enquiry": "test data test data"}
        urllib3.disable_warnings()
        request = requests.post(
            "https://192.168.195.143/index.php?route=information/contact", parameters, verify=False
        )
        assert "Contact Us" in request.text and "success" in request.url


if __name__ == "__main__":
    run_testcase()

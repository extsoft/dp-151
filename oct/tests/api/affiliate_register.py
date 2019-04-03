# pylint: disable=no-self-use # pyATS-related exclusion
import urllib3
import requests
from pyats.aetest import test, Testcase
from pyats.topology import Device
from oct.tests import run_testcase


class AffiliateReg(Testcase):
    @test
    def test_affiliate_reg(self, device: Device) -> None:
        urllib3.disable_warnings()
        params = {
            "firstname": "Alex",
            "lastname": "Second",
            "email": "ates122@gmail.com",
            "telephone": "+380989898989",
            "company": "Company",
            "website": "www.company-site.net",
            "tax": "123456",
            "payment": "paypal",
            "paypal": "atet122@gmail.com",
            "password": "12345",
            "confirm": "12345",
            "agree": 1,
        }
        register_request = requests.post(
            f"https://{device.connections.main.ip}/index.php?route=affiliate/register",
            params,
            verify=False,
        )
        assert "success" in register_request.url


if __name__ == "__main__":
    run_testcase()

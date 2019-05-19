# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
import urllib3
import requests
from pyats.aetest import test, Testcase
from pyats.topology import Device
from oct.tests import run_testcase


class AffiliateReg(Testcase):
    @test
    def test_affiliate_reg(self, device: Device) -> None:
        urllib3.disable_warnings()
        generator = Person()
        params = {
            "firstname": generator.name(),
            "lastname": generator.last_name(),
            "email": generator.email(),
            "telephone": generator.telephone(),
            "company": generator.full_name(),
            "website": f"www.{generator.username()}.net",
            "tax": "123456",
            "payment": "paypal",
            "paypal": generator.email(),
            "password": generator.password(),
            "confirm": generator.password(),
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

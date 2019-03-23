# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
from oct.tests import run_testcase


class AffiliateReg(Testcase):
    @test
    def test_affiliate_reg(self) -> None:
        params = {
            "firstname": "Alex",
            "lastname": "Second",
            "email": "atest122@gmail.com",
            "telephone": "+380989898989",
            "company": "Company",
            "website": "www.company-site.net",
            "tax": "123456",
            "payment": "paypal",
            "paypal": "atest122@gmail.com",
            "password": "12345",
            "confirm": "12345",
            "agree": 1,
        }
        register_request = requests.post(
            "http://localhost/index.php?route=affiliate/register", params
        )
        assert "Your Affiliate Account Has Been Created!" in register_request.text


if __name__ == "__main__":
    run_testcase()

# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
import urllib3
from oct.tests import run_testcase


class GiftCertificate(Testcase):
    @test
    def test_gift_certificate(self) -> None:
        urllib3.disable_warnings()
        parameters = {
            "to_name": "green22",
            "to_email": "green222@gmail.com",
            "from_name": "red22",
            "from_email": "red222@gmail.com",
            "voucher_theme_id": 7,
            "message": "some text",
            "amount": 1,
            "agree": 1,
        }
        gift_request = requests.post(
            "https://192.168.195.143/index.php?route=account/voucher", parameters, verify=False
        )
        assert "success" in gift_request.url


if __name__ == "__main__":
    run_testcase()

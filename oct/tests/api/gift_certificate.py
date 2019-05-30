# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.topology import Device
from pyats.aetest import Testcase, test
import requests
import urllib3
from oct.tests import run_testcase


class GiftCertificate(Testcase):
    @test
    def test_gift_certificate(self, device: Device) -> None:
        urllib3.disable_warnings()
        assert "success" in requests.post(
            f"https://{device.connections.main.ip}/index.php?route=account/voucher",
            {
                "to_name": "green22",
                "to_email": "green222@gmail.com",
                "from_name": "red22",
                "from_email": "red222@gmail.com",
                "voucher_theme_id": 7,
                "message": "some text",
                "amount": 1,
                "agree": 1,
            },
            verify=False,
        )


if __name__ == "__main__":
    run_testcase()

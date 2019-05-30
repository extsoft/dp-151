# pylint: disable=no-self-use # pyATS-related exclusion
import urllib3
import requests
from pyats.topology import Device
from pyats.aetest import Testcase, test
from oct.tests import run_testcase


class Review(Testcase):
    @test
    def test_review(self, device: Device) -> None:
        urllib3.disable_warnings()
        assert (
            "Thank you for your review. It has been submitted to the webmaster for approval."
            in requests.post(
                f"https://{device.connections.main.ip}/"
                f"index.php?route=product/product/write&product_id=40",
                {
                    "name": "Solomon",
                    "text": "This is auto test-bot review. This is auto test-bot review.",
                    "rating": "5",
                },
                verify=False,
            )
        )


if __name__ == "__main__":
    run_testcase()

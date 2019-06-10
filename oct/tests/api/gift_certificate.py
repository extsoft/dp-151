# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.topology import Device
from pyats.aetest import Testcase, test
from oct.tests import run_testcase
from oct.tests.api.returns import assert_if_request_contains_success_response_text
from oct.tests.api.affiliate_register import Post


class GiftCertificate(Testcase):
    @test
    def test_gift_certificate(self, device: Device) -> None:
        assert_if_request_contains_success_response_text(
            Post(
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
            ),
            "success",
        )


if __name__ == "__main__":
    run_testcase()

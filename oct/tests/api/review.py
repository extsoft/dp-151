# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.topology import Device
from pyats.aetest import Testcase, test
from oct.tests import run_testcase
from oct.tests.api.affiliate_register import Post
from oct.tests.api.returns import assert_if_request_contains_success_response_text


class Review(Testcase):
    @test
    def test_review(self, device: Device) -> None:
        assert_if_request_contains_success_response_text(
            Post(
                f"https://{device.connections.main.ip}/"
                f"index.php?route=product/product/write&product_id=40",
                {
                    "name": "Solomon",
                    "text": "This is auto test-bot review. This is auto test-bot review.",
                    "rating": "5",
                },
            ),
            "Thank you for your review. It has been submitted to the webmaster for approval.",
        )


if __name__ == "__main__":
    run_testcase()

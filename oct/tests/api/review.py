# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
from oct.tests import run_testcase


class Review(Testcase):
    @test
    def test_review(self) -> None:
        params = {
            "name": "Solomon",
            "text": "This is auto test-bot review. This is auto test-bot review.",
            "rating": "5",
        }

        review_request = requests.post(
            "http://localhost/index.php?route=product/product/write&product_id=40", params
        )
        assert (
            "Thank you for your review. It has been submitted to the webmaster for approval."
            in review_request.text
        )


if __name__ == "__main__":
    run_testcase()

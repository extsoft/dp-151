# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from oct.tests import run_testcase
from oct.tests.api.affiliate_register import Post


def assert_if_request_contains_success_response_text(post: Post, text: str) -> None:
    assert text in post.response().text


class Returns(Testcase):
    @test
    def test_returns(self, device: Device) -> None:
        assert_if_request_contains_success_response_text(
            Post(
                f"https://{device.connections.main.ip}/index.php?route=account/return/add",
                {
                    "firstname": "Alex",
                    "lastname": "Petrov",
                    "email": "newaddr@gmail.com",
                    "telephone": "+380963453377",
                    "order_id": "1234",
                    "date_ordered": "2019-03-22",
                    "product": "apple",
                    "model": "Imac",
                    "quantity": 1,
                    "return_reason_id": 4,
                    "opened": 1,
                    "comment": "New item has some scratches",
                },
            ),
            "Thank you for submitting your return request."
            " Your request has been sent to the relevant department for processing",
        )


if __name__ == "__main__":
    run_testcase()

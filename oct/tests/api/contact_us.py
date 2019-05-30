# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
from pyats.topology import Device
from pyats.aetest import Testcase, test
from oct.tests import run_testcase
from oct.tests.api.affiliate_register import assert_if_request_contains_success_response_url, Post


class ContactUs(Testcase):
    @test
    def test_contact_us(self, device: Device) -> None:
        generator = Person()
        assert_if_request_contains_success_response_url(
            Post(
                f"https://{device.connections.main.ip}/index.php?route=information/contact",
                {
                    "name": generator.name(),
                    "email": generator.email(),
                    "enquiry": "test data test data",
                },
            )
        )


if __name__ == "__main__":
    run_testcase()

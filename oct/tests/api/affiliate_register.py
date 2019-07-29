# pylint: disable=no-self-use # pyATS-related exclusion
from typing import Dict, Union
from mimesis import Person
import urllib3
import requests
from pyats.aetest import test, Testcase
from pyats.topology import Device
from oct.tests import run_testcase


class Post:
    def __init__(self, url: str, data: Dict[str, Union[int, str]]) -> None:
        self._url = url
        self._data = data

    def response(self) -> requests.Response:
        return requests.post(self._url, self._data, verify=False)


def assert_if_request_contains_success_response_url(post: Post) -> None:
    assert "success" in post.response().url


class AffiliateReg(Testcase):
    @test
    def test_affiliate_reg(self, device: Device) -> None:
        urllib3.disable_warnings()
        person = Person()
        (
            assert_if_request_contains_success_response_url(
                Post(
                    f"https://{device.connections.main.ip}/index.php?route=affiliate/register",
                    {
                        "firstname": person.name(),
                        "lastname": person.last_name(),
                        "email": person.email(),
                        "telephone": person.telephone(),
                        "company": person.full_name(),
                        "website": f"www.{person.username()}.net",
                        "tax": "123456",
                        "payment": "paypal",
                        "paypal": person.email(),
                        "password": person.password(),
                        "confirm": person.password(),
                        "agree": 1,
                    },
                )
            )
        )


if __name__ == "__main__":
    run_testcase()

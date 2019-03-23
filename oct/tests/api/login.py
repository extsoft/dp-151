# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
import urllib3
from oct.tests import run_testcase


class Login(Testcase):
    @test
    def test_login(self) -> None:
        parameters = {"email": "didilov.aleksey@gmail.com", "password": "12345678"}
        urllib3.disable_warnings()
        request = requests.post(
            "https://192.168.195.143/index.php?route=account/login", parameters, verify=False
        )
        assert "My Account" in request.text


if __name__ == "__main__":
    run_testcase()

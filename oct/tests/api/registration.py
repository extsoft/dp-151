# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
import requests
from oct.tests import run_testcase


class Registration(Testcase):
    @test
    def test_registration(self) -> None:
        parameters = {
            "customer_group_id": 1,
            "firstname": "Alex",
            "lastname": "Aleks",
            "email": "asttwe227@gmail.com",
            "telephone": "+380989898989",
            "password": "1234",
            "confirm": "1234",
            "newsletter": 0,
            "agree": 1,
        }
        request = requests.post("http://localhost/index.php?route=account/register", parameters)
        assert "Your Account Has Been Created!" in request.text


if __name__ == "__main__":
    run_testcase()

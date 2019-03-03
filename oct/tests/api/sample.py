# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test

from oct.tests import run_testcase


class SampleApiTest(Testcase):
    @test
    def to_be_deleted(self) -> None:
        print("Please delete me (SampleApiTest) once a real test is added.")


if __name__ == "__main__":
    run_testcase()

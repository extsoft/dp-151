# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test

from oct.tests import run_testcase


class SampleWebTest(Testcase):
    @test
    def to_be_deleted(self):
        print("Please delete me (SampleWebTest) once a real test is added.")


if __name__ == "__main__":
    run_testcase()

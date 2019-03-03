# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test

from oct.tests import run_testcase


class SampleDeploymentTest(Testcase):
    @test
    def to_be_deleted(self):
        print("Please delete me (SampleDeploymentTest) once a real test is added.")


if __name__ == "__main__":
    run_testcase()

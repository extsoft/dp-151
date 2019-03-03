from pyats.aetest import Testcase, test

from oct.tests import run_module


class SampleDeploymentTest(Testcase):
    @test
    def to_be_deleted(self):
        print("Please delete me once a real test is added.")


if __name__ == "__main__":
    run_module()

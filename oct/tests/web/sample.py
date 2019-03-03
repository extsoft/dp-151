# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test

from oct.tests import run_testcase
from oct.browsers import Chrome


class SampleWebTest(Testcase):
    @test
    def to_be_deleted(self, grid: str) -> None:
        chrome = Chrome(grid)
        chrome.get("http://google.com")
        chrome.refresh()
        print("Please delete me (SampleWebTest) once a real test is added.")


if __name__ == "__main__":
    run_testcase()

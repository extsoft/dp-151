from typing import Dict, Any

from pyats import aetest
from pyats.topology import loader
from pyats.topology.testbed import Testbed  # pylint: disable=no-name-in-module


def mandatory_aetest_arguments(testbed: Testbed,) -> Dict[str, Any]:
    return {"testbed": testbed, "grid": testbed.custom["selenium-grid"]}


def run_testcase(testbed_file: str = "testbed.yaml") -> None:
    aetest.main(
        **mandatory_aetest_arguments(loader.load(testbed_file))  # pylint: disable=no-member
    )

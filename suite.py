# pylint: disable=no-value-for-parameter
import sys
import os
from typing import List, Tuple, Any
from pyats import easypy

from pyats.easypy.main import EasypyRuntime

from oct.tests import mandatory_aetest_arguments
from oct.tests.web import review as web_review
from oct.tests.api import forgot_passwrd, review

_api_tests = (review, forgot_passwrd)

_web_tests = (web_review,)


def tests_runner(test_suite: Tuple, instance: Any) -> List:  # type: ignore
    test_suite_results = list()
    for test_module in test_suite:
        full_test_path = test_module.__file__
        test_result = easypy.run(  # pylint: disable=no-member
            taskid=" -> ".join(
                (
                    os.path.dirname(full_test_path).split(os.sep)[-1],
                    os.path.basename(full_test_path),
                )
            ),
            testscript=full_test_path,
            **mandatory_aetest_arguments(instance, device_name="vm"),
        )
        test_suite_results.append(str(test_result))
    return test_suite_results


def main(runtime: EasypyRuntime) -> None:
    if "failed" not in tests_runner(_api_tests, runtime.testbed):
        tests_runner(_web_tests, runtime.testbed)


if __name__ == "__main__":
    # This configuration allow to replace `easypy` with a Python runner.
    #
    # It means that
    #    easypy suite.py.py <...>
    # you can replace with
    #    python suite.py.py <...>
    # where <...> are easypy's arguments.
    #
    # We add a name of this module as first parameter to the `sys.argv`
    # as `easypy` expect it as positional parameter.
    sys.argv = [sys.argv[0]] + sys.argv
    easypy.main()

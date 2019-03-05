import sys
import os
from pyats import easypy

from pyats.easypy.main import EasypyRuntime

from oct.tests import mandatory_aetest_arguments
from oct.tests.web import sample as web_sample_test
from oct.tests.api import sample as api_sample_test
from oct.tests.deployment import sample as deployment_sample_test

_api_tests = (api_sample_test,)

_web_tests = (web_sample_test,)

_deployment_tests = (deployment_sample_test,)


def main(runtime: EasypyRuntime) -> None:
    for test_module in _api_tests + _web_tests + _deployment_tests:
        full_test_path = test_module.__file__
        easypy.run(  # pylint: disable=no-member
            taskid=" -> ".join(
                (
                    os.path.dirname(full_test_path).split(os.sep)[-1],
                    os.path.basename(full_test_path),
                )
            ),
            testscript=full_test_path,
            **mandatory_aetest_arguments(runtime.testbed),
        )


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

# pylint: disable=no-value-for-parameter
import sys
import os
from pyats import easypy

from pyats.easypy.main import EasypyRuntime

from oct.tests import mandatory_aetest_arguments
from oct.tests.web import sample as web_sample_test
from oct.tests.web import adding_to_cart
from oct.tests.web import adding_to_wish_list
from oct.tests.web import affiliate_register as web_affiliate_register_test
from oct.tests.web import brand
from oct.tests.web import contact_us as web_contact_us_test
from oct.tests.web import creating_emails
from oct.tests.web import forgot_password_test
from oct.tests.web import gift_certificate
from oct.tests.web import login as web_login_test
from oct.tests.web import open_prod_img
from oct.tests.web import registration as web_registration_test
from oct.tests.web import returns as web_returns_test
from oct.tests.web import review as web_review_test
from oct.tests.web import share
from oct.tests.api import affiliate_register
from oct.tests.api import contact_us
from oct.tests.api import forgot_passwrd
from oct.tests.api import login
from oct.tests.api import registration
from oct.tests.api import returns
from oct.tests.api import review
from oct.tests.deployment import deploy_app


_api_tests = (affiliate_register, contact_us, forgot_passwrd, login, registration, returns, review)

_web_tests = (
    web_sample_test,
    adding_to_cart,
    adding_to_wish_list,
    web_affiliate_register_test,
    brand,
    web_contact_us_test,
    creating_emails,
    forgot_password_test,
    gift_certificate,
    web_login_test,
    open_prod_img,
    web_registration_test,
    web_returns_test,
    web_review_test,
    share,
)

_deployment_tests = (deploy_app,)


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
            **mandatory_aetest_arguments(runtime.testbed, device_name="vm"),
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

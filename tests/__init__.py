from tests.testbed_validation_rules import Rules
from tests.testbed_validation_rules import CheckUserCredentials
from tests.testbed_validation_rules import CheckDevicesIp
from tests.testbed_validation_rules import CheckSeleniumGridUrl
from tests.testbed_validation_rules import CheckServerIp


testbed_rules = (CheckUserCredentials(), CheckDevicesIp(), CheckSeleniumGridUrl(), CheckServerIp())

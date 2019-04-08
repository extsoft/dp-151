import collections
import logging
from abc import ABC, abstractmethod
import re
from typing import Sequence, List
from pyats.topology.testbed import Testbed


_log: logging.Logger = logging.getLogger(__name__)

Result = collections.namedtuple("Result", "rule run_status reason")


class Rule(ABC):

    ip_pattern = r"^\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}$"

    @abstractmethod
    def is_passed(self, testbed: Testbed) -> List[Result]:
        """Provides a result of rule execution"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Returns rule name"""
        pass


class CheckUserCredentials(Rule):
    def is_passed(self, testbed: Testbed) -> List[Result]:
        results = []
        for device in testbed:
            try:
                device.connect()
                results.append(Result(rule=self.__str__(), run_status=True, reason="Passed"))
            except Exception:
                message = (
                    f'Could not connect to "{device}" with following credentials: '
                    f"{device.connections.main.username}/{device.connections.main.password}"
                )
                results.append(Result(rule=self.__str__(), run_status=False, reason=message))
                continue
        return results

    def __str__(self) -> str:
        return "Check user credentials"


class CheckDevicesIp(Rule):
    def is_passed(self, testbed: Testbed) -> List[Result]:
        results = []
        for device in testbed:
            device_ip = str(device.connections.main.ip)
            has_passed = bool(re.fullmatch(self.ip_pattern, device_ip))
            message = (
                "Passed"
                if has_passed
                else f'"{device}" device: IP address "{device_ip}" does not conform to IP pattern "{self.ip_pattern}"'
            )
            results.append(Result(rule=self.__str__(), run_status=has_passed, reason=message))
        return results

    def __str__(self) -> str:
        return "Check devices ip format"


class CheckSeleniumGridUrl(Rule):

    url_pattern = r"^https?:\/\/.+:\d+$"

    def is_passed(self, testbed: Testbed) -> List[Result]:
        grid_url = testbed.custom["selenium-grid"]
        has_passed = bool(re.fullmatch(self.url_pattern, grid_url))
        message = (
            "Passed"
            if has_passed
            else f'Selenium grid url "{grid_url}" does not conform to url pattern "{self.url_pattern}"'
        )
        return [Result(rule=self.__str__(), run_status=has_passed, reason=message)]

    def __str__(self) -> str:
        return "Check Selenium grid url format"


class CheckServerIp(Rule):
    def is_passed(self, testbed: Testbed) -> List[Result]:
        server_ip = testbed.servers.server_alias.address
        has_passed = bool(re.fullmatch(self.ip_pattern, server_ip))
        message = (
            "Passed"
            if has_passed
            else f'Server IP address "{server_ip}" does not conform to IP pattern "{self.ip_pattern}"'
        )
        return [Result(rule=self.__str__(), run_status=has_passed, reason=message)]

    def __str__(self) -> str:
        return "Check server ip format"


class Rules:
    def __init__(self, rules: Sequence[Rule]):
        self._rules = rules

    def validate(self, testbed: Testbed) -> None:
        results = [rule.is_passed(testbed) for rule in self._rules]
        flat_results = [result for sublist in results for result in sublist]
        if not all([result.run_status for result in flat_results]):
            _log.info("Testbed validations".upper().center(100))
            for result in flat_results:
                _log.info(f"{result.rule}: " + result.reason.rjust(100 - len(result.rule)))
            raise AssertionError("Testbed validation rule/s failed! Please fix errors!!!")

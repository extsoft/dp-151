import logging
from abc import ABC, abstractmethod
import re
from typing import Sequence, Iterable
from pyats.topology import Testbed, Device

_log: logging.Logger = logging.getLogger(__name__)


class TestbedRule(ABC):
    @abstractmethod
    def results(self, testbed: Testbed) -> Iterable["Result"]:
        """Provides the results of rule execution."""

    @abstractmethod
    def __str__(self) -> str:
        """Returns rule name."""


class Result:
    def __init__(self, rule: TestbedRule, passed: bool, target: str):
        self.rule = rule
        self.passed = passed
        self.details = target

    def __str__(self) -> str:
        return f"{self.rule} => {self.details}"


class DevicesConnectivity(TestbedRule):
    def __init__(self, connection_name: str):
        self._connection_name = connection_name

    def results(self, testbed: Testbed) -> Iterable[Result]:
        def inspect(device: Device) -> Result:
            connection = device.connections[self._connection_name]
            identity = f"{device.name}['{connection.username}':'{connection.password}']"
            try:
                device.connect()
                return Result(self, True, identity)
            except Exception:  # pylint: disable=broad-except
                return Result(self, False, identity)

        return tuple(map(inspect, testbed))

    def __str__(self) -> str:
        return f"Devices connectivity of '{self._connection_name}' connection"


class SeleniumGridUrlCorrectness(TestbedRule):
    _url_pattern = r"^https?:\/\/.+:\d+$"

    def results(self, testbed: Testbed) -> Iterable[Result]:
        grid_url = testbed.custom["selenium-grid"]
        return [
            Result(
                rule=self, passed=bool(re.fullmatch(self._url_pattern, grid_url)), target=grid_url
            )
        ]

    def __str__(self) -> str:
        return f"Selenium Grid URL matching '{self._url_pattern}' pattern"


class TestbedRules:
    def __init__(
        self,
        rules: Sequence[TestbedRule] = (DevicesConnectivity("main"), SeleniumGridUrlCorrectness()),
    ):
        self._rules = rules

    def apply(self, testbed: Testbed) -> None:
        results = [rule.results(testbed) for rule in self._rules]
        flat_results = [result for sublist in results for result in sublist]
        fails = filter(lambda result: not result.passed, flat_results)
        if fails:
            _log.info("Testbed validations is failed. There are the following errors:")
            for result in fails:
                _log.info("- %s", result)
            raise AssertionError("Testbed validation rule/s failed! Please fix errors!!!")

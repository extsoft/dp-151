import functools
import weakref
import logging
from typing import Any

from selenium.webdriver import Remote


_log = logging.getLogger(__name__)

_chrome_settings = {
    "version": "ANY",
    "platform": "ANY",
    "browserName": "chrome",
    "os_version": "High Sierra",
    "browser_version": "74.0.3729.169",
}


class Chrome:
    """The class is a proxy for ``Remote`` object.

    The class is introduced to manage a browser lifecycle. It means:
        - lazy browser initialization - open a browser in the case of real interaction
        - automatic session closing - close a browser while destroying the instance of this object

    It has the same interface that ``Remote`` object from ``selenium.webdriver`` module has.
    """

    def __init__(self) -> None:
        @functools.lru_cache()
        def con() -> Remote:

            _log.info("Starting a browser session. Connect to: %s", _chrome_settings)
            remote = Remote("http://localhost:4444/wd/hub", _chrome_settings)
            remote.implicitly_wait(5)
            return remote

        self._client = con

        def close(cache: Any) -> None:
            if cache.cache_info().currsize > 0:
                _log.info("Closing the browser session. Disconnect from %s", _chrome_settings)
                cache().quit()

        weakref.finalize(self, close, self._client)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._client(), name)

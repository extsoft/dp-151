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
    "browser_version": "ANY",
}


class Chrome:
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

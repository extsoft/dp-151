from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException


class ShareWindow:
    def __init__(self, browser: Remote):
        self._browser = browser
        self._browser.implicitly_wait(5)

    def is_open_popup_share(self) -> bool:
        try:
            self._browser.find_element_by_xpath('//*[@id="at-expanded-menu-container"]/div[2]')
            return True
        except NoSuchElementException:
            return False

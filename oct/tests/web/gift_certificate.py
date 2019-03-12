# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.gift_certificate import GiftCertificate, PurchaseSuccessful


class GiftCertificateTest(Testcase):
    @test
    def purchase_gift_certificate(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        gift = GiftCertificate(chrome)
        gift.open()
        gift.fill_certificate_data(
            "green235", "green235@gmail.com", "green657", "green456@gmail.com"
        )
        gift.chose_certificate_theme()
        gift.click_gift_checkbox()
        gift.click_continue()
        assert PurchaseSuccessful(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

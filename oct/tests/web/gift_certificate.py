# pylint: disable=no-self-use # pyATS-related exclusion
from mimesis import Person
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.gift_certificate import GiftCertificate, PurchaseSuccessful
from oct.browsers import Chrome
from oct.tests import run_testcase


class GiftCertificateTest(Testcase):
    @test
    def purchase_gift_certificate(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        generator = Person()
        gift = GiftCertificate(chrome)
        gift.open(device)
        gift.fill_certificate_data(
            generator.name(), generator.email(), generator.username(), generator.email()
        )
        gift.chose_certificate_theme()
        gift.click_gift_checkbox()
        gift.click_continue()
        assert PurchaseSuccessful(chrome).loaded()


if __name__ == "__main__":
    run_testcase()

# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.tests import run_testcase
from oct.browsers import Chrome
from oct.pages.brand import BrandPage
from oct.pages.brands import BrandsPage, BrandList


class AllBrands(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        brands_page = BrandsPage(chrome)
        brands_page.load(device)
        brands_page.click_brand_name(BrandList.APPLE)
        assert BrandPage(chrome, "8", "Apple").available()


if __name__ == "__main__":
    run_testcase()

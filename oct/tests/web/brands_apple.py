# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.tests import run_testcase
from oct.pages.brand import BrandPage
from oct.pages.all_brands import AllBrandsPage


class BrandsApple(Testcase):
    @test
    def test(self, grid: str) -> None:
        chrome: Remote = Chrome(grid)
        brands_page = AllBrandsPage(chrome)
        brands_page.open()
        brands_page.loaded()
        brands_page.click_apple_brand()
        assert BrandPage(chrome, "8", "Apple").loaded()


if __name__ == "__main__":
    run_testcase()

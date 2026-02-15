from playwright.sync_api import expect

from PythonProject.Python_trenning.pom_exemple_project.pages.adv_page import AdvPage
from PythonProject.Python_trenning.pom_exemple_project.pages.search_page import SearchPage


class TestEbayTest:
    def test_search_for_camera(self,setup_playwright_project):
        page = setup_playwright_project
        page.goto("https://www.ebay.com/")
        search_page = SearchPage(page)
        search_page.search_for_items("Camera Canon")
        text = search_page.get_amount_after_search()
        assert int(text)>100

    def test_click_on_advanced_link(self,setup_playwright_project):
        page = setup_playwright_project
        page.goto("https://www.ebay.com/")
        search_page = SearchPage(page)
        search_page.click_on_advanced_link()
        expect(page).to_have_url("https://www.ebay.com/sch/ebayadvsearch")
        assert page.title() == "Advanced Search | eBay", "Page title is not as expected after click_on_advanced_link"

    def test_search_from_adv_page(self, setup_playwright_project, ITEM_TO_FIND=None):
        page = setup_playwright_project
        adv_page = AdvPage(page)
        search_page = SearchPage(page)
        search_page.click_on_advanced_link()
        adv_page.search_for_item(ITEM_TO_FIND)
        text = search_page.get_amount_after_search()
        assert int(text) > 100, "products did not found "
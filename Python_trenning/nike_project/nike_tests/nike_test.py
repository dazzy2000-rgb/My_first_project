import time

from PythonProject.Python_trenning.nike_project.nike_pages.nike_card_page import NikeCardPage
from PythonProject.Python_trenning.nike_project.nike_pages.nike_homepage import Homepage
from PythonProject.Python_trenning.nike_project.nike_pages.nike_search_result_page import SearchResultsPage


class TestNikeTest():
    def test_search_item(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        home = Homepage(page)
        home.load()
        item = "air jordan"
        home.search_for_item(item)
        item_clean = item.lower().replace(" ", "")
        url_clean = page.url.lower().replace("%20", "")

        assert item_clean in url_clean


    def test_search_results_amount(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        search_page = SearchResultsPage(page)
        home = Homepage(page)
        home.load()
        home.search_for_item("jordan")
        amount = search_page.get_amount_after_search_text()
        assert amount > 0

    def test_jordan_categories(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        home = Homepage(page)
        home.load()
        home.search_for_item("jordan")
        results = SearchResultsPage(page)
        results.get_amount_after_search_text()
        results.print_jordan_categories()

        assert "jordan" in page.url.lower()

    def test_product_page(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        home = Homepage(page)
        home.load()
        home.search_for_item("Air")
        results = SearchResultsPage(page)
        results.open_first_product()

        card = NikeCardPage(page)
        title = card.get_product_title()

        assert len(title) > 0

    def test_product_url_changed(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        home = Homepage(page)
        home.load()
        home.search_for_item("Men")
        results = SearchResultsPage(page)
        results.open_first_product()
        card = NikeCardPage(page)

        assert card.is_product_url()

    def test_products_exist_after_search(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        home = Homepage(page)
        results = SearchResultsPage(page)
        home.load()
        home.search_for_item("Run")
        count = results.get_products_count()

        assert count > 1

    def test_product_title_contains_search_word(self, setup_playwright_project_nike):
        page = setup_playwright_project_nike
        home = Homepage(page)
        results = SearchResultsPage(page)
        card = NikeCardPage(page)
        home.load()
        home.search_for_item("Air")
        results.open_first_product()
        title = card.get_product_title()

        assert "air" in title.lower()
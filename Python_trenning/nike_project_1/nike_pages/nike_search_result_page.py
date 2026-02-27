import time


class SearchResultsPage:
    def __init__(self, page):
        self.page = page

    def search_item(self,item: str):
        search_menu = self.page.locator("[id='gn-search-input']")
        search_menu.click()
        search_menu.fill(item)
        search_menu.press("Enter")

    def get_amount_after_search_text(self):
        print("trying to get results")
        time.sleep(3)
        text_element = self.page.locator("[class*='wall-header__content']")
        text = text_element.inner_text()
        print(f"raw text: {text}")
        start = text.index("(")
        end = text.index(")")
        number = text[start + 1:end]
        amount = int(number)
        print(f"result amount is {amount}")
        return amount

    def print_jordan_categories(self):
        print("printing categories with jordan")
        categories = self.page.locator("text=Jordan")
        count = categories.count()
        for i in range(count):
            text = categories.nth(i).inner_text()
            print(f"CATEGORY: {text}")

    def open_first_product(self):
        print("opening first product")
        time.sleep(3)
        products = self.page.locator("[data-testid='product-card']")
        products.first.click()
        self.page.wait_for_load_state("load")

    def get_products_count(self):
        print("getting products count")
        time.sleep(3)
        products = self.page.query_selector_all("[data-testid='product-card']")
        count = len(products)
        print(f"PRODUCTS COUNT: {count}")
        return count

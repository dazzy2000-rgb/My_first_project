import time


class NikeCardPage:
    def __init__(self, page):
        self.page = page

    def get_product_title(self):
        print("getting product title")
        time.sleep(2)
        title = self.page.locator("[id='pdp_product_title']").inner_text()
        print(f"PRODUCT TITLE: {title}")

        return title

    def is_product_url(self):
        print("checking product url")
        url = self.page.url
        print(f"PRODUCT URL: {url}")

        return "/t/" in url or "/product/" in url

class Testzara():

    def test_zara(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.zara.com/il/en/")
        shopping = page.locator("a.layout-header-desktop-action-cart[data-qa-id='layout-actions-cart']")
        label = shopping.get_attribute("aria-label")
        print("aria-label:", label)
        assert label == "Basket empty"

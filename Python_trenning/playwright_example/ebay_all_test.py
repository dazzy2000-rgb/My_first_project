class TestEbayAdvanced ():

    def test_ebay_advanced(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        button = page.get_by_role("link", name="Advanced")
        button.click()
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch","Page did not load correctly"
        print("End test")
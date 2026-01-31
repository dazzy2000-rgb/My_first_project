class TestEbayAdvanced ():

    def test_ebay_advanced(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        button = page.get_by_role("link", name="Advanced")
        button.click()
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch","Page did not load correctly"
        print("End test")

    def test_ebay_drop_down_example (self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        button = page.get_by_role("link", name="Advanced")
        button.click()
        drop_down = page.locator("[id='s0-1-20-4[0]-7[3]-_sacat']")
        drop_down.select_option(label="Art")
        print("End test")

    def test_ebay_checkbox_example (self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.ebay.com/")
        button = page.get_by_role("link", name="Advanced")
        button.click()

        sold = page.locator("[name = 'LH_Sold']")
        sold.check()
        print("End test")
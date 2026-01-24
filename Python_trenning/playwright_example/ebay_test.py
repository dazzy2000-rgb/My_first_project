from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com")
    search = page.locator("[id='gh-ac']")
    search.click()
    search.clear()
    search.fill("Box")
    search_button = page.locator("[id='gh-search-btn']")
    search_button.click()

    browser.close()
    print("Test end")
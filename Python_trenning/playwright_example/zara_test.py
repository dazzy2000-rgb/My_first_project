from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.zara.com/il/en/")
    shopping = page.locator("a.layout-header-desktop-action-cart[data-qa-id='layout-actions-cart']")
    label = shopping.get_attribute("aria-label")
    print("aria-label:", label)
    assert label == "Basket empty"

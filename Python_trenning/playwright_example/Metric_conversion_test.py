from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_default_navigation_timeout(60000)
    page.goto("https://www.metric-conversions.org/", wait_until="domcontentloaded")
    page.locator("a[href*='temperature']").first.click()
    page.wait_for_url("**/temperature-conversion.htm")
    print("end test")


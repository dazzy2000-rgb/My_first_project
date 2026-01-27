from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    search_find = page.locator("[id='searchform']")
    search_find.click()
    search_find.clear()
    search_find.fill("potato")
    password = page.locator("[id='password']")
    password.fill("secret_sauce")
    login_button = page.locator("[id='login-button']")
    login_button.click()
    time.sleep(3)
    url= page.url
    print(f"url:{url}")
    page.close()
    browser.close()
    print("### Test end ###")
    if url == "https://www.saucedemo.com/inventory.html":
        print(f"###Test Pass###")
    else:
        print(f"###Test Fail###")
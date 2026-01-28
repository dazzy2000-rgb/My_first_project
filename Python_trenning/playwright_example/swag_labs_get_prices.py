from playwright.sync_api import sync_playwright

from PythonProject.Python_trenning.playwright_example.swag_labs_test import url

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator("[id='user-name']")
    user_name.fill("standard_user")
    password = page.locator("[id='password']")
    password.fill("secret_sauce")
    login_button = page.locator("[name='login-button']")
    login_button.click()
    prices=page.query_selector_all("[class='inventory_item_price']")
    for price in prices:
        print (price.inner_text())
    page.close()
    # browser.close()
    print("### Test end ###")
    if url == "https://www.saucedemo.com/inventory.html":
        print(f"###Test Pass###")
    else:
        print(f"###Test Fail###")


import time

from playwright.sync_api import sync_playwright

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
    prices=page.locator("[class='inventory_item_price']")
    print(prices[0].)
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

#
# def test_swaglabs_correct_login(setup_playwright):
#     pass
#
#
# with test_swaglabs_correct_login(setup_playwright):
#         print ("into test_swaglabs_correct_login")
#         page = setup_playwright
#         page.goto("https://www.saucedemo.com/")
#
#         user = page.locator("#user-name")
#         user.fill("standard_user")
#         password = page.locator("#password")
#         password.fill("secret_sauce")
#         login_btn = page.get_by_text("login")
#         login_btn.click()
#         current_url = page.url
#         assert current_url == "https://www.saucedemo.com/inventory.html", "current URL is not as expected"
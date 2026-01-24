import time

import login
from playwright.sync_api import sync_playwright


class Sign_in:
    pass


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.applitools.com/")
    user_name = page.locator("[id='username']")
    user_name.fill("Margarita")
    password = page.locator("[id='password']")
    password.fill("2417D")
    login_button = page.locator("[id='log-in']")
    login_button.click()

    page.close()
    browser.close()
    print("### Test end ###")
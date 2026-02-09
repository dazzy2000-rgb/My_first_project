import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    contact=page.get_by_role("link", name="Contact")
    contact.click()
    page.locator("#exampleModal .modal-footer button.btn-secondary").click()
    # close_button = page.get_by_role("button", name="Close")
    # close_button.click()
    # assert Pass.input_value()=="2"
    # assert From.input_value() == "London"
    time.sleep(5)
    browser.close()
    print("Test end")
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/reservation.php")
    Type=page.locator("[value='oneway']")
    Type.check()
    Pass = page.locator("[name='passCount']")
    Pass.select_option("2")
    From = page.locator("[name='fromPort']")
    From.select_option("London")
    On = page.locator("[name='fromMonth']")
    On.select_option("6")
    Date = page.locator("[name='fromDay']")
    Date.select_option("5")
    To = page.locator("[name='toPort']")
    To.select_option("Portland")
    Back = page.locator("[name='toMonth']")
    Back.select_option("7")
    Back_Date = page.locator("[name='toDay']")
    Back_Date.select_option("5")
    Business_class= page.locator("[name='servClass'][value='Business']")
    Business_class.check()
    Airline= page.locator("[name='airline']")
    Airline.select_option("Blue Skies Airlines")
    Continue= page.locator("[name='findFlights']")
    Continue.click()

    # assert Pass.input_value()=="2"
    # assert From.input_value() == "London"

    browser.close()
    print("Test end")
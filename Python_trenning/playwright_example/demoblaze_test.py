
class Testdemoblaze():

    def test_demoblaze(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")
        contact=page.get_by_role("link", name="Contact")
        contact.click()
        close_but = page.query_selector_all('[class*="btn-secondary"]')
        close_but[0].click()
        print("Test end")
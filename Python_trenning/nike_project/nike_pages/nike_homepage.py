class Homepage():
    def __init__(self,page):
        self.page = page

    def load(self):
        print("Opening Nike homepage")
        self.page.goto("https://www.nike.com/il/")

    def search_for_item(self,item):
        print(f"trying to search for {item}")

        search_icon = self.page.locator("[id='nav-search-icon']")
        search_icon.click()

        search_menu = self.page.locator("[id='gn-search-input']")
        search_menu.click()
        search_menu.fill(item)
        search_menu.press("Enter")






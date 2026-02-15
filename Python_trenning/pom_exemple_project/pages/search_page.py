
class SearchPage():
    def __init__(self, page):
        self.page = page

    def search_for_items(self,item):
        search_menu = self.page.locator("[id='gh-ac']")
        search_menu.click()
        search_menu.fill(item)

        self.page.get_by_role("button",name="Search",exact=True).click()
    def get_amount_after_search(self):
        print("Trying to get result after search")
        text = self.page.locator(".srp-controls__count-heading").inner_text()

        index =text.index("+")
        text =text[:index]
        text = text.replace(",","")
        print(f"result text is {text}")
        return text

    def click_on_advanced_link(self):
        adv_button = self.page.get_by_role("link", name="Advanced")
        adv_button.click()

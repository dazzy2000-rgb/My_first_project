
class BankLoginPage:
    def __init__(self, page):
        self.page = page
        self.manager_login_btn = page.get_by_role("button", name="Bank Manager Login")
    def open(self):
        self.page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    def login_as_manager(self):
        self.manager_login_btn.click()
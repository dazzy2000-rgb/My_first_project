
class BankManagerPage:
    def __init__(self, page):
        self.page = page

        # locators
        self.add_customer_btn = page.get_by_role("button", name="Add Customer")
        self.open_account_btn = page.get_by_role("button", name="Open Account")
        self.customers_btn = page.get_by_role("button", name="Customers")

    def read_buttons_texts(self) -> dict:
        return {
            "add_customer": self.add_customer_btn.inner_text(),
            "open_account": self.open_account_btn.inner_text(),
            "customers": self.customers_btn.inner_text(),
        }
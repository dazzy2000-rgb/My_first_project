from PythonProject.Python_trenning.xyz_exemple_project.xyz_pages.bank_page import BankManagerPage
from PythonProject.Python_trenning.xyz_exemple_project.xyz_pages.customerLogin_page import BankLoginPage


class TestBankTest:
    def test_Login_for_bank(self, setup_playwright_xyz_project):
        page = setup_playwright_xyz_project

        login_page = BankLoginPage(page)
        manager_page = BankManagerPage(page)

        login_page.open()
        login_page.login_as_manager()

        texts = manager_page.read_buttons_texts()
        print(texts)

        assert texts["add_customer"] == "Add Customer"
        assert texts["open_account"] == "Open Account"
        assert texts["customers"] == "Customers"
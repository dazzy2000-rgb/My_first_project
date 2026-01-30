

class Testcalculator ():

    def test_calculate_bmi_button(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        bmi = page.get_by_text("BMI Calculator")
        bmi.click()
        assert page.url == "https://www.calculator.net/bmi-calculator.html","Page did not load correctly"
        print("End test")

    def test_calculate_get_by_role(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        payment_button = page.get_by_role("Link", name = "payment calculator")
        payment_button.click()
        assert page.url == "https://www.calculator.net/payment-calculator.html", "Page did not load correctly"
        print("End test")
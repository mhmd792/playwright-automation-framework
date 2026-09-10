from playwright.sync_api import Page, expect

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.continue_shopping = page.locator("#continue-shopping")
        self.checkout_button = page.locator("#checkout")

    def return_to_inventory(self):
        self.continue_shopping.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def checkout(self):
            self.checkout_button.click()
            expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    



 

 


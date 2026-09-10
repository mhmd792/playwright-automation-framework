from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_message = page.locator("[data-test='error']")

    def open_from_cart(self):
        self.cart_link.click()
        self.checkout_button.click()

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def is_on_overview_page(self):
        return "checkout-step-two.html" in self.page.url

    def is_error_visible(self):
        return self.error_message.is_visible()

    def get_error_text(self):
        return self.error_message.text_content() if self.is_error_visible() else None

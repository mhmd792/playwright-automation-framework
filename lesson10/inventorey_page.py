from playwright.sync_api import Page, expect

class inventory_page:
    def __init__(self, page: Page):
        self.page = page
        self.add_backpack_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_badge = page.locator(".shopping_cart_badge")


    def add_backpack_to_cart(self):
        self.add_backpack_button.click()
        expect(self.cart_badge).to_have_text("1",timeout=3000)


    def add_object(self,name:srting):
        self.add_backpack_button.click()
        add_object=self.page.locator(f"#add-to-cart-{name}")
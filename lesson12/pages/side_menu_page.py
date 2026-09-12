from playwright.sync_api import Page

class SideMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.open_menu_btn = page.get_by_role("button", name="Open Menu")
        self.about_link = page.get_by_test_id("about-sidebar-link")

    def open(self):
        self.open_menu_btn.click()

    def go_to_about(self):
        self.about_link.click()
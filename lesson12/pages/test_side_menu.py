import re
from playwright.sync_api import Page, expect
from pages.side_menu_page import SideMenuPage

def test_about_link_navigates_to_saucelabs(logged_in_page: Page):
    menu = SideMenuPage(logged_in_page)

    menu.open()
    expect(menu.about_link).to_be_visible()

    menu.go_to_about()
    expect(logged_in_page).to_have_url(re.compile(r"saucelabs\.com"))
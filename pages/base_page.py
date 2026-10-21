from playwright.sync_api import Page, expect

from components.footer import FooterPage
from components.main_header import MainHeader
from components.upper_header import UpperHeader

class BasePage:

    def __init__(self, page: Page):
        self.page = page

        self.upper_header = UpperHeader(page)
        self.main_header = MainHeader(page)
        self.footer = FooterPage(page)

    def open(self, url: str):
        self.page.goto(url)

    def reload(self):
        self.page.reload()

    def get_title(self) -> str:
        return self.page.title()

    def check_url(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)
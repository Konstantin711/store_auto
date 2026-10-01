from playwright.sync_api import Page


class MainHeader:
    def __init__(self, page: Page):

        self.logo_icon = ''
        self.catalog_nav = '???'
        self.search_input = '???'
        self.like_link = ''
        self.cart_link = ''


    def click_logo(self):
        self.logo_icon.click()

    def click_nav_menu(self):
        pass

    def make_item_search(self):
        pass

    def open_liked_page(self):
        pass

    def open_cart_page(self):
        pass
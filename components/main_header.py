from playwright.sync_api import Page, expect


class MainHeader:
    def __init__(self, page: Page):
        self._page = page
        self.logo_icon = page.get_by_role("link", name="MATCH TOBI")
        self.search_input = page.get_by_role("combobox", name="Пошук товарів", exact=True)
        self.like_link = page.locator("//a[@href='/favorites']")
        self.cart_link = page.locator("//a[@href='/cart']")


    def click_logo(self):
        self.logo_icon.click()

    def click_nav_menu(self, f_level: str, s_level: str):
        f_level_el = self._page.get_by_role(
            "button",
            name=f_level,
            exact=True,
        )
        f_level_el.click()

        expect(f_level_el).to_have_attribute("aria-expanded", "true")

        s_level_el = self._page.get_by_role(
            "link",
            name=s_level,
            exact=True,
        )
        expect(s_level_el).to_be_visible()

        s_level_el.click()

    def make_item_search(self, search_data):
        expect(self.search_input).to_be_visible()
        self.search_input.fill(search_data)

    def open_liked_page(self):
        self.like_link.click()

    def open_cart_page(self):
        self.cart_link.click()
from playwright.sync_api import Page


class UpperHeader:
    def __init__(self, page: Page):
        self.about_us_page_link = page.locator(
            "//nav[contains(@class, 'top-header')]//a[@href='/about_us']"
        )
        self.payment_delivery_page_link = page.locator(
            "//nav[contains(@class, 'top-header')]//a[@href='/delivery']"
        )
        self.contact_phone_number = page.locator(
            "//div[@class='top-header-contacts']/a[@class='h-phone']"
        )
        self.contact_email = page.locator(
            "//div[@class='top-header-contacts']/a[@class='h-email']"
        )
        self.tik_tok_link = page.get_by_test_id("instagram-link")
        self.insta_link = page.get_by_test_id("tiktok-link")

        self.login_register_link = page.locator("//a[@href='/login']")
        self.logged_user_menu = page.locator("//div[contains(@class, 'user-email')]/a")


    def open_about_us_page(self):
        self.about_us_page_link.click()

    def open_payment_delivery_page(self):
        self.payment_delivery_page_link.click()

    def open_tik_tok_page(self):
        self.tik_tok_link.click()

    def open_insta_page(self):
        self.insta_link.click()

    def open_register_page(self):
        self.login_register_link.click()

    def open_login_page(self):
        self.login_register_link.click()

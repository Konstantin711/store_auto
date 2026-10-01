from playwright.sync_api import Page


class UpperHeader:
    def __init__(self, page: Page):
        self.about_us_page_link = page.get_by_role("link", name="Про нас", exact=True)
        self.payment_delivery_page_link = page.get_by_role("link", name="Оплата та Доставка", exact=True)

        self.contact_phone_number = ''
        self.contact_email = ''

        self.tik_tok_link = ''
        self.insta_link = ''

        self.login_register_link = ''
        self.logged_user_menu = ''


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

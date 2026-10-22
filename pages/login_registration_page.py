from playwright.sync_api import Page


class LoginRegisterPage:
    def __init__(self, page: Page):
        self.login_tab = page.locator("//ul[@id='auth-tabs']//button[@text()='Логін']")
        self.log_email_input = page.locator("//input[@id='loginEmail']")
        self.log_password_input = page.locator("//input[@id='loginPassword']")
        self.login_btn = page.get_by_role("button", name="Увійти", exact=True)

        self.register_tab = page.locator("//ul[@id='auth-tabs']//button[@text()='Реєстрація']")
        self.reg_name_input = page.locator("//input[@id='registrationName']")
        self.reg_email_input = page.locator("//input[@id='registrationEmail']")
        self.reg_pass_input = page.locator("//input[@id='registrationPassword']")
        self.reg_re_pass_input = page.locator("//input[@id='registrationConfirmPassword']")
        self.register_btn = page.locator("//button[@type='submit'][@text()='Увійти']")


    def fill_login_form(self, email, password):
        self.log_email_input.fill(email)
        self.log_password_input.fill(password)

    def fill_registration_form(self, name, email, password, repeat_password):
        self.reg_name_input.fill(name)
        self.reg_email_input.fill(email)
        self.reg_pass_input.fill(password)
        self.reg_re_pass_input.fill(repeat_password)

    def click_login_tab(self):
        self.login_btn.click()

    def click_register_tab(self):
        self.register_btn.click()

    def make_login(self, email, password):
        self.fill_login_form(email, password)
        self.login_btn.click()

    def make_register(self, name, email, password, repeat_password):
        self.fill_registration_form(name, email, password, repeat_password)
        self.register_btn.click()

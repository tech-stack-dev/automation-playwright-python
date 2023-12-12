from playwright.sync_api import Locator
from base.page.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logo: Locator = self.page.locator("//a[contains(@class, 'navbar-brand')]")
        self.add_user_button: Locator = self.page.locator("//a[contains(., 'Add User')]")

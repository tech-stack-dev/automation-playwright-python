from base.page.base_page import BasePage
from playwright.sync_api import Locator


class AddUserPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.user_name_input: Locator = self.page.locator("//input[@id='inputUserName']")
        self.year_input_validation_message: Locator = self.page.locator("//span[@data-testid='inputError-YearOfBirth']")
        self.cancel_button: Locator = self.page.locator("//a[contains(@class, 'btn btn-secondary')]")
        self.create_button: Locator = self.page.locator("//button[contains(@class, 'btn btn-primary')]")

from playwright.async_api import Locator
from playwright.async_api import expect
from base.driver.driver import driver
from pages.home_page import HomePage


class HomePageSteps:
    async def check_logo(self):
        logo: Locator = driver.get_page(HomePage).logo
        await expect(logo).to_be_visible(timeout=5000)

    async def click_logo(self):
        await driver.get_page(HomePage).logo.click()

    async def click_add_user_button(self):
        await driver.get_page(HomePage).add_user_button.click()


home_page_steps = HomePageSteps()

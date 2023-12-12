from typing import Any, List

from playwright._impl._playwright import Playwright
from playwright.async_api import async_playwright
from base.driver.broswers_enum import BrowsersEnum
from base.driver.base_driver import BaseDriver


class Driver(BaseDriver):
    def __init__(self):
        super().__init__()
        self.browser = Any
        self.headless = False
        self._browsers: List[Any] = []

    @property
    def browsers(self):
        return self._browsers

    def collect_browsers(self, browser):
        self.browsers.append(browser)

    async def create_browser(self, browser_name: BrowsersEnum, playwright: Playwright):
        BaseDriver.focused_driver = Driver()
        BaseDriver.focused_driver.browser = await playwright.chromium.launch(headless=self.headless)
        BaseDriver.focused_driver.driver_name = browser_name
        BaseDriver.focused_driver.driver_context = await BaseDriver.focused_driver.browser.new_context()
        BaseDriver.focused_driver.page = await BaseDriver.focused_driver.driver_context.new_page()
        BaseDriver.focused_driver.list_of_pages.append(BaseDriver.focused_driver.page)
        self.collect_browsers(driver.focused_driver)
        BaseDriver.list_of_drivers = self.browsers
        return self


    async def close_drivers(self):
        for driver_to_close in BaseDriver.list_of_drivers:
            BaseDriver.focused_driver = driver_to_close

            try:
                await self.driver_context.close()
            except Exception as error:
                print(f"An error occurred while closing the browser context '{driver_to_close}': {error}")

            try:
                await self.close()
            except Exception as error:
                print(f"An error occurred while closing browser '{driver_to_close}': {error}")

        BaseDriver.list_of_drivers = []


driver = Driver()

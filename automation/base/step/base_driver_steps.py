from playwright._impl._playwright import Playwright

from base.driver.driver import driver
from base.driver.broswers_enum import BrowsersEnum
from base.driver.base_driver import BaseDriver

class BaseDriverSteps:
    async def creates_new_browser(self, browser_name: BrowsersEnum, playwright: Playwright):
        await driver.create_browser(browser_name, playwright)

    async def creates_new_browser_and_go_to_url(self, url: str, browser_name: BrowsersEnum, playwright: Playwright):
        await driver.create_browser(browser_name, playwright)
        await self.go_to_url(url)

    async def create_new_page(self):
        new_page = await driver.driver_context.new_page()
        driver.page = new_page
        driver.list_of_pages.append(new_page)

    async def switch_to_browser(self, browser_name: BrowsersEnum):
        which_one = next((x for x in BaseDriver.list_of_drivers if x.driver_name == browser_name), None)
        BaseDriver.focused_driver = which_one

    async def switch_to_browser_tab(self, tab_number: int):
        driver.page = driver.list_of_pages[tab_number]

    async def close_browser(self):
        await driver.driver_context.close()

    async def close_browser_tab(self):
        await driver.page.close()

    async def go_to_url(self, url: str):
        await driver.page.goto(url)


base_driver_steps = BaseDriverSteps()

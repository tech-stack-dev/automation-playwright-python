from playwright.sync_api import Locator
from base.driver.driver import driver


class ButtonSteps:
    def click_button(self, component_type, identifier: str, parent: Locator = None):
        (driver.component(component_type, identifier, parent)).click()


button_steps = ButtonSteps()

from playwright.sync_api import Locator
from base.driver.driver import driver


class FormSteps:
    def fill_text_field(self, text: str, component_type, identifier: str, parent: Locator = None):
        (driver.component(component_type, identifier, parent)).fill(text)


form_steps = FormSteps()

from playwright.sync_api import Locator, Page
from base.component.base_component import BaseComponent


class TextFieldById(BaseComponent):
    def __init__(self, page: Page, identifier: str, parent: Locator = None):
        super().__init__(identifier, page, parent=parent)
        self.component_context = f'//input[@id="{identifier}"]'

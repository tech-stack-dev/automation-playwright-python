from playwright.sync_api import Locator, Page
from base.component.base_component import BaseComponent


class FormByRole(BaseComponent):
    def __init__(self, page: Page, identifier: str, parent: Locator = None):
        super().__init__(identifier, page, parent=parent)
        self.component_context = f'//main[@role="{identifier}"]'

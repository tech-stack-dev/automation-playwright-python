from typing import List, Type, TypeVar, Any
from playwright.async_api import Browser, BrowserContext, Locator, Page
from base.component.base_component import BaseComponent
from base.driver.broswers_enum import BrowsersEnum

T = TypeVar("T", bound=BaseComponent)


class BaseDriver:
    focused_driver: 'BaseDriver' = Any
    list_of_drivers: List['BaseDriver'] = []

    def __init__(self):
        self._driver_context: BrowserContext = Any
        self._page: Page = Any
        self._list_of_pages: List[Page] = []
        self._driver_name: BrowsersEnum = Any
        self.browser: Browser = Any

        # Permissions and args
        self._permissions: List[str] = []
        self._args: List[str] = []

    @property
    def driver_context(self) -> BrowserContext:
        return BaseDriver.focused_driver._driver_context

    @driver_context.setter
    def driver_context(self, value: BrowserContext):
        BaseDriver.focused_driver._driver_context = value

    @property
    def page(self) -> Page:
        return BaseDriver.focused_driver._page

    @page.setter
    def page(self, value: Page):
        BaseDriver.focused_driver._page = value

    @property
    def list_of_pages(self) -> list[Page]:
        return BaseDriver.focused_driver._list_of_pages

    @list_of_pages.setter
    def list_of_pages(self, value: list[Page]):
        BaseDriver.focused_driver._list_of_pages = value

    @property
    def driver_name(self) -> BrowsersEnum:
        return BaseDriver.focused_driver._driver_name

    @driver_name.setter
    def driver_name(self, value: BrowsersEnum):
        BaseDriver.focused_driver._driver_name = value

    @property
    def permissions(self) -> List[str]:
        return BaseDriver.focused_driver._permissions

    @permissions.setter
    def permissions(self, value: List[str]):
        BaseDriver.focused_driver._permissions = value

    @property
    def args(self) -> List[str]:
        return BaseDriver.focused_driver._args

    @args.setter
    def args(self, value: List[str]):
        BaseDriver.focused_driver._args = value

    async def close(self):
        await BaseDriver.focused_driver.browser.close()

    async def component(self, component_type: Type[T], identifier: str, parent: Locator = None) -> T:
        component = component_type(BaseDriver.focused_driver.page, identifier, parent)
        return await self.component_build(component)

    async def component_build(self, component: T) -> T:
        if component.Parent:
            component.Element = component.parent.locator(f"xpath={component.component_context}")
        else:
            component.Element = component.page.locator(f"xpath={component.component_context}")
        return component

    def locator(self, selector: str, base_element: Locator = None) -> Locator:
        if base_element:
            return base_element.locator(selector)
        else:
            return BaseDriver.focused_driver.page.locator(selector)

    def get_by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def get_page(self, page_type: Type[T]) -> T:
        return page_type(BaseDriver.focused_driver.page)

    async def execute_func(self, func, attempts: int):
        error = None
        for i in range(attempts):
            try:
                await func()
                return
            except Exception as err:
                print(f"{i + 1} attempt to execute {func.__name__}")
                error = err

        if error:
            raise error

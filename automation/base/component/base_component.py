import typing
from playwright.sync_api import Locator, Page, ElementHandle, FrameLocator, JSHandle


class BaseComponent(Locator):
    _element: Locator

    def __init__(self, identifier: str, page: Page, *, parent: Locator, impl_obj: typing.Any):
        super().__init__(impl_obj)
        self._component_context = None
        self.identifier = identifier
        self._page = page
        self._parent = parent

    @property
    def Element(self) -> Locator:
        return self._element

    @Element.setter
    def Element(self, value: Locator):
        self.Element = value

    @property
    def Parent(self) -> Locator:
        return self._parent

    @Parent.setter
    def Parent(self, value: Locator):
        self._parent = value

    @property
    def Page(self) -> Page:
        return self._page

    @Page.setter
    def Page(self, value: Page):
        self._page = value

    @property
    def ComponentContext(self):
        return self._component_context

    @ComponentContext.setter
    def ComponentContext(self, context: str):
        self._component_context = context

    def or_(self, locator: Locator) -> Locator:
        return self._element.or_(locator)

    def and_(self, locator: Locator) -> Locator:
        return self._element.and_(locator)

    def all(self) -> list[Locator]:
        return self._element.all()

    def blur(self, **options):
        return self._element.blur(**options)

    def clear(self, **options) -> None: return self._element.clear(**options)

    def get_by_alt_text(self, text, **options) -> Locator:
        return self._element.get_by_alt_text(text, **options)

    def get_by_label(self, text, **options) -> Locator:
        return self._element.get_by_label(text, **options)

    def get_by_placeholder(self, text, **options) -> Locator:
        return self._element.get_by_placeholder(text, **options)

    def get_by_role(self, text, **options) -> Locator:
        return self._element.get_by_role(text, **options)

    def get_by_test_id(self, text) -> Locator:
        return self._element.get_by_test_id(text)

    def get_by_text(self, text, **options) -> Locator:
        return self._element.get_by_text(text, **options)

    def get_by_title(self, text, **options) -> Locator:
        return self._element.get_by_title(text, **options)

    def evaluate(self, **options) -> Locator:
        return self._element.evaluate(**options)

    def evaluate_all(self, **options) -> list[Locator]:
        return self._element.evaluate_all(**options)

    def element_handle(self, **options) -> ElementHandle:
        return self._element.element_handle(**options)

    def all_inner_texts(self) -> list[str]:
        return self._element.all_inner_texts()

    def all_text_contents(self) -> list[str]:
        return self._element.all_text_contents()

    def bounding_box(self, **options):
        return self._element.bounding_box(**options)

    def check(self, **options):
        return self._element.check(**options)

    def click(self, **options):
        return self._element.click(**options)

    def count(self) -> int:
        return self._element.count()

    def dblclick(self, **options):
        return self._element.dblclick(**options)

    def drag_to(self, target: Locator, **options):
        return self._element.drag_to(target, **options)

    def element_handles(self):
        return self._element.element_handles()

    def fill(self, value: str, **options):
        return self._element.fill(value, **options)

    def filter(self, **options) -> Locator:
        return self._element.filter(**options)

    def first(self) -> Locator:
        return self._element.first

    def focus(self, **options):
        return self._element.focus(**options)

    def frame_locator(self, selector: str) -> FrameLocator:
        return self._element.frame_locator(selector)

    def get_attribute(self, name: str, **options) -> str:
        return self._element.get_attribute(name, **options)

    def highlight(self):
        return self._element.highlight()

    def hover(self, **options):
        return self._element.hover(**options)

    def inner_html(self, **options) -> str:
        return self._element.inner_html(**options)

    def inner_text(self, **options) -> str:
        return self._element.inner_text(**options)

    def input_value(self, **options) -> str:
        return self._element.input_value(**options)

    def is_checked(self, **options) -> bool:
        return self._element.is_checked(**options)

    def is_disabled(self, **options) -> bool:
        return self._element.is_disabled(**options)

    def is_editable(self, **options) -> bool:
        return self._element.is_editable(**options)

    def is_enabled(self, **options) -> bool:
        return self._element.is_enabled(**options)

    def is_hidden(self, **options) -> bool:
        return self._element.is_hidden(**options)

    def is_visible(self, **options) -> bool:
        return self._element.is_visible(**options)

    def last(self) -> Locator:
        return self._element.last

    def locator(self, selector: str, **options) -> Locator:
        return self._element.locator(selector, **options)

    def nth(self, index: int) -> Locator:
        return self._element.nth(index)

    def page(self) -> Page:
        return self._element.page

    def press(self, key: str, **options):
        return self._element.press(key, **options)

    def screenshot(self, **options) -> bytes:
        return self._element.screenshot(**options)

    def scroll_into_view_if_needed(self, **options):
        return self._element.scroll_into_view_if_needed(**options)

    def select_option(self, **options):
        return self._element.select_text(**options)

    def select_text(self, **options):
        return self._element.select_text(**options)

    def set_checked(self, checked: bool, **options):
        return self._element.set_checked(checked, **options)

    def set_input_files(self, files, **options):
        return self._element.set_input_files(files, **options)

    def tap(self, **options):
        return self._element.tap(**options)

    def text_content(self, **options) -> typing.Union[str, None]:
        return self._element.text_content(**options)

    def type(self, text: str, **options):
        return self._element.type(text, **options)

    def uncheck(self, **options):
        return self._element.uncheck(**options)

    def wait_for(self, **options):
        return self._element.wait_for(**options)

    def dispatch_event(self, type, event_init=None, **options):
        return self._element.dispatch_event(type, event_init, **options)

    def evaluate_handle(self, expression, arg=None, **options) -> JSHandle:
        return self._element.evaluate_handle(expression, arg, **options)

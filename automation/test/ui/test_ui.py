import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, expect
from base.driver.broswers_enum import BrowsersEnum
from base.driver.driver import driver
from base.step.base_driver_steps import base_driver_steps
from components.Button.button_by_data_test_id import ButtonByDataTestId
from components.Form.form_by_role import FormByRole
from components.Form.text_field_by_id import TextFieldById
from identifiers.buttons.buttons import Buttons
from identifiers.forms.add_user_form import AddUserForm
from providers.url_path import UrlPath
from providers.url_provider import UrlProvider
from steps.components.button_steps import button_steps
from steps.components.form_steps import form_steps
from steps.ui.add_user_page_steps import add_user_page_steps
from steps.ui.home_page_steps import home_page_steps


@pytest_asyncio.fixture
async def setup():
    async with async_playwright() as p:
        await base_driver_steps.creates_new_browser_and_go_to_url(UrlProvider.home_page_url(), BrowsersEnum.Browser_1, p)
        yield p
        await driver.close_drivers()


@pytest.mark.asyncio
async def test_example(setup):
    await home_page_steps.click_add_user_button()
    await add_user_page_steps.click_cancel_button()
    await home_page_steps.check_logo()


@pytest.mark.asyncio
async def test_example_2_browsers_2_pages(setup):
    await base_driver_steps.creates_new_browser(BrowsersEnum.Browser_2, setup)
    await base_driver_steps.go_to_url(UrlProvider.home_page_url())

    await home_page_steps.check_logo()

    await base_driver_steps.create_new_page()
    await base_driver_steps.go_to_url(UrlProvider.url_builder(UrlPath.AddUser))

    await add_user_page_steps.fill_user_name_input("testName")
    await add_user_page_steps.click_create_button()
    await add_user_page_steps.check_year_input_validation_message("Year of Birth is requried")

    await base_driver_steps.switch_to_browser(BrowsersEnum.Browser_1)
    await base_driver_steps.close_browser()


@pytest.mark.asyncio
async def test_example_with_components(setup):
    await base_driver_steps.go_to_url(UrlProvider.url_builder(UrlPath.AddUser))

    add_user_form = await driver.component(FormByRole, "main", parent=None)
    await form_steps.fill_text_field("testData", TextFieldById, "inputUserName", add_user_form.element)
    await form_steps.fill_text_field("1900", TextFieldById, "inputYearOfBirth", add_user_form.element)

    await button_steps.click_button(ButtonByDataTestId, Buttons.Cancel)


@pytest.mark.asyncio
async def test_example_with_test_id_attribute(setup):
    await base_driver_steps.go_to_url(UrlProvider.url_builder(UrlPath.AddUser))
    await driver.get_by_test_id(Buttons.Create).click()
    await expect(driver.get_by_test_id(AddUserForm.NameValidationMessage)).to_have_text("Name is requried")
    await driver.get_by_test_id(Buttons.Cancel).click()
    await expect(driver.get_by_test_id(Buttons.Delete).last).to_have_css("background-color", "rgb(220, 53, 69)")
    await driver.get_by_test_id(Buttons.Edit).nth(0).click()
    await driver.get_by_test_id(Buttons.Cancel).click()
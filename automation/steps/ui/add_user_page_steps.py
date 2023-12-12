from playwright.async_api import expect
from base.driver.driver import driver
from pages.add_user_page import AddUserPage


class AddUserPageSteps:
    async def fill_user_name_input(self, user_name: str):
        await driver.get_page(AddUserPage).user_name_input.fill(user_name)

    async def check_year_input_validation_message(self, message: str):
        await expect(driver.get_page(AddUserPage).year_input_validation_message).to_have_text(message)

    async def click_cancel_button(self):
        await driver.get_page(AddUserPage).cancel_button.click()

    async def click_create_button(self):
        await driver.get_page(AddUserPage).create_button.click()


add_user_page_steps = AddUserPageSteps()

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
from base.client.clients_enum import ClientsEnum
from base.client.context_options import ContextOptions
from base.client.request_options import RequestOptions
from base.step.base_api_steps import base_api_steps
from runtimeVariables.dto.user_dto import user_dto_variable
from steps.api.api_steps import api_steps


@pytest_asyncio.fixture
async def create_context():
    async with async_playwright() as p:
        context = ContextOptions(base_url=ClientsEnum.Client_1)
        await base_api_steps.create_client(p, context_options=context, client_name=ClientsEnum.Client_1)
        yield context


@pytest.mark.asyncio
async def test_api_get_request(create_context):
    context = create_context
    options = RequestOptions(url=context.base_url)
    await api_steps.execute_get_request("/api/users?page=2", request_options=options)
    await api_steps.check_property_value("page", 2)


def test_api_post_request(create_context):
    context = create_context
    user_dto_variable.value = {
        "name": "morpheus",
        "job": "leader",
    }

    request_options = RequestOptions(context.base_url)
    request_options.data = user_dto_variable.value

    api_steps.execute_post_request("/api/users", request_options, 201)
    api_steps.check_property_value("name", "morpheus")

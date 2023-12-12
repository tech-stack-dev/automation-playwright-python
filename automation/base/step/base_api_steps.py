from playwright.async_api import Playwright
from base.client.base_client import BaseClient
from base.client.client import client
from base.client.client import ClientsEnum
from base.client.context_options import ContextOptions


class BaseApiSteps:
    async def create_client(self, playwright: Playwright, client_name: ClientsEnum = ClientsEnum.Client_1, context_options: ContextOptions = None):
        await client.create_client(client_name, context_options, playwright)

    async def switch_to_client(self, client_name: ClientsEnum):
        BaseClient.focused_client = next((client for client in BaseClient.list_of_clients if client.client_name == client_name), None)


base_api_steps = BaseApiSteps()

from playwright.async_api import Playwright
from base.client.base_client import BaseClient
from base.client.clients_enum import ClientsEnum
from base.client.context_options import ContextOptions
from providers.url_provider import UrlProvider


class Client(BaseClient):
    async def create_client(self, client_name: ClientsEnum, context_options: ContextOptions, playwright: Playwright):
        focused_client = BaseClient()
        focused_client.client_name = client_name
        context_options.base_url = UrlProvider.client_url(client_name)
        BaseClient.focused_client.client_name = client_name
        client.client_context = await playwright.request.new_context(base_url=context_options.base_url, extra_http_headers=context_options.extra_http_headers, http_credentials=context_options.http_credentials, ignore_https_errors=context_options.ignore_https_errors, proxy=context_options.proxy, user_agent=context_options.user_agent, timeout=context_options.timeout, storage_state=context_options.storage_state)
        BaseClient.list_of_clients.append(BaseClient.focused_client)

        return self


client = Client()

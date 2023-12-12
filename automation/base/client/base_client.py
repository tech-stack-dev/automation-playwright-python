from typing import Optional, Dict, Any, Union

from playwright._impl._api_structures import Headers, FilePayload
from playwright._impl._connection import ChannelOwner
from playwright._impl._fetch import APIRequestContext, ParamsType, DataType, FormType, MultipartType, APIResponse

from base.client.clients_enum import ClientsEnum
from base.client.request_options import RequestOptions


class BaseClient:
    focused_client: 'BaseClient' = Any
    list_of_clients: list['BaseClient'] = []

    def __init__(self):
        self._client_name: Optional[ClientsEnum] = None
        self._client_context: Optional[APIRequestContext] = None

    @property
    def client_name(self) -> Optional[ClientsEnum]:
        return self._client_name

    @client_name.setter
    def client_name(self, value: ClientsEnum) -> None:
        self._client_name = value

    @property
    def client_context(self) -> Optional[APIRequestContext]:
        if BaseClient.focused_client:
            return BaseClient.focused_client._client_context
        return None

    @client_context.setter
    def client_context(self, value: APIRequestContext) -> None:
        if BaseClient.focused_client:
            BaseClient.focused_client._client_context = value

    async def delete(
        self,
        url: str,
        params: ParamsType = None,
        headers: Headers = None,
        data: DataType = None,
        form: FormType = None,
        multipart: MultipartType = None,
        timeout: float = None,
        failOnStatusCode: bool = None,
        ignoreHTTPSErrors: bool = None,
        maxRedirects: int = None,
    ) -> "APIResponse": return await self.client_context.delete(url, params, headers, data, form, multipart, timeout, failOnStatusCode, ignoreHTTPSErrors, maxRedirects)

    async def post(
        self,
        url: str,
        params: ParamsType = None,
        headers: Headers = None,
        data: DataType = None,
        form: FormType = None,
        multipart: Dict[str, Union[bytes, bool, float, str, FilePayload]] = None,
        timeout: float = None,
        failOnStatusCode: bool = None,
        ignoreHTTPSErrors: bool = None,
        maxRedirects: int = None,
    ) -> "APIResponse": return await self.client_context.post(url, params, headers, data, form, multipart, timeout, failOnStatusCode, ignoreHTTPSErrors, maxRedirects)

    async def get(
        self,
        url: str,
        params: ParamsType
    ) -> "APIResponse": return await self.client_context.get(url, params=params)

from typing import Any

from playwright.async_api import expect
from base.client.client import client
from base.client.request_options import RequestOptions
from runtimeVariables.dto.response_variable import ResponseVariable


class ApiSteps:
    async def execute_get_request(self, url: str, request_options: RequestOptions, statusCode = 200):
        ResponseVariable.set_value(await client.get(url=url, params=request_options.params))
        expect(ResponseVariable.get_value()).to_be_ok()
        assert ResponseVariable.get_value().status == statusCode

    async def execute_post_request(self, url: str, request_options: RequestOptions, statusCode = 200):
        ResponseVariable.set_value(await client.post(url=url, params=request_options.params, headers=request_options.headers, data=request_options.data, form=request_options.form, multipart=request_options.multipart, timeout=request_options.timeout,failOnStatusCode=request_options.fail_on_status_code,ignoreHTTPSErrors=request_options.ignore_https_errors,maxRedirects=request_options.max_redirects))
        expect(ResponseVariable.get_value()).to_equal(statusCode)

    async def check_property_value(self, property:str, expected_value: Any):
        response_json = await ResponseVariable.get_value().json()
        actual_value = response_json[property]
        assert actual_value == expected_value


api_steps = ApiSteps()

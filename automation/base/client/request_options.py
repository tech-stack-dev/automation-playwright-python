from typing import Optional

from playwright._impl._api_structures import Headers
from playwright._impl._fetch import ParamsType, DataType, FormType, MultipartType


class RequestOptions:
    def __init__(
        self,
        url: str,
        params: Optional[ParamsType] = None,
        headers: Optional[Headers] = None,
        data: Optional[DataType] = None,
        form: Optional[FormType] = None,
        multipart: Optional[MultipartType] = None,
        timeout: Optional[float] = None,
        fail_on_status_code: Optional[bool] = None,
        ignore_https_errors: Optional[bool] = None,
        max_redirects: Optional[int] = None,
    ):
        self.url = url
        self.params = params
        self.headers = headers
        self.data = data
        self.form = form
        self.multipart = multipart
        self.timeout = timeout
        self.fail_on_status_code = fail_on_status_code
        self.ignore_https_errors = ignore_https_errors
        self.max_redirects = max_redirects

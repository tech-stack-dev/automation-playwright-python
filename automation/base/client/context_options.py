from typing import Optional, Dict, List
from dataclasses import dataclass


@dataclass
class ContextOptions:
    base_url: Optional[str] = None
    extra_http_headers: Optional[Dict[str, str]] = None
    http_credentials: Optional[Dict[str, str]] = None
    ignore_https_errors: Optional[bool] = None
    proxy: Optional[Dict[str, str]] = None
    storage_state: Optional[Dict[str, List[Dict[str, any]]]] = None
    timeout: Optional[int] = None
    user_agent: Optional[str] = None

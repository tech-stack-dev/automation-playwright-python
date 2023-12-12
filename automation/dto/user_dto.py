from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class UserDto:
    name: str
    job: str
    id: Optional[str] = None
    created_at: Optional[datetime] = None

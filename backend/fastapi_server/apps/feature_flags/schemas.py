from typing import Optional

from pydantic import BaseModel


class FeatureFlagRead(BaseModel):
    codename: str
    label: Optional[str]
    description: Optional[str]
    is_active: bool

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndexListResponse", "Index"]


class Index(BaseModel):
    change: Optional[float] = None

    name: Optional[str] = None

    percent_change: Optional[float] = FieldInfo(alias="percentChange", default=None)

    price: Optional[float] = None

    symbol: Optional[str] = None


class IndexListResponse(BaseModel):
    indices: Optional[List[Index]] = None
